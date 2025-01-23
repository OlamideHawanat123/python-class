import unittest
from common_number import common_number

class TestThatFindsCommonNumber(unittest.TestCase):
	def test_that_returns_common_number_in_a_list(self):
		actual = common_number([1, 2, 5][3, 1, 9])
		result = 1
		self.assertEqual(actual, result)

	def test_that_common_number_function_exists(self):
		common_number([1, 2, 5][3, 1, 9])
