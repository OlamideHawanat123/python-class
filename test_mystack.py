import unittest
from mystack import Stack


class MyTestCase(unittest.TestCase):
    def test_that_my_stack_adds_item_to_stack(self):
        stack1 = mystack.Stack
        self.assertEqual(len(stack1.stack), 0)
        stack1.push(1)
        self.assertEqual(len(stack1.stack), 1)
        stack1.push(2)
        self.assertEqual(len(stack1.stack), 2)

if __name__ == '__main__':
    unittest.main()
