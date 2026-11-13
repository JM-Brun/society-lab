#!/usr/bin/env python3
"""Cas-types transparents pour comparer des hausses du SMIC avec OpenFisca-France.

Les résultats sont des microsimulations statiques de cas-types, pas des prévisions
d'emploi ni des estimations représentatives de la population.
"""
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from typing import Any

REFERENCE_YEAR = 2026
REFERENCE_MONTHLY_GROSS_SMIC = 1867.02  # France hors Mayotte, depuis le 1er juin 2026
MONTHS = [f"{REFERENCE_YEAR}-{month:02d}" for month in range(1, 13)]


@dataclass(frozen=True)
class Person:
    identifier: str
    role: str
    wage_share: float = 0.0


@dataclass(frozen=True)
class HouseholdCase:
    identifier: str
    label: str
    adults: tuple[Person, ...]
    children: int = 0


CASES = (
    HouseholdCase("single_full_time", "Personne seule, temps plein au SMIC",
                  (Person("adult_1", "reference", 1.0),)),
    HouseholdCase("single_parent_part_time", "Parent isolé, temps partiel à 80 %",
                  (Person("adult_1", "reference", 0.8),), children=1),
    HouseholdCase("couple_one_low_wage", "Couple, un salarié au SMIC et un à 80 % du SMIC",
                  (Person("adult_1", "reference", 1.0),
                   Person("adult_2", "spouse", 0.8)), children=1),
    HouseholdCase("couple_two_smic", "Couple, deux salariés à temps plein au SMIC",
                  (Person("adult_1", "reference", 1.0),
                   Person("adult_2", "spouse", 1.0))),
)


def build_situation(case: HouseholdCase, gross_monthly_smic: float,
                    uplift: float) -> dict[str, Any]:
    """Construit une situation OpenFisca complète pour un ménage simple."""
    if gross_monthly_smic <= 0:
        raise ValueError("Le SMIC mensuel brut doit être strictement positif.")
    if uplift < -1:
        raise ValueError("La variation de salaire ne peut pas être inférieure à -100 %.")

    individuals: dict[str, dict[str, Any]] = {}
    adults = [person.identifier for person in case.adults]
    children = [f"child_{index + 1}" for index in range(case.children)]

    for person in case.adults:
        monthly_gross = gross_monthly_smic * person.wage_share * (1 + uplift)
        individuals[person.identifier] = {
            "salaire_de_base": {month: round(monthly_gross, 2) for month in MONTHS}
        }
    for child in children:
        individuals[child] = {}

    household: dict[str, Any] = {
        "personne_de_reference": [case.adults[0].identifier],
        "enfants": children,
    }
    family: dict[str, Any] = {
        "parents": adults,
        "enfants": children,
    }
    tax_household: dict[str, Any] = {
        "declarants": adults,
        "personnes_a_charge": children,
    }
    if len(adults) > 1:
        household["conjoint"] = [case.adults[1].identifier]

    return {
        "individus": individuals,
        "menages": {"household_1": household},
        "familles": {"family_1": family},
        "foyers_fiscaux": {"tax_household_1": tax_household},
    }


def run_case(case: HouseholdCase, gross_monthly_smic: float,
             uplift: float) -> dict[str, Any]:
    """Exécute un cas avec la version installée d'OpenFisca-France."""
    try:
        from openfisca_core.simulation_builder import SimulationBuilder
        from openfisca_france import FranceTaxBenefitSystem
    except ImportError as error:
        raise RuntimeError(
            "Dépendances absentes. Installer avec : "
            "python -m pip install openfisca-france"
        ) from error

    tax_benefit_system = FranceTaxBenefitSystem()
    simulation = SimulationBuilder().build_from_dict(
        tax_benefit_system,
        build_situation(case, gross_monthly_smic, uplift),
    )
    disposable_income = float(simulation.calculate("revenu_disponible", str(REFERENCE_YEAR))[0])
    return {
        "case": case.identifier,
        "label": case.label,
        "uplift_percent": round(uplift * 100, 2),
        "gross_monthly_smic_eur": gross_monthly_smic,
        "disposable_income_annual_eur": round(disposable_income, 2),
        "disposable_income_monthly_equivalent_eur": round(disposable_income / 12, 2),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gross-monthly-smic", type=float,
                        default=REFERENCE_MONTHLY_GROSS_SMIC,
                        help="SMIC mensuel brut de référence (défaut : 1 867,02 €).")
    parser.add_argument("--uplifts", type=float, nargs="+", default=[0, 1, 3, 5],
                        help="Hausses hypothétiques en pourcentage, ex. 0 1 3 5.")
    args = parser.parse_args()

    results = []
    for case in CASES:
        for uplift_percent in args.uplifts:
            results.append(run_case(case, args.gross_monthly_smic, uplift_percent / 100))
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
