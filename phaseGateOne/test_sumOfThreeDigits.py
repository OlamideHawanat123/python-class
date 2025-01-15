import unittest
import sumOfThreeDigitFunction

class sum_of_integers(unittest.TestCase):

	def test_that_sum_of_digits_exists(self):
		sumOfThreeDigitFunction.sum_digits(395)

	def test_that_sum_of_digits_returns_invalid_data_when_a_string_data_type_is_entered(self):
		actual = sumOfThreeDigitFunction.sum_digits('try')
		result = 'invalid data'
		self.assertEqual(actual, result)

	def test_that_sum_of_digits_returns_invalid_data_when_a_string_and_int_data_type_is_entered(self):
		actual = sumOfThreeDigitFunction.sum_digits('a34')
		result = 'invalid data'
		self.assertEqual(actual, result)

	