import unittest
from data_structures.queue import Queue

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()
        
    def test_enqueue(self):
        self.queue.enqueue(1)
        self.assertEqual(self.queue.front(), 1)
        self.assertEqual(self.queue.size(), 1)
        
    def test_dequeue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.size(), 1)
        
    def test_empty_queue(self):
        with self.assertRaises(IndexError):
            self.queue.dequeue()
        with self.assertRaises(IndexError):
            self.queue.front()
            
    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(1)
        self.assertFalse(self.queue.is_empty())

if __name__ == '__main__':
    unittest.main() 