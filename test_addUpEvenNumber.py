import unittest
from addUpEvenNumber import addition

class TestOfEvenNumbers(unittest.TestCase):

	def test_that_addition_only_add_even_number(self):
		actual = addition([1, 2, 3, 4, 5, 6])
		result = 12
		self.assertEqual(actual, result)

	def test_that_addition_doesnt_add_odd_number(self):
		actual = addition([1, 3, 5, 7, 9])
		result = 0
		self.assertEqual(actual, result)

	def test_that_addition_doesnt_work_with_decimal(self):
		actual = addition([2.4, 6.2, 8.4])
		result = 0
		self.assertEqual(actual, result)

	