from unittest import TestCase
from calculator_Operator import *


class TestCalculator(TestCase):
    # for testing purposes, we want to verify the calculator object
    # for this exercise, we are going to assume the Main() method will defend against non-numeric input.

    def test_addition(self):
        # verify integer math works
        self.assertTrue(Calculator(4,5).addition() == 9)
        # verify float math works - call 7 places close enough
        self.assertAlmostEqual(Calculator(4.7,3.3).addition(),8.0,delta=.000001)


    def test_substraction(self):
        # verify integer math works
        self.assertTrue(Calculator(4, 5).substraction() == -1)
        # verify float math works - call 7 places close enough
        self.assertAlmostEqual(Calculator(4.7, 3.3).substraction(), 1.4, delta=.000001)
        # verify it doesn't concatenate strings
        #self.assertIsNone(Calculator("alpha", "beta").substraction())

    def test_multiply(self):
        # verify integer math works
        self.assertTrue(Calculator(4,5).multiply() == 20)
        # verify float math works - call 4 places close enough
        self.assertAlmostEqual(Calculator(4.7, 3.3).multiply(), 15.51, delta=.0001)

    def test_divid(self):
        # verify integer math works
        self.assertTrue(Calculator(4,5).divide() == 0.8)
        # verify float math works - call 4 places close enough
        self.assertAlmostEqual(Calculator(4.7, 3.3).divide(), 1.4242, delta=.0001)


