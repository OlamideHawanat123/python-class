import unittest
import functionpractice

class TestCubeFunction(unittest.TestCase):
	
	def test_that_cube_function_exists(self):
		functionpractice.get_cube(3)

	def test_that_cube_function_return_correct_value(self):
		actual = functionpractice.get_cube(3)
		result = 27
		self.assertEqual(actual, result)
		actual = functionpractice.get_cube(5)
		result = 125
		self.assertEqual(actual, result)

	def test_that_cube_function_return_negative_value_with_negative_parameter(self):
		actual = functionpractice.get_cube(-3)
		result = -27
		self.assertEqual(actual, result)

	def test_that_cube_function_return_invalid_data_with_invalid_input(self):
		actual = functionpractice.get_cube('a')
		result = 'invalid data'
		self.assertEqual(actual, result)

	def test_that_cube_function_return_correct_value_with_decimal_value(self):
		actual = functionpractice.get_cube(3.25)
		result = 34.328
		self.assertEqual(actual, result)

class TestExchangeRate(unittest.TestCase):

	def test_that_cube_function_exists(self):
		functionpractice.convert_dollar_to_naira(500)

	def test_that_dollar_can_be_converted_to_naira_using_exchange_rate(self):
		actual = functionpractice.convert_dollar_to_naira(100)
		result = 155000
		self.assertEqual(actual, result)
		
	def test_that_conversion_rate_return_invalid_data_when_an_invalid_amount_is_entered(self):
		actual = functionpractice.convert_dollar_to_naira(-4)
		result = 'invalid data'
		self.assertEqual(actual, result)

	def test_that_conversion_rate_return_invalid_data_with_invalid_input(self):
		actual = functionpractice.convert_dollar_to_naira('a')
		result = 'invalid data'
		self.assertEqual(actual, result)

	def test_that_decimal_number_is_valid_during_conversion(self):
		actual = functionpractice.convert_dollar_to_naira(5.4)
		result = 8370
		self.assertEqual(actual, result)

	def test_that_negative_decimal_is_invalid_during_conversion(self):
		actual = functionpractice.convert_dollar_to_naira(-9.6)
		result = 'invalid data'
		self.assertEqual(actual, result)

	def test_that_string_and_int_data_type_is_not_valid_during_conversion(self):
		actual = functionpractice.convert_dollar_to_naira('a3')
		result = 'invalid data'
		self.assertEqual(actual, result)

	