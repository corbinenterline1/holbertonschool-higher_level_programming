#!/usr/bin/python3
"""0x0C - Almost a circle.
Base class testing module"""
import unittest
from models.base import Base
import pep8


class TestBase(unittest.TestCase):
    """Base tests."""

    def test_docs_and_pep(self):
        """Tests for proper docstrings and PEP8 formatting."""
        self.assertIsNotNone(Base.__doc__)
        self.assertIsNotNone(("models.base").__doc__)
        self.assertIsNotNone(Base.__init__.__doc__)
        self.assertIsNotNone(Base.to_json_string.__doc__)
        self.assertIsNotNone(Base.save_to_file.__doc__)
        self.assertIsNotNone(Base.from_json_string.__doc__)
        self.assertIsNotNone(Base.create.__doc__)
        self.assertIsNotNone(Base.load_from_file.__doc__)
        peppy = pep8.StyleGuide(quiet=True)
        peppa = peppy.check_files(['models/base.py'])
        self.assertEqual(peppa.total_errors, 0)

    def test_creation(self):
        """Creates base class, confirms it exists. Checks its' id.
        Checks custom id, then id 2. Same 3 checks for each.
        Makes a couple bad attributes for later tests."""
        self.base1 = Base()
        self.assertIsNot(self.base1, None)
        self.assertIsInstance(self.base, Base)
        self.assertTrue(type(self.base) is Base)
        self.assertEqual(self.base1.id, 1)
        self.basemmb = Base(737)
        self.assertEqual(self.basemmb.id, 737)
        self.base2 = Base()
        self.assertEqual(self.base2.id, 2)
        self.baseneg = Base(-737)
        self.basebomb = Base("bomb")

if __name__ == '__main__':
    unittest.main()
