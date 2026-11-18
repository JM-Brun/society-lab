import unittest
from unittest.mock import patch
from urllib.error import URLError

from scripts.validate import sync_issue_labels
from scripts.validate.sync_issue_labels import canonical_labels, compare_labels


class CanonicalLabelSyncTests(unittest.TestCase):
    def setUp(self):
        self.expected = {
            "internal": {"name": "internal", "color": "ededed", "description": "Travail interne"},
            "priority:high": {"name": "priority:high", "color": "b60205", "description": "Urgent"},
        }

    def test_exact_match_has_no_drift(self):
        self.assertEqual(compare_labels(self.expected, dict(self.expected)), [])

    def test_missing_label_is_reported(self):
        drift = compare_labels(self.expected, {"internal": self.expected["internal"]})
        self.assertEqual([(item.name, item.kind) for item in drift], [("priority:high", "missing")])

    def test_color_and_description_divergence_is_reported(self):
        actual = {"internal": {"color": "ededed", "description": None}}
        drift = compare_labels({"internal": self.expected["internal"]}, actual)
        self.assertEqual(len(drift), 1)
        self.assertEqual(drift[0].kind, "different")
        self.assertIn("description", drift[0].detail)

    def test_unmanaged_label_is_preserved_and_reported(self):
        actual = {
            **self.expected,
            "legacy-label": {"color": "ffffff", "description": "Historical"},
        }
        drift = compare_labels(self.expected, actual)
        self.assertEqual([(item.name, item.kind) for item in drift], [("legacy-label", "unmanaged")])

    def test_canonical_flattening_keeps_metadata(self):
        policy = {"axes": {"scope": {"internal": {"color": "EDEDED", "description": "Travail"}}}}
        self.assertEqual(canonical_labels(policy)["internal"]["color"], "ededed")


    def test_request_retries_transient_network_error(self):
        class Response:
            headers = {}
            def __enter__(self): return self
            def __exit__(self, *_args): return False
            def read(self): return b'{"ok": true}'

        with patch.object(sync_issue_labels, "TOKEN", "test-token"), \
             patch.object(sync_issue_labels.urllib.request, "urlopen", side_effect=[URLError("temporary"), Response()]) as urlopen, \
             patch.object(sync_issue_labels.time, "sleep") as sleep:
            payload, _link = sync_issue_labels.request("https://api.github.com/test")
        self.assertEqual(payload, {"ok": True})
        self.assertEqual(urlopen.call_count, 2)
        sleep.assert_called_once_with(1)

if __name__ == "__main__":
    unittest.main()
