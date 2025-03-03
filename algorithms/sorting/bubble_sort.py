def bubble_sort(arr):
    """
    Bubble Sort algoritması implementasyonu
    
    Zaman Karmaşıklığı:
    - En iyi durum: O(n) - dizi zaten sıralıysa
    - Ortalama durum: O(n^2)
    - En kötü durum: O(n^2)
    
    Uzay Karmaşıklığı: O(1)
    """
    n = len(arr)
    
    for i in range(n):
        # Her iterasyonda en büyük eleman sona gider
        for j in range(0, n-i-1):
            # Yan yana elemanları karşılaştır
            if arr[j] > arr[j+1]:
                # Yer değiştir
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    return arr 