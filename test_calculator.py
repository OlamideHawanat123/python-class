import unittest
from Calculator import *

class TestThatCalculatorCanDoVarietiesOfThings(unittest.TestCase):
	def test_that_calculator_can_add_two_numbers(self):
		actual = addition(12, 4)
		result = 16
		self.assertEqual(actual, result)

	def test_that_addition_can_add_two_decimal_numbers(self):
		actual = addition(1.2, 4.5)
		result = 5.7
		self.assertEqual(actual, result)
	
	def test_that_addition_cannot_add_String(self):
		actual = addition('b', 'e')
		result = 'invalid data'
		self.assertEqual(actual, result)

	def test_that_calculator_can_subtract_a_number_from_another(self):
		actual = subtraction(12, 4)
		result = 8
		self.assertEqual(actual, result)