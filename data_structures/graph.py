class Graph:
    """
    Graf veri yapısı implementasyonu (Komşuluk listesi kullanarak)
    
    Zaman Karmaşıklığı:
    - kenar ekleme: O(1)
    - kenar silme: O(V) - V: düğüm sayısı
    - komşu bulma: O(1)
    - graf gezinme: O(V + E) - E: kenar sayısı
    """
    
    def __init__(self):
        self.graph = {}
        
    def add_vertex(self, vertex):
        """Grafa yeni düğüm ekler"""
        if vertex not in self.graph:
            self.graph[vertex] = []
            
    def add_edge(self, vertex1, vertex2):
        """İki düğüm arasına kenar ekler (yönsüz graf)"""
        if vertex1 not in self.graph:
            self.add_vertex(vertex1)
        if vertex2 not in self.graph:
            self.add_vertex(vertex2)
            
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)  # Yönsüz graf için
        
    def remove_edge(self, vertex1, vertex2):
        """İki düğüm arasındaki kenarı siler"""
        if vertex1 in self.graph and vertex2 in self.graph:
            if vertex2 in self.graph[vertex1]:
                self.graph[vertex1].remove(vertex2)
            if vertex1 in self.graph[vertex2]:
                self.graph[vertex2].remove(vertex1)
                
    def get_neighbors(self, vertex):
        """Verilen düğümün komşularını döndürür"""
        return self.graph.get(vertex, [])
        
    def bfs(self, start_vertex):
        """Breadth-First Search (Genişlik Öncelikli Arama)"""
        visited = set()
        queue = [start_vertex]
        visited.add(start_vertex)
        traversal = []
        
        while queue:
            vertex = queue.pop(0)
            traversal.append(vertex)
            
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return traversal 

    def dfs(self, start_vertex):
        """Depth-First Search (Derinlik Öncelikli Arama)"""
        visited = set()
        traversal = []
        
        def dfs_recursive(vertex):
            visited.add(vertex)
            traversal.append(vertex)
            
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    dfs_recursive(neighbor)
                    
        dfs_recursive(start_vertex)
        return traversal 