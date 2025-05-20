import unittest
from MyPythonCollections import mystack

class MyTestCase(unittest.TestCase):

    def test_that_stack_is_empty(self):
        self.assertTrue(mystack.is_empty())

    def test_that_push_adds_an_element_to_stack_and_stack_is_no_longer_empty(self):
        self.assertTrue(mystack.is_empty())
        mystack.push(23)
        self.assertFalse(mystack.is_empty())

    def test_that_pop_removes_the_last_element_in_the_stack(self):
        self.assertTrue(mystack.is_empty())
        mystack.push(23)

        self.assertFalse(mystack.is_empty())
        mystack.pop()
        self.assertTrue(mystack.is_empty())

    def test_that_peek_returns_the_last_element_that_was_pushed(self):
        mystack.push(23)
        mystack.push(1)
        mystack.push(5)
        self.assertEqual(5, mystack.peek())

    def test_that_peek_throws_an_exception_if_called_when_stack_is_empty(self):
        mystack.peek()
        with self.assertRaises(IndexError):
            raise IndexError("No element found")



if __name__ == '__main__':
    unittest.main()
