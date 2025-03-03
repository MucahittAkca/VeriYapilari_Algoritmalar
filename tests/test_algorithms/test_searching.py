import unittest
from algorithms.searching.binary_search import binary_search
from algorithms.searching.linear_search import linear_search

class TestSearching(unittest.TestCase):
    def setUp(self):
        self.sorted_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.unsorted_arr = [5, 2, 8, 1, 9, 3, 7, 4, 6, 10]
        
    def test_binary_search_found(self):
        self.assertEqual(binary_search(self.sorted_arr, 5), 4)
        self.assertEqual(binary_search(self.sorted_arr, 1), 0)
        self.assertEqual(binary_search(self.sorted_arr, 10), 9)
        
    def test_binary_search_not_found(self):
        self.assertEqual(binary_search(self.sorted_arr, 11), -1)
        self.assertEqual(binary_search(self.sorted_arr, 0), -1)
        
    def test_linear_search_found(self):
        self.assertEqual(linear_search(self.unsorted_arr, 5), 0)
        self.assertEqual(linear_search(self.unsorted_arr, 2), 1)
        self.assertEqual(linear_search(self.unsorted_arr, 10), 9)
        
    def test_linear_search_not_found(self):
        self.assertEqual(linear_search(self.unsorted_arr, 11), -1)
        self.assertEqual(linear_search(self.unsorted_arr, 0), -1)

if __name__ == '__main__':
    unittest.main() 