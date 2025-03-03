import unittest
from data_structures.linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()
        
    def test_insert_at_beginning(self):
        self.linked_list.insert_at_beginning(1)
        self.linked_list.insert_at_beginning(2)
        self.assertEqual(self.linked_list.display(), [2, 1])
        
    def test_insert_at_end(self):
        self.linked_list.insert_at_end(1)
        self.linked_list.insert_at_end(2)
        self.assertEqual(self.linked_list.display(), [1, 2])
        
    def test_delete(self):
        self.linked_list.insert_at_end(1)
        self.linked_list.insert_at_end(2)
        self.linked_list.insert_at_end(3)
        self.linked_list.delete(2)
        self.assertEqual(self.linked_list.display(), [1, 3])
        
    def test_search(self):
        self.linked_list.insert_at_end(1)
        self.linked_list.insert_at_end(2)
        self.assertTrue(self.linked_list.search(2))
        self.assertFalse(self.linked_list.search(3))

if __name__ == '__main__':
    unittest.main() 