import csv
import io
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIELDS = {'intake': ['report', 'item', 'household', 'street', 'category', 'at'], 'recognition': ['id', 'left_item', 'right_item', 'action', 'target', 'signed_by', 'at'], 'disposition': ['id', 'item', 'basis', 'prior_item', 'at'], 'roster': ['cycle', 'object', 'item', 'street', 'category', 'basis', 'frozen_at'], 'draw_policy': ['cycle', 'street', 'category', 'slots', 'seed'], 'dispatch': ['cycle', 'object', 'basis', 'sent_at'], 'inspections': ['id', 'cycle', 'object', 'covered_item', 'evidence', 'finding', 'at']}


class DataContractTests(unittest.TestCase):
    def test_readable_source_tables(self):
        for name, fields in FIELDS.items():
            with self.subTest(table=name):
                text = (ROOT / 'data' / (name + '.csv')).read_text(encoding='utf-8')
                with io.StringIO(text, newline='') as stream:
                    reader = csv.reader(stream, strict=True)
                    self.assertEqual(next(reader), fields)
                    rows = list(reader)
                self.assertTrue(rows)
                self.assertTrue(all(len(row) == len(fields) for row in rows))
