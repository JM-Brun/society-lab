#!/usr/bin/env python3
"""Download INSEE monthly SMIC/CPI series and reconstruct annual real SMIC levels.

The workflow keeps the raw source observations and the linked CPI series so that
the annual result can be reproduced and audited. It does not estimate causal
employment or poverty effects.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from datetime import datetime, timezone
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

START_YEAR = 1970
END_YEAR = 2025
SMIC_ID = "000822484"
CPI_1980_ID = "000008964"
CPI_2015_ID = "001759970"
BASE_URL = "https://bdm.insee.fr/series/sdmx/data/SERIES_BDM"
SOURCE_URLS = {
    "smic": f"{BASE_URL}/{SMIC_ID}?startPeriod=1970-01&endPeriod=2025-12",
    "cpi_1980": f"{BASE_URL}/{CPI_1980_ID}?startPeriod=1970-01&endPeriod=1992-12",
    "cpi_2015": f"{BASE_URL}/{CPI_2015_ID}?startPeriod=1990-01&endPeriod=2025-12",
}
ACCEPT = "application/vnd.sdmx.structurespecificdata+xml;version=2.1"


def fetch_bytes(url: str) -> bytes:
    request = urllib.request.Request(
        url,
        headers={"Accept": ACCEPT, "User-Agent": "society-lab-smic-research/1.0"},
    )
    last_error = None
    for attempt in range(4):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                payload = response.read()
                content_type = response.headers.get("Content-Type", "")
            break
        except (urllib.error.URLError, TimeoutError) as error:
            last_error = error
            if attempt == 3:
                raise
            delay = 2 ** (attempt + 1)
            print(f"Temporary INSEE connection failure; retrying in {delay}s: {error}", flush=True)
            time.sleep(delay)
    else:
        raise RuntimeError(f"Unable to download {url}") from last_error
    if not payload or ("xml" not in content_type.lower() and not payload.lstrip().startswith(b"<?xml")):
        raise ValueError(f"Unexpected response for {url}: {content_type}")
    return payload


def parse_sdmx_observations(payload: bytes) -> dict[str, float]:
    root = ET.fromstring(payload)
    observations: dict[str, float] = {}
    for node in root.iter():
        if node.tag.rsplit("}", 1)[-1] != "Obs":
            continue
        attrs = {key.rsplit("}", 1)[-1].upper(): value for key, value in node.attrib.items()}
        period = attrs.get("TIME_PERIOD")
        value = attrs.get("OBS_VALUE")
        if period is None or value is None:
            continue
        if period in observations:
            raise ValueError(f"duplicate observation for {period}")
        parsed = float(value)
        if not math.isfinite(parsed) or parsed <= 0:
            raise ValueError(f"invalid observation for {period}: {value}")
        observations[period] = parsed
    if not observations:
        raise ValueError("SDMX response contains no usable Obs elements")
    return dict(sorted(observations.items()))


def link_cpi_series(old_base: dict[str, float], new_base: dict[str, float]) -> tuple[dict[str, float], float]:
    """Express pre-1990 base-1980 observations on base-2015 scale.

    Following the published data.gouv linking convention, use the geometric
    mean of monthly new/old ratios over the 1990–1992 overlap.
    """
    overlap = sorted(set(old_base) & set(new_base))
    expected = [f"{year}-{month:02d}" for year in range(1990, 1993) for month in range(1, 13)]
    if overlap != expected:
        raise ValueError(f"CPI linking overlap must contain 36 months (1990–1992); got {len(overlap)}")
    factor = math.exp(sum(math.log(new_base[m] / old_base[m]) for m in overlap) / len(overlap))
    linked = {period: value * factor for period, value in old_base.items() if period < "1990-01"}
    linked.update(new_base)
    return dict(sorted(linked.items())), factor


def require_months(series: dict[str, float], start_year: int, end_year: int, label: str) -> None:
    expected = [f"{year}-{month:02d}" for year in range(start_year, end_year + 1) for month in range(1, 13)]
    missing = sorted(set(expected) - set(series))
    if missing:
        raise ValueError(f"{label}: missing {len(missing)} months; first missing: {missing[:5]}")
    extras = sorted(set(series) - set(expected))
    if extras:
        raise ValueError(f"{label}: unexpected periods: {extras[:5]}")


def annual_reconstruction(smic: dict[str, float], cpi: dict[str, float]) -> list[dict[str, str]]:
    require_months(smic, START_YEAR, END_YEAR, "SMIC")
    require_months(cpi, START_YEAR, END_YEAR, "CPI")
    rows = []
    ratios = {}
    for year in range(START_YEAR, END_YEAR + 1):
        months = [f"{year}-{month:02d}" for month in range(1, 13)]
        smic_avg = sum(smic[m] for m in months) / 12
        cpi_avg = sum(cpi[m] for m in months) / 12
        ratios[year] = smic_avg / cpi_avg
    base = ratios[2015]
    previous = None
    for year in range(START_YEAR, END_YEAR + 1):
        months = [f"{year}-{month:02d}" for month in range(1, 13)]
        smic_avg = sum(smic[m] for m in months) / 12
        cpi_avg = sum(cpi[m] for m in months) / 12
        ratio = ratios[year]
        change = "" if previous is None else f"{100 * (ratio / previous - 1):.6f}"
        rows.append({
            "year": str(year),
            "smic_hourly_gross_annual_avg_eur": f"{smic_avg:.6f}",
            "ipc_annual_avg_base_2015_100": f"{cpi_avg:.6f}",
            "smic_real_ratio": f"{ratio:.9f}",
            "real_smic_index_2015_100": f"{100 * ratio / base:.6f}",
            "real_purchasing_power_change_pct": change,
            "source_smic_idbank": SMIC_ID,
            "source_cpi_idbanks": f"{CPI_1980_ID}+{CPI_2015_ID}",
            "method": "ratio of annual means: mean(monthly SMIC) / mean(monthly CPI)",
            "confidence": "reconstructed_primary_series",
        })
        previous = ratio
    return rows


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=Path("artifacts/smic-monthly"))
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    raw = {}
    for name, url in SOURCE_URLS.items():
        print(f"Downloading {name}: {url}", flush=True)
        raw[name] = fetch_bytes(url)
        print(f"Downloaded {name}: {len(raw[name])} bytes", flush=True)
    raw_filenames = {
        "smic": "insee-smic-1970-2025.xml",
        "cpi_1980": "insee-cpi-base-1980-1970-1992.xml",
        "cpi_2015": "insee-cpi-base-2015-1990-2025.xml",
    }
    for name, payload in raw.items():
        (args.output_dir / raw_filenames[name]).write_bytes(payload)

    smic = parse_sdmx_observations(raw["smic"])
    cpi_old = parse_sdmx_observations(raw["cpi_1980"])
    cpi_new = parse_sdmx_observations(raw["cpi_2015"])
    cpi, factor = link_cpi_series(cpi_old, cpi_new)
    require_months(smic, START_YEAR, END_YEAR, "SMIC")
    require_months(cpi, START_YEAR, END_YEAR, "CPI")

    monthly_rows = []
    for period in sorted(smic):
        monthly_rows.append({
            "period": period,
            "smic_hourly_gross_eur": f"{smic[period]:.6f}",
            "ipc_base_2015_100": f"{cpi[period]:.6f}",
            "source_smic_idbank": SMIC_ID,
            "source_cpi_idbanks": f"{CPI_1980_ID}+{CPI_2015_ID}",
        })
    write_csv(args.output_dir / "smic-cpi-monthly-1970-2025.csv", monthly_rows)
    annual = annual_reconstruction(smic, cpi)
    write_csv(args.output_dir / "smic-real-purchasing-power-1970-2025.csv", annual)

    manifest = {
        "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
        "series": {
            "smic": {"idbank": SMIC_ID, "url": SOURCE_URLS["smic"], "observations": len(smic)},
            "cpi_base_1980": {"idbank": CPI_1980_ID, "url": SOURCE_URLS["cpi_1980"], "observations": len(cpi_old)},
            "cpi_base_2015": {"idbank": CPI_2015_ID, "url": SOURCE_URLS["cpi_2015"], "observations": len(cpi_new)},
        },
        "linked_cpi_observations": len(cpi),
        "cpi_link_factor_1980_to_2015": f"{factor:.12f}",
        "cpi_link_method": "geometric mean of monthly base-2015/base-1980 ratios over 1990-01 to 1992-12",
        "annual_method": "mean(monthly SMIC) / mean(monthly CPI); do not average monthly ratios",
        "raw_sha256": {raw_filenames[name]: hashlib.sha256(payload).hexdigest() for name, payload in raw.items()},
    }
    (args.output_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    print(f"SMIC observations: {len(smic)}; CPI observations used: {len(cpi)}")
    print(f"CPI base-link factor (1980 -> 2015): {factor:.12f}")
    print(f"Annual rows: {len(annual)}; first year: {annual[0]}; last year: {annual[-1]}")
    print(f"Artifacts written to {args.output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
