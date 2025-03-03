import unittest
from data_structures.binary_tree import BinaryTree

class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.tree = BinaryTree()
        
    def test_insert_and_search(self):
        self.tree.insert(5)
        self.tree.insert(3)
        self.tree.insert(7)
        
        self.assertIsNotNone(self.tree.search(5))
        self.assertIsNotNone(self.tree.search(3))
        self.assertIsNotNone(self.tree.search(7))
        self.assertIsNone(self.tree.search(10))
        
    def test_inorder_traversal(self):
        self.tree.insert(5)
        self.tree.insert(3)
        self.tree.insert(7)
        self.tree.insert(1)
        self.tree.insert(9)
        
        self.assertEqual(self.tree.inorder_traversal(), [1, 3, 5, 7, 9])

    def test_preorder_traversal(self):
        self.tree.insert(5)
        self.tree.insert(3)
        self.tree.insert(7)
        self.tree.insert(1)
        self.tree.insert(9)
        
        self.assertEqual(self.tree.preorder_traversal(), [5, 3, 1, 7, 9])

    def test_postorder_traversal(self):
        self.tree.insert(5)
        self.tree.insert(3)
        self.tree.insert(7)
        self.tree.insert(1)
        self.tree.insert(9)
        
        self.assertEqual(self.tree.postorder_traversal(), [1, 3, 9, 7, 5])

if __name__ == '__main__':
    unittest.main() 