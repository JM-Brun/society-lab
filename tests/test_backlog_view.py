import unittest
from scripts.report.generate_backlog_view import build_rows, render_markdown
class BacklogViewTests(unittest.TestCase):
    def setUp(self):
        self.mapping={"issues":[{"issue":7,"kind":"research","dossier_ids":["D1"],"depends_on":[8]},{"issue":8,"kind":"meta","dossier_ids":[],"depends_on":[]}]}
        self.dossiers={"dossiers":[{"id":"D1","title":"Dossier test","domain_ids":["DOMAIN-A","DOMAIN-B"]}]}
        self.issues=[{"number":7,"title":"Sujet","html_url":"https://example.test/7","labels":[{"name":"priority:high"},{"name":"research"}]},{"number":8,"title":"Gouvernance","html_url":"https://example.test/8","labels":[{"name":"priority:medium"},{"name":"meta"},{"name":"documentation"}]},{"number":9,"title":"Non mappée","html_url":"https://example.test/9","labels":[{"name":"priority:low"}]}]
    def test_domains_derive_from_linked_dossiers(self):
        row=next(item for item in build_rows(self.issues,self.mapping,self.dossiers) if item["number"]==7)
        self.assertEqual(row["domain_ids"],["DOMAIN-A","DOMAIN-B"])
    def test_unmapped_issue_is_not_guessed(self):
        row=next(item for item in build_rows(self.issues,self.mapping,self.dossiers) if item["number"]==9)
        self.assertEqual(row["kind"],"unmapped"); self.assertEqual(row["domain_ids"],[]); self.assertFalse(row["mapping_valid"])
    def test_invalid_priority_is_flagged(self):
        issue=dict(self.issues[0],labels=[{"name":"priority:high"},{"name":"priority:low"}])
        row=build_rows([issue],self.mapping,self.dossiers)[0]
        self.assertFalse(row["priority_valid"]); self.assertEqual(row["priority"],"unclassified")
    def test_rendering_includes_domain_and_dependencies(self):
        output=render_markdown(build_rows(self.issues,self.mapping,self.dossiers),"2026-11-18T12:00+00:00")
        self.assertIn("DOMAIN-A, DOMAIN-B",output); self.assertIn("#8",output); self.assertIn("À qualifier",output)
if __name__=="__main__": unittest.main()