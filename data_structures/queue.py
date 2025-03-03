class Queue:
    """
    Queue (Kuyruk) veri yapısı implementasyonu
    
    Zaman Karmaşıklığı:
    - enqueue: O(1)
    - dequeue: O(1)
    - front: O(1)
    - is_empty: O(1)
    """
    
    def __init__(self):
        self.items = []
        
    def enqueue(self, item):
        """Kuyruğun sonuna eleman ekler"""
        self.items.append(item)
        
    def dequeue(self):
        """Kuyruğun başındaki elemanı çıkarır ve döndürür"""
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("Kuyruk boş")
        
    def front(self):
        """Kuyruğun başındaki elemanı döndürür ama çıkarmaz"""
        if not self.is_empty():
            return self.items[0]
        raise IndexError("Kuyruk boş")
        
    def is_empty(self):
        """Kuyruğun boş olup olmadığını kontrol eder"""
        return len(self.items) == 0
        
    def size(self):
        """Kuyruktaki eleman sayısını döndürür"""
        return len(self.items) 