""" unit tests for translator"""
import unittest

from translator import english_to_french, french_to_english

class TestMyModule(unittest.TestCase):
    """ Define Test Module Case."""

    def test_english_to_french(self):
        """ English to French Function."""
        self.assertNotEqual(english_to_french("None"), "")
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test_french_to_english(self):
        """ French to English Function."""
        self.assertNotEqual(french_to_english("None"), "")
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
