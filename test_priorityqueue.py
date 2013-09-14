import unittest
from priorityqueue import PriorityQueue

class TestPriorityQueue(unittest.TestCase):

    def setUp(self):
        self.ppq = PriorityQueue(":memory:")

    def test_empty(self):
        result = self.ppq.is_empty()
        self.assertTrue(result)

    def test_order(self):
        self.ppq.push(10, "hello")
        self.ppq.push(1, "foo")
        self.ppq.push(30, "bar")
        self.ppq.push(5, "baz")

        self.assertEqual("bar", self.ppq.pop())
        self.assertEqual("hello", self.ppq.pop())
        self.assertEqual("baz", self.ppq.pop())
        self.assertEqual("foo", self.ppq.pop())

if __name__ == '__main__':
    unittest.main()
