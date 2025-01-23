import unittest
from number_above import number_above_seventy_Five

class TestForNumberAboveSeventyfiveAndBelowHundred(unittest.TestCase):

	def test_that_number_above_seventyfive_and_below_hundred_exist(self):
		actual = number_above_seventy_Five([75, 100])
		result = [75, 100]
		self.assertEqual(actual, result)


	def test_that_number_above_seventy_five_only_returns_number_above_seventyfive_and_below_hundred(self):
		actual = number_above_seventy_Five([34, 100, 76, 23])
		result = [100, 76]
		self.assertEqual(actual, result)

	def test_that_number_below_seventy_five_returns_empty_list(self):
		actual = number_above_seventy_Five([1, 2, 45])
		result = []
		self.assertEqual(actual, result)

	def test_that_number_above_hundred_returns_empty_list(self):
		actual = number_above_seventy_Five([500, 450, 101])
		result = [] 
		self.assertEqual(actual, result)

	


	


