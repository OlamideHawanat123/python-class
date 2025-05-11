import unittest
import normal_number

class TestPalindrome(unittest.TestCase):

	def test_that_random_determines_a_palindrome(self):
		actual = 'False'
		result = random.palindrome("4567776")
		self.assertEqual(actual,result)