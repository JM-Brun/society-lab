import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "audit"))

from report_graph_reconciliation import classify_exceptions, compare_snapshots, render_markdown


def edge(relation, source, target):
    return {"type": relation, "from": source, "to": target}


class GraphReconciliationTests(unittest.TestCase):
    def test_documentary_rules_compare_only_their_own_endpoints_and_direction(self):
        registries = {
            "DOSSIER": [
                {"id": "DOSSIER-A", "claim_ids": ["CLAIM-Z", "CLAIM-A"], "concept_ids": ["CONCEPT-A"]},
            ],
            "STUDY": [{"id": "STUDY-A", "dataset_ids": ["DATASET-A"]}],
        }
        edges = [
            edge("REL-INCLUDES", "DOSSIER-A", "CONCEPT-A"),
            edge("REL-INCLUDES", "DOSSIER-A", "CLAIM-B"),
            edge("REL-INCLUDES", "DOMAIN-A", "CLAIM-A"),
            edge("REL-INCLUDES", "CLAIM-Z", "DOSSIER-A"),
            edge("REL-ABOUT", "DOSSIER-A", "CLAIM-A"),
            edge("REL-USES", "DOSSIER-A", "DATASET-A"),
            edge("REL-USES", "STUDY-A", "CONCEPT-A"),
        ]
        by_field = {row["field"]: row for row in compare_snapshots((registries, edges))}
        self.assertEqual(by_field["claim_ids"]["registry_only"], [
            ("DOSSIER-A", "CLAIM-A"), ("DOSSIER-A", "CLAIM-Z"),
        ])
        self.assertEqual(by_field["claim_ids"]["graph_only"], [("DOSSIER-A", "CLAIM-B")])
        self.assertEqual(by_field["concept_ids"]["matching_count"], 1)
        self.assertEqual(by_field["dataset_ids"]["registry_only"], [("STUDY-A", "DATASET-A")])
        self.assertEqual(by_field["dataset_ids"]["graph_only"], [])
        self.assertNotIn("changes", by_field["dataset_ids"])

    def test_delta_uses_pair_identity_even_when_totals_stay_the_same(self):
        registries = {
            "DOSSIER": [{"id": "DOSSIER-A", "claim_ids": ["CLAIM-A", "CLAIM-B"]}],
            "STUDY": [],
        }
        before = [edge("REL-INCLUDES", "DOSSIER-A", "CLAIM-A")]
        after = [edge("REL-INCLUDES", "DOSSIER-A", "CLAIM-B")]
        rows = compare_snapshots((registries, after), (registries, before))
        claim = next(row for row in rows if row["field"] == "claim_ids")
        self.assertEqual(claim["changes"], {
            "registry_only": {"added": [("DOSSIER-A", "CLAIM-A")], "resolved": [("DOSSIER-A", "CLAIM-B")]},
            "graph_only": {"added": [], "resolved": []},
        })
        summary = render_markdown({"revision": "after", "base_revision": "before", "rules": rows})
        self.assertIn("**Apparus** 1 · **Disparus** 1", summary)
        self.assertIn("`DOSSIER-A` → `CLAIM-B`", summary)


    def test_exception_matches_only_the_exact_field_side_and_pair(self):
        registries = {
            "DOSSIER": [{"id": "DOSSIER-A", "claim_ids": ["CLAIM-A", "CLAIM-B"]}],
            "STUDY": [],
        }
        rules = compare_snapshots((registries, []))
        documented = {
            "field": "claim_ids", "side": "registry_only", "source": "DOSSIER-A",
            "target": "CLAIM-A", "reason": "Documentary choice.",
        }
        inactive = {**documented, "side": "graph_only"}
        classification = classify_exceptions(rules, [inactive, documented])
        self.assertEqual(classification, {
            "unreviewed_count": 1,
            "documented_exceptions": [documented],
            "inactive_exceptions": [inactive],
        })
        claim_rule = next(rule for rule in rules if rule["field"] == "claim_ids")
        self.assertEqual(len(claim_rule["registry_only"]), 2)
        summary = render_markdown({
            "revision": "after", "base_revision": None, "rules": rules, **classification,
        })
        self.assertIn("**À examiner** 1 · **Écarts documentés** 1", summary)
        self.assertIn("### Décisions à réexaminer", summary)

    def test_invalid_and_duplicate_exceptions_are_rejected(self):
        entry = {
            "field": "claim_ids", "side": "graph_only", "source": "DOSSIER-A",
            "target": "CLAIM-A", "reason": "Documentary choice.",
        }
        for invalid in (
            {**entry, "field": "unknown"},
            {**entry, "side": "both"},
            {**entry, "target": "STUDY-A"},
            {**entry, "reason": " "},
        ):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                classify_exceptions([], [invalid])
        with self.assertRaisesRegex(ValueError, "duplicate"):
            classify_exceptions([], [entry, {**entry, "reason": "Different reason."}])


if __name__ == "__main__":
    unittest.main()
