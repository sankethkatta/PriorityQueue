import unittest
from priorityqueue import PriorityQueue, Queue, Stack

class TestPriorityQueue(unittest.TestCase):

    def setUp(self):
        self.ppq = PriorityQueue(":memory:")

    def test_empty(self):
        result = self.ppq.is_empty()
        self.assertTrue(result)

    def test_order(self):
        self.assertEqual("hello", self.ppq.push(10, "hello"))
        self.ppq.push(1, "foo")
        self.ppq.push(30, "bar")
        self.ppq.push(5, "baz")

        self.assertEqual("bar", self.ppq.pop())
        self.assertEqual("hello", self.ppq.pop())
        self.assertEqual("baz", self.ppq.pop())
        self.assertEqual("foo", self.ppq.pop())

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.q = Queue(":memory:")

    def test_order(self):
        self.assertEqual("hello", self.q.push("hello"))
        self.q.push("foo")
        self.q.push("bar")
        self.q.push("baz")

        self.assertEqual("hello", self.q.pop())
        self.assertEqual("foo", self.q.pop())
        self.assertEqual("bar", self.q.pop())
        self.assertEqual("baz", self.q.pop())

class TestStack(unittest.TestCase):

    def setUp(self):
        self.q = Stack(":memory:")

    def test_order(self):
        self.assertEqual("hello", self.q.push("hello"))
        self.q.push("foo")
        self.q.push("bar")
        self.q.push("baz")

        self.assertEqual("baz", self.q.pop())
        self.assertEqual("bar", self.q.pop())
        self.assertEqual("foo", self.q.pop())
        self.assertEqual("hello", self.q.pop())

if __name__ == '__main__':
    unittest.main()
