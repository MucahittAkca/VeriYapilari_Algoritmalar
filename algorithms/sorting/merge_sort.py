def merge_sort(arr):
    """
    Merge Sort algoritması implementasyonu
    
    Zaman Karmaşıklığı:
    - En iyi durum: O(n log n)
    - Ortalama durum: O(n log n)
    - En kötü durum: O(n log n)
    
    Uzay Karmaşıklığı: O(n)
    """
    if len(arr) <= 1:
        return arr
        
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)
    
def merge(left, right):
    """İki sıralı diziyi birleştirir"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    return result 