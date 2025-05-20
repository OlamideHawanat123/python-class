import unittest

from MrChineduTasks.array import find_median


class MyTestCase(unittest.TestCase):
    def test_find_median_returns_the_median_of_two_arrays(self):
        first_list = [1, 2, 4]
        second_list = [5, 6, 7, 8]

        self.assertEqual(5, find_median(first_list, second_list))



if __name__ == '__main__':
    unittest.main()
