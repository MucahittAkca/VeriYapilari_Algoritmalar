class MinHeap:
    """
    Min Heap veri yapısı implementasyonu
    
    Zaman Karmaşıklığı:
    - ekleme: O(log n)
    - minimum değeri çıkarma: O(log n)
    - minimum değeri görme: O(1)
    """
    
    def __init__(self):
        self.heap = []
        
    def parent(self, i):
        return (i - 1) // 2
        
    def left_child(self, i):
        return 2 * i + 1
        
    def right_child(self, i):
        return 2 * i + 2
        
    def insert(self, key):
        """Heap'e yeni eleman ekler"""
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)
        
    def extract_min(self):
        """En küçük elemanı çıkarır ve döndürür"""
        if not self.heap:
            return None
            
        min_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        
        if self.heap:
            self._heapify_down(0)
            
        return min_val
        
    def _heapify_up(self, i):
        """Elemanı yukarı taşıyarak heap özelliğini korur"""
        parent = self.parent(i)
        if i > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            self._heapify_up(parent)
            
    def _heapify_down(self, i):
        """Elemanı aşağı taşıyarak heap özelliğini korur"""
        min_idx = i
        left = self.left_child(i)
        right = self.right_child(i)
        
        if left < len(self.heap) and self.heap[left] < self.heap[min_idx]:
            min_idx = left
            
        if right < len(self.heap) and self.heap[right] < self.heap[min_idx]:
            min_idx = right
            
        if min_idx != i:
            self.heap[i], self.heap[min_idx] = self.heap[min_idx], self.heap[i]
            self._heapify_down(min_idx) 