class Node:
    """İkili ağaç düğüm sınıfı"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    """
    İkili ağaç implementasyonu
    
    Zaman Karmaşıklığı:
    - ekleme: O(h) - h: ağaç yüksekliği
    - arama: O(h)
    - silme: O(h)
    - derinlik öncelikli gezinme: O(n)
    """
    
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        """Ağaca yeni düğüm ekler"""
        if not self.root:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)
            
    def _insert_recursive(self, node, data):
        """Recursive olarak ekleme yapar"""
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(node.right, data)
                
    def search(self, data):
        """Ağaçta değer arar"""
        return self._search_recursive(self.root, data)
        
    def _search_recursive(self, node, data):
        """Recursive olarak arama yapar"""
        if node is None or node.data == data:
            return node
            
        if data < node.data:
            return self._search_recursive(node.left, data)
        return self._search_recursive(node.right, data)
        
    def inorder_traversal(self):
        """Inorder gezinme (Sol-Kök-Sağ)"""
        elements = []
        self._inorder_recursive(self.root, elements)
        return elements
        
    def _inorder_recursive(self, node, elements):
        """Recursive olarak inorder gezinme"""
        if node:
            self._inorder_recursive(node.left, elements)
            elements.append(node.data)
            self._inorder_recursive(node.right, elements)
        
    def preorder_traversal(self):
        """Preorder gezinme (Kök-Sol-Sağ)"""
        elements = []
        self._preorder_recursive(self.root, elements)
        return elements
        
    def _preorder_recursive(self, node, elements):
        if node:
            elements.append(node.data)
            self._preorder_recursive(node.left, elements)
            self._preorder_recursive(node.right, elements)
        
    def postorder_traversal(self):
        """Postorder gezinme (Sol-Sağ-Kök)"""
        elements = []
        self._postorder_recursive(self.root, elements)
        return elements
        
    def _postorder_recursive(self, node, elements):
        if node:
            self._postorder_recursive(node.left, elements)
            self._postorder_recursive(node.right, elements)
            elements.append(node.data) 