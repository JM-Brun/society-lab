import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "audit"))

from audit_registry_coverage import TARGETS


class RegistryCoverageTargetTests(unittest.TestCase):
    def test_inventory_covers_every_validated_canonical_registry(self):
        targets = {registry: (collection, schema, prefix) for _, registry, collection, schema, prefix, _ in TARGETS}
        expected = {
            "sources/registry.yml": ("sources", "schemas/source.schema.json", "SOURCE"),
            "research/studies/registry.yml": ("studies", "schemas/study.schema.json", "STUDY"),
            "research/datasets/registry.yml": ("datasets", "schemas/dataset.schema.json", "DATASET"),
            "claims/registry.yml": ("claims", "schemas/claim.schema.json", "CLAIM"),
            "hypotheses/registry.yml": ("hypotheses", "schemas/hypothesis.schema.json", "HYPOTHESIS"),
            "forecasts/registry.yml": ("forecasts", "schemas/forecast.schema.json", "FORECAST"),
            "dossiers/registry.yml": ("dossiers", "schemas/dossier.schema.json", "DOSSIER"),
            "knowledge/concepts/registry.yml": ("concepts", "schemas/concept.schema.json", "CONCEPT"),
            "knowledge/mechanisms/registry.yml": ("mechanisms", "schemas/mechanism.schema.json", "MECHANISM"),
        }
        self.assertEqual(targets, expected)


if __name__ == "__main__":
    unittest.main()
