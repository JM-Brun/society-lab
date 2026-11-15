import csv
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"/"analysis"))
from audit_smic_real_purchasing_power_2001_2008_tef2010 import audit_rows
class TestTef2010SmicPower(unittest.TestCase):
    def setUp(self):
        with (ROOT/"data"/"smic-real-purchasing-power-2001-2008-tef2010.csv").open(encoding="utf-8",newline="") as f:
            self.rows=list(csv.DictReader(f))
    def test_coverage(self):
        self.assertEqual(audit_rows(self.rows),8)
    def test_rejects_missing_year(self):
        with self.assertRaisesRegex(ValueError,"unique, ordered"):
            audit_rows(self.rows[:-1])
    def test_requires_source(self):
        rows=[dict(x) for x in self.rows]
        rows[0]["source_url"]=""
        with self.assertRaisesRegex(ValueError,"traceability"):
            audit_rows(rows)
if __name__=="__main__":
    unittest.main()
