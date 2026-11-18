import unittest

from scripts.validate.validate_issue_domain_map import validate_mapping


class IssueDomainMapTests(unittest.TestCase):
    def setUp(self):
        self.mapping = {
            "issues": [
                {"issue": 1, "kind": "research", "dossier_ids": ["D1"], "depends_on": []},
                {"issue": 2, "kind": "meta", "dossier_ids": [], "depends_on": [1]},
            ]
        }
        self.dossiers = {"dossiers": [{"id": "D1", "domain_ids": ["DOMAIN-A"]}]}
        self.taxonomy = {"domains": [{"id": "DOMAIN-A"}]}

    def test_valid_explicit_mapping(self):
        self.assertEqual(validate_mapping(self.mapping, self.dossiers, self.taxonomy), [])

    def test_unknown_dossier_and_domain_are_reported(self):
        dossiers = {"dossiers": [{"id": "D1", "domain_ids": ["DOMAIN-MISSING"]}]}
        errors = validate_mapping(self.mapping, dossiers, self.taxonomy)
        self.assertTrue(any("unknown domain" in error for error in errors))

    def test_unmapped_dependency_is_reported(self):
        mapping = {"issues": [{"issue": 1, "kind": "meta", "dossier_ids": [], "depends_on": [9]}]}
        errors = validate_mapping(mapping, self.dossiers, self.taxonomy)
        self.assertTrue(any("no explicit mapping" in error for error in errors))

    def test_meta_cannot_claim_scientific_dossier(self):
        mapping = {"issues": [{"issue": 1, "kind": "meta", "dossier_ids": ["D1"], "depends_on": []}]}
        errors = validate_mapping(mapping, self.dossiers, self.taxonomy)
        self.assertTrue(any("must not invent" in error for error in errors))

    def test_duplicate_issue_number_is_reported(self):
        mapping = {"issues": [
            {"issue": 1, "kind": "meta", "dossier_ids": [], "depends_on": []},
            {"issue": 1, "kind": "meta", "dossier_ids": [], "depends_on": []},
        ]}
        errors = validate_mapping(mapping, self.dossiers, self.taxonomy)
        self.assertTrue(any("must be unique" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
