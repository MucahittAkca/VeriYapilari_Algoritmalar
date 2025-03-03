def quick_sort(arr):
    """
    Quick Sort algoritması implementasyonu
    
    Zaman Karmaşıklığı:
    - En iyi durum: O(n log n)
    - Ortalama durum: O(n log n)
    - En kötü durum: O(n²) - pivot en büyük/küçük eleman olduğunda
    
    Uzay Karmaşıklığı: O(log n)
    """
    if len(arr) <= 1:
        return arr
        
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right) 