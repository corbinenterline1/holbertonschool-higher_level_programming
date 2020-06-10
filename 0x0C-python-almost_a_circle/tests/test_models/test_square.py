#!/usr/bin/python3
"""0x0C - Almost a circle.
Square test module."""
import unittest
import pep8
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests for square class."""

    def test_docs_and_pep(self):
        """tests for docstrings & pep8 adherance."""
        self.assertIsNotNone(Rectangle.__doc__)
        self.assertIsNotNone(("models.rectangle").__doc__)
        peppy = pep8.StyleGuide(quiet=True)
        peppa = peppy.check_files(['models/square.py'])
        self.assertEqual(peppa.total_errors, 0)


if __name__ == '__main__':
    unittest.main()
