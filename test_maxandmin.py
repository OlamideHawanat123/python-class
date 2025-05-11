import unittest
from maxandmin import maxAndMin

class MaximumAndMinimumInAList(unittest.TestCase):
	def test_that_max_and_min_can_return_highest_and_minimum_in_a_list(self):
		actual = maxAndMin([1, 2, 3, 4])
		result = [4, 1]
		self.assertEqual(actual, result)
	
		