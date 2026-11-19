import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BENCHMARK = ROOT / "scripts" / "audit" / "benchmark_validation_scale.py"


class ValidationScaleBenchmarkTests(unittest.TestCase):
    def test_full_validation_path_at_x1_x10_and_x100(self):
        completed = subprocess.run(
            [sys.executable, str(BENCHMARK), "--scales", "1", "10", "100"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=300,
        )
        report = json.loads(completed.stdout)
        results = report["results"]
        self.assertEqual([item["scale"] for item in results], [1, 10, 100])
        self.assertGreater(results[1]["records"], results[0]["records"])
        self.assertGreater(results[2]["records"], results[1]["records"])
        self.assertGreater(results[1]["edges"], results[0]["edges"])
        self.assertGreater(results[2]["edges"], results[1]["edges"])
        print("VALIDATION_SCALE_BENCHMARK=" + json.dumps(report, ensure_ascii=False))


if __name__ == "__main__":
    unittest.main()
