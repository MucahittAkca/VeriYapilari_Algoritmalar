import unittest
from data_structures.graph import Graph

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        
    def test_add_vertex_and_edge(self):
        self.graph.add_vertex(1)
        self.graph.add_vertex(2)
        self.graph.add_edge(1, 2)
        
        self.assertIn(2, self.graph.get_neighbors(1))
        self.assertIn(1, self.graph.get_neighbors(2))
        
    def test_remove_edge(self):
        self.graph.add_edge(1, 2)
        self.graph.remove_edge(1, 2)
        
        self.assertNotIn(2, self.graph.get_neighbors(1))
        self.assertNotIn(1, self.graph.get_neighbors(2))
        
    def test_bfs(self):
        self.graph.add_edge(1, 2)
        self.graph.add_edge(1, 3)
        self.graph.add_edge(2, 4)
        self.graph.add_edge(3, 4)
        
        traversal = self.graph.bfs(1)
        self.assertEqual(len(traversal), 4)
        self.assertEqual(traversal[0], 1)

    def test_dfs(self):
        self.graph.add_edge(1, 2)
        self.graph.add_edge(1, 3)
        self.graph.add_edge(2, 4)
        self.graph.add_edge(3, 4)
        
        traversal = self.graph.dfs(1)
        self.assertEqual(len(traversal), 4)
        self.assertEqual(traversal[0], 1)

if __name__ == '__main__':
    unittest.main() 