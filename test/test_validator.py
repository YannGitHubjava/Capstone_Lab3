# unit testing file for validation methods
from unittest import TestCase
from validator import *

class TestValidator(TestCase):

    def test_isNumeric(self):
        # test positive and negative integers
        self.assertTrue(isNumeric(1))
        self.assertTrue(isNumeric(-7052435844))
        # test positive and negative floats
        self.assertTrue(isNumeric(7.524))
        self.assertTrue(isNumeric(-7008523189.28158436))
        # test that strings return false
        self.assertFalse(isNumeric("string"))

    def test_is_whole_number(self):
        # check that whole numbers with no ranges pass, including large ones
        self.assertTrue(is_whole_number(7))
        self.assertTrue(is_whole_number(-3))
        self.assertTrue(is_whole_number(3679845))
        # check that valid ranges return true
        self.assertTrue(is_whole_number(3,range(0,5)))
        self.assertTrue(is_whole_number(-3, range(-10, 5)))
        # check that invalid ranges return false
        self.assertFalse(is_whole_number(-3,range(0,5)))
        self.assertFalse(is_whole_number(13, range(-10, 5)))
        # check that floats return false, including with both valid and invalid ranges
        self.assertFalse(is_whole_number(7.152))
        self.assertFalse(is_whole_number(-.3336))
        self.assertFalse(is_whole_number(-.13, range(-10, 5)))
        self.assertFalse(is_whole_number(13.333, range(-10, 5)))
        # and check that strings return false
        self.assertFalse(is_whole_number("string"))
        # and verify it can cope with stringlike numbers
        self.assertTrue(is_whole_number("7"))
        self.assertFalse(is_whole_number("7.5"))
        self.assertFalse(is_whole_number(".332432"))
        # assume that if people enter a period with no tail, they meant to enter a float:
        self.assertFalse(is_whole_number("3."))