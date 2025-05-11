import unittest
from phaseGateOne.PhaseGateApps.MenstrualApp import *


class MyTestCase(unittest.TestCase):
    my_object = MenstrualCycle("22/03/2025", "26/03/2025", 28, 24, 5)
    def test_that_menstrual_app_can_predict_the_starting_date_of_your_next_period(self):
        self.assertEqual(19-4-2025, my_object.next_flow_starting_date())  # add assertion here


if __name__ == '__main__':
    unittest.main()
