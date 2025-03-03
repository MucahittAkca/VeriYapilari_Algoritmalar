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
        """i indeksindeki elemanın ebeveyn indeksini döndürür"""
        return (i - 1) // 2
        
    def left_child(self, i):
        """i indeksindeki elemanın sol çocuğunun indeksini döndürür"""
        return 2 * i + 1
        
    def right_child(self, i):
        """i indeksindeki elemanın sağ çocuğunun indeksini döndürür"""
        return 2 * i + 2
        
    def swap(self, i, j):
        """i ve j indekslerindeki elemanları değiştirir"""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        
    def insert(self, key):
        """Heap'e yeni eleman ekler"""
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)
        
    def extract_min(self):
        """En küçük elemanı çıkarır ve döndürür"""
        if not self.heap:
            return None
            
        if len(self.heap) == 1:
            return self.heap.pop()
            
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()  # Son elemanı köke taşı
        self._heapify_down(0)  # Kökten başlayarak heap özelliğini düzelt
            
        return min_val
        
    def _heapify_up(self, i):
        """i indeksindeki elemanı yukarı taşıyarak heap özelliğini korur"""
        while i > 0:
            parent = self.parent(i)
            if self.heap[i] < self.heap[parent]:
                self.swap(i, parent)
                i = parent
            else:
                break
                
    def _heapify_down(self, i):
        """i indeksindeki elemanı aşağı taşıyarak heap özelliğini korur"""
        size = len(self.heap)
        while True:
            smallest = i
            left = self.left_child(i)
            right = self.right_child(i)
            
            # Sol çocuk varsa ve kökten küçükse
            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left
                
            # Sağ çocuk varsa ve şimdiye kadar bulunan en küçükten küçükse
            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right
                
            # Eğer en küçük eleman değişmediyse işlem tamamdır
            if smallest == i:
                break
                
            # Değilse swap yapıp devam et
            self.swap(i, smallest)
            i = smallest 