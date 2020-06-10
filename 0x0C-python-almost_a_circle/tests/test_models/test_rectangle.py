#!/usr/bin/python3
"""0x0C - Almost a circle.
Test module for rectangle."""
import unittest
from models.rectangle import Rectangle
import pep8

class TestRectangle(unittest.TestCase):
    """Rectangle tests"""

    def test_docs_and_pep8(self):
        """test docs and pep8"""
    self.assertIsNotNone(Rectangle.__doc__)
    self.assertIsNotNone(("models.rectangle").__doc__)
    peppy = pep8.StyleGuide(quiet=True)
    peppa = peppy.check_files(['models/rectangle.py'])
    self.assertEqual(peppa.total_errors, 0)


if __name__ == '__main__':
    unittest.main()
