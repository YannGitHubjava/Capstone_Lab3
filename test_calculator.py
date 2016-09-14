from unittest import TestCase
from calculator_Operator import *

class TestCalculator(TestCase):
    # for testing purposes, we want to verify the calculator object

    def test_addition(self):
        # verify integer math works
        self.assertTrue(addition(4,5)==9)
        # verify float math works - call 7 places close enough
        self.assertAlmostEqual(addition(4.7,3.3),8.0,delta=.000001)
        # verify it doesn't concatenate strings
        self.assertIsNone(addition("alpah","beta"))

    def test_substraction(self):
        # verify integer math works
        self.assertTrue(substraction(4, 5) == -1)
        # verify float math works - call 7 places close enough
        self.assertAlmostEqual(substraction(4.7, 3.3), 1.4, delta=.000001)
        # verify it doesn't concatenate strings
        self.assertIsNone(substraction("alpah", "beta"))

# TODO build these two test cases
    def test_multiply(self):
        self.fail()

    def test_divid(self):
        self.fail()
