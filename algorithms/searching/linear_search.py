def linear_search(arr, target):
    """
    Linear Search algoritması implementasyonu
    
    Zaman Karmaşıklığı:
    - En iyi durum: O(1)
    - Ortalama durum: O(n)
    - En kötü durum: O(n)
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  # Eleman bulunamadı 