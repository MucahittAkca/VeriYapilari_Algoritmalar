class Node:
    """Bağlı liste düğüm sınıfı"""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """
    Tek yönlü bağlı liste implementasyonu
    
    Zaman Karmaşıklığı:
    - başa ekleme: O(1)
    - sona ekleme: O(n)
    - araya ekleme: O(n)
    - silme: O(n)
    - arama: O(n)
    """
    
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self, data):
        """Liste başına eleman ekler"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def insert_at_end(self, data):
        """Liste sonuna eleman ekler"""
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
            
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        
    def delete(self, key):
        """Verilen değere sahip ilk düğümü siler"""
        current = self.head
        
        if current and current.data == key:
            self.head = current.next
            return
            
        while current and current.next:
            if current.next.data == key:
                current.next = current.next.next
                return
            current = current.next
            
    def search(self, key):
        """Verilen değeri listede arar"""
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False
        
    def display(self):
        """Listeyi yazdırır"""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements 