# Python Veri Yapıları ve Algoritmalar

Bu repo, eğitimim sırasında öğrendiğim temel veri yapıları ve algoritmaların Python implementasyonlarını içerir. Her bir implementasyon için kapsamlı testler ve Big-O analizleri eklenmiştir.

## 📚 İçindekiler

### Veri Yapıları

#### 1. Stack
- `push(item)`: Yığına eleman ekler - O(1)
- `pop()`: Yığından eleman çıkarır - O(1)
- `peek()`: En üstteki elemanı gösterir - O(1)
- `is_empty()`: Yığının boş olup olmadığını kontrol eder - O(1)

#### 2. Queue
- `enqueue(item)`: Kuyruğa eleman ekler - O(1)
- `dequeue()`: Kuyruktan eleman çıkarır - O(1)
- `front()`: Kuyruğun başındaki elemanı gösterir - O(1)
- `is_empty()`: Kuyruğun boş olup olmadığını kontrol eder - O(1)

#### 3. Linked List
- `insert_at_beginning(data)`: Liste başına eleman ekler - O(1)
- `insert_at_end(data)`: Liste sonuna eleman ekler - O(n)
- `delete(key)`: Verilen değere sahip elemanı siler - O(n)
- `search(key)`: Verilen değeri listede arar - O(n)

#### 4. Binary Tree
- `insert(data)`: Ağaca yeni düğüm ekler - O(h)
- `search(data)`: Ağaçta değer arar - O(h)
- `inorder_traversal()`: Sol-Kök-Sağ gezinme
- `preorder_traversal()`: Kök-Sol-Sağ gezinme
- `postorder_traversal()`: Sol-Sağ-Kök gezinme

#### 5. Graph
- `add_vertex(vertex)`: Grafa yeni düğüm ekler - O(1)
- `add_edge(vertex1, vertex2)`: İki düğüm arasına kenar ekler - O(1)
- `remove_edge(vertex1, vertex2)`: Kenarı siler - O(V)
- `bfs(start_vertex)`: Genişlik öncelikli arama - O(V + E)
- `dfs(start_vertex)`: Derinlik öncelikli arama - O(V + E)

#### 6. Hash Table (Hash Tablosu)
- `insert(key, value)`: Tabloya eleman ekler - O(1)*
- `get(key)`: Key ile eşleşen değeri döndürür - O(1)*
- `remove(key)`: Key ile eşleşen elemanı siler - O(1)*
- `contains(key)`: Key'in var olup olmadığını kontrol eder - O(1)*
* Çakışma durumunda O(n)

#### 7. Heap (Yığın)
- `insert(key)`: Heap'e eleman ekler - O(log n)
- `extract_min()`: En küçük elemanı çıkarır - O(log n)
- `_heapify_up()`: Yukarı taşıma işlemi - O(log n)
- `_heapify_down()`: Aşağı taşıma işlemi - O(log n)

### Algoritmalar

#### Sıralama Algoritmaları
1. **Bubble Sort**
   - En iyi durum: O(n)
   - Ortalama durum: O(n²)
   - En kötü durum: O(n²)

2. **Quick Sort**
   - En iyi durum: O(n log n)
   - Ortalama durum: O(n log n)
   - En kötü durum: O(n²)

3. **Merge Sort**
   - Her durumda: O(n log n)
   - Uzay karmaşıklığı: O(n)

#### Arama Algoritmaları
1. **Binary Search**
   - Sıralı dizilerde - O(log n)
   - Dizi sıralı olmalıdır

2. **Linear Search**
   - Her durumda - O(n)
   - Sıralı olmayan dizilerde kullanılabilir

## 🚀 Kurulum

### Repoyu klonlayın
git clone https://github.com/MucahittAkca/VeriYapilari_Algoritmalar.git
### Proje dizinine gidin
cd dsa_python
### Testleri çalıştırın
python -m unittest discover tests



## 📝 Notlar
- Her bir veri yapısı ve algoritma için detaylı açıklamalar kodların içinde bulunmaktadır.
- Tüm implementasyonlar için test dosyaları mevcuttur.
- Big-O analizleri her bir sınıf/fonksiyon için dokümante edilmiştir.


## 🙏 Teşekkürler
Bu repo, veri yapıları ve algoritmalar dersinde öğrendiklerimi pekiştirmek ve başkalarına yardımcı olmak amacıyla oluşturulmuştur. Katkıda bulunan herkese teşekkürler!