import unittest 
from ExpressTracker import *

class TestThatExpenseTrackerExists(unittest.TestCase):
	def test_that_expense_tracker_can_sum_amount(self):
		actual = calculate_total({amount: 2500,amount: 2500})
		result = 18
		self.assertEqual(actual, result)		
	
	
		
