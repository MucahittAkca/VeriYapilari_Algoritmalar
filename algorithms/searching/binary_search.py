def binary_search(arr, target):
    """
    Binary Search algoritması implementasyonu
    
    Zaman Karmaşıklığı:
    - En iyi durum: O(1)
    - Ortalama durum: O(log n)
    - En kötü durum: O(log n)
    
    Not: Dizi sıralı olmalıdır
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1  # Eleman bulunamadı 