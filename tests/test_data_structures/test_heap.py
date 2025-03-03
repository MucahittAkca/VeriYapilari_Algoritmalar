import unittest
from data_structures.heap import MinHeap

class TestMinHeap(unittest.TestCase):
    def setUp(self):
        self.heap = MinHeap()
        
    def test_insert_and_extract(self):
        self.heap.insert(5)
        self.heap.insert(3)
        self.heap.insert(7)
        self.heap.insert(1)
        
        self.assertEqual(self.heap.extract_min(), 1)
        self.assertEqual(self.heap.extract_min(), 3)
        self.assertEqual(self.heap.extract_min(), 5)
        self.assertEqual(self.heap.extract_min(), 7)
        self.assertIsNone(self.heap.extract_min())
        
    def test_heapify_up(self):
        elements = [5, 3, 7, 1]
        for element in elements:
            self.heap.insert(element)
            
        # En küçük eleman her zaman kök olmalı
        self.assertEqual(self.heap.heap[0], min(elements))
        
    def test_heapify_down(self):
        self.heap.heap = [5, 3, 7, 1]  # Geçersiz heap yapısı
        self.heap._heapify_down(0)  # Düzeltme
        self.assertEqual(self.heap.heap[0], 1)  # En küçük eleman köke taşınmalı

if __name__ == '__main__':
    unittest.main() 