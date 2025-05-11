import unittest
from datetime import datetime, timedelta
from menstrual_cycle import MenstrualCycle

class TestMenstrualCycle(unittest.TestCase):

    def setUp(self):
        self.start_date = datetime(2025, 4, 1)
        self.end_date = datetime(2025, 4, 5)
        self.cycle_length = 28
        self.cycle = MenstrualCycle(self.start_date, self.end_date, self.cycle_length)

    def test_get_ovulation_date(self):
        expected = self.end_date + timedelta(days=self.cycle_length // 2)
        self.assertEqual(self.cycle.get_ovulation_date(), expected)

    def test_get_safe_period_end_date(self):
        expected = self.end_date + timedelta(days=6)
        self.assertEqual(self.cycle.get_safe_period_end_date(), expected)

    def test_get_next_period_start_date(self):
        expected = self.start_date + timedelta(days=self.cycle_length)
        self.assertEqual(self.cycle.get_next_period_start_date(), expected)

    def test_get_start_date(self):
        self.assertEqual(self.cycle.get_start_date(), self.start_date)

    def test_get_end_date(self):
        self.assertEqual(self.cycle.get_end_date(), self.end_date)

    def test_get_fertile_window(self):
        ovulation = self.cycle.get_ovulation_date()
        expected_start = ovulation - timedelta(days=5)
        expected_end = ovulation + timedelta(days=1)
        self.assertEqual(self.cycle.get_fertile_window(), (expected_start, expected_end))


if __name__ == '__main__':
    unittest.main()
