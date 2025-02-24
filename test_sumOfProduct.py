import unittest 
from sumOfProduct import sum_of_product

class TestThatSumsProductOfElementsInAList(unittest.TestCase):
	def test_that_sum_of_product_exists(self):
		 sum_of_product([1, 2, 3, 4])

	def test_that_sum_of_product_sums_the_product_of_all_elements_in_the_list(self):
		actual = sum_of_product([1, 2, 3, 4])
		result = 30
		self.assertNotEqual(actual, result)


		