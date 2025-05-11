import unittest
from MyPythonCollections import mystack

class MyTestCase(unittest.TestCase):
    stack = mystack.Stack
    def test_that_is_empty_returns_true_if_stack_is_empty(self):
        self.assertFalse(mystack.is_empty())  # add assertion here


if __name__ == '__main__':
    unittest.main()
