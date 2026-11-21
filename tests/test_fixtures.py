import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class FixtureTests(unittest.TestCase):
    def test_synthetic_records_match_documented_envelope(self):
        path = ROOT / 'fixtures' / 'records.json'
        data = json.loads(path.read_text(encoding='utf-8'))
        self.assertEqual(data['dataset'], 'argument')
        self.assertIsInstance(data['records'], list)
        self.assertGreaterEqual(len(data['records']), 3)
        identifiers = [row['id'] for row in data['records']]
        self.assertEqual(len(identifiers), len(set(identifiers)))
        self.assertTrue(all(isinstance(row, dict) for row in data['records']))

    def test_claim_evidence_counterclaim_and_next_round_are_linked(self):
        data = json.loads((ROOT / 'fixtures' / 'records.json').read_text(encoding='utf-8'))
        claims = {row['id'] for row in data['records'] if row['kind'] == 'claim'}
        evidence = [row for row in data['records'] if row['kind'] == 'evidence-link']
        counterclaims = {row['id'] for row in data['records'] if row['kind'] == 'counterclaim'}
        self.assertTrue(all(row['claim'] in claims for row in evidence))
        responses = [row for row in data['records'] if row['kind'] == 'response']
        self.assertTrue(all(row['counterclaim'] in counterclaims for row in responses))
        self.assertTrue(any(row['kind'] == 'next-round-plan' for row in data['records']))

if __name__ == '__main__':
    unittest.main()
