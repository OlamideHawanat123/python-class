import unittest
from TDDSnacks import myAc


class MyTestCase(unittest.TestCase):
    def test_that_my_ac_turns_on_when_turned_on(self):
        self.assertFalse(myAc.is_on())
        myAc.turn_on()
        self.assertTrue(myAc.is_on())


if __name__ == '__main__':
    unittest.main()
