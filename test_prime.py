import unittest
from prime import return_prime

class TestThatChecksIfANumberIsPrime(unittest.TestCase):
	def test_that_prime_number_exists(self):
		return_prime(25)

	def test_that_prime_number_determines_if_a_number_is_prime(self):
		actual = return_prime(24)
		result = False
		self.assertEqual(actual, result)