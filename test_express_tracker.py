import unittest 
from ExpressTracker import *

class TestThatExpenseTrackerExists(unittest.TestCase):
	def test_that_expense_tracker_can_sum_amount(self):
		actual = calculate_total(15, 3)
		result = 18
		self.assertEqual(actual, result)		
	
	def test_that_date_is_valid(self):
		self.assertTrue(is_valid_date("2025-12-01"))

		
