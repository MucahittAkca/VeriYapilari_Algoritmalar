class HashTable:
    """
    Hash Table (Hash Map) veri yapısı implementasyonu
    
    Zaman Karmaşıklığı:
    - ekleme: O(1) - ortalama durum, O(n) - en kötü durum (çakışma durumunda)
    - arama: O(1) - ortalama durum, O(n) - en kötü durum
    - silme: O(1) - ortalama durum, O(n) - en kötü durum
    """
    
    def __init__(self, size=256):
        self.size = size
        self.table = [[] for _ in range(self.size)]  # Chaining yöntemi için
        
    def _hash(self, key):
        """Hash fonksiyonu"""
        if isinstance(key, str):
            # String için basit bir hash fonksiyonu
            return sum(ord(c) for c in key) % self.size
        # Sayısal değerler için
        return key % self.size
        
    def insert(self, key, value):
        """Hash table'a yeni eleman ekler"""
        hash_key = self._hash(key)
        
        # Bu hash değerinde daha önce eklenen elemanları kontrol et
        for i, (k, v) in enumerate(self.table[hash_key]):
            if k == key:
                # Aynı key varsa, value'yu güncelle
                self.table[hash_key][i] = (key, value)
                return
                
        # Yeni key-value çifti ekle
        self.table[hash_key].append((key, value))
        
    def get(self, key):
        """Key ile eşleşen value'yu döndürür"""
        hash_key = self._hash(key)
        
        for k, v in self.table[hash_key]:
            if k == key:
                return v
                
        raise KeyError(f"Key bulunamadı: {key}")
        
    def remove(self, key):
        """Key ile eşleşen elemanı siler"""
        hash_key = self._hash(key)
        
        for i, (k, v) in enumerate(self.table[hash_key]):
            if k == key:
                del self.table[hash_key][i]
                return
                
        raise KeyError(f"Key bulunamadı: {key}")
        
    def contains(self, key):
        """Key'in var olup olmadığını kontrol eder"""
        hash_key = self._hash(key)
        
        return any(k == key for k, v in self.table[hash_key]) 