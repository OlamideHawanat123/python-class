import unittest 
from numberOfVowel import return_sum_of_vowel

class TestNumberOfVowel(unittest.TestCase):
	def test_that_number_of_vowel_returns_number_of_vowel_in_the_string(self):
		actual = return_sum_of_vowel("i am a boy")
		result = 4
		self.assertEqual(actual, result)

	def test_that_number_of_vowel_returns_zero_if_there_are_only_consonants_in_the_string(self):
		actual = return_sum_of_vowel("trll grll")
		result = 0
		self.assertEqual(actual, result)

	def test_that_number_of_number_of_vowel_exists(self):
		return_sum_of_vowel("i am a girl")
