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
