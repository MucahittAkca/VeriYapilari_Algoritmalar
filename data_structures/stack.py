class Stack:
    """
    Stack veri yapısı implementasyonu
    
    Zaman Karmaşıklığı:
    - push: O(1)
    - pop: O(1)
    - peek: O(1)
    - is_empty: O(1)
    """
    
    def __init__(self):
        self.items = []
        
    def push(self, item):
        """Yığının üstüne eleman ekler"""
        self.items.append(item)
        
    def pop(self):
        """Yığının üstündeki elemanı çıkarır ve döndürür"""
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Stack boş")
        
    def peek(self):
        """Yığının üstündeki elemanı döndürür ama çıkarmaz"""
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Stack boş")
        
    def is_empty(self):
        """Yığının boş olup olmadığını kontrol eder"""
        return len(self.items) == 0
        
    def size(self):
        """Yığındaki eleman sayısını döndürür"""
        return len(self.items) 