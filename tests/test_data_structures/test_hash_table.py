import unittest
from data_structures.hash_table import HashTable

class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.hash_table = HashTable()
        
    def test_insert_and_get(self):
        self.hash_table.insert("name", "Alice")
        self.hash_table.insert("age", 25)
        
        self.assertEqual(self.hash_table.get("name"), "Alice")
        self.assertEqual(self.hash_table.get("age"), 25)
        
    def test_key_not_found(self):
        with self.assertRaises(KeyError):
            self.hash_table.get("nonexistent")
            
    def test_update_existing_key(self):
        self.hash_table.insert("name", "Alice")
        self.hash_table.insert("name", "Bob")
        
        self.assertEqual(self.hash_table.get("name"), "Bob")
        
    def test_remove(self):
        self.hash_table.insert("name", "Alice")
        self.hash_table.remove("name")
        
        with self.assertRaises(KeyError):
            self.hash_table.get("name")
            
    def test_contains(self):
        self.hash_table.insert("name", "Alice")
        
        self.assertTrue(self.hash_table.contains("name"))
        self.assertFalse(self.hash_table.contains("age"))
        
    def test_hash_collision(self):
        # Aynı hash değerine sahip farklı keyler
        self.hash_table.insert("abc", 1)
        self.hash_table.insert("cba", 2)
        
        self.assertEqual(self.hash_table.get("abc"), 1)
        self.assertEqual(self.hash_table.get("cba"), 2)

if __name__ == '__main__':
    unittest.main() 