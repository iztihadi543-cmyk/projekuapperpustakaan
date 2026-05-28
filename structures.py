#pertama buat fitur buku yang treakhir di tambahin dulu ya 
class StackBuku:
    def __init__(self):
        self.items = []

    def push(self, data_buku):
        self.items.append(data_buku)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def all(self):
        return self.items[::-1]

#nah terus kita buat fitur daftar tunggu ya, pake queue sama linked list ya 
class QueueNode:
    def __init__(self, nama_peminjam):
        self.nama = nama_peminjam
        self.next = None

class QueueAntrean:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, nama_peminjam):
        new_node = QueueNode(nama_peminjam)
        if self.tail is None:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        temp = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return temp.nama

    def is_empty(self):
        return self.head is None

    def get_all_antrean(self):
        daftar = []
        current = self.head
        while current:
            daftar.append(current.nama)
            current = current.next
        return daftar

#Implementasi Binary Search Tree (BST)
class BSTNode:
    def __init__(self, id_buku, judul, pengarang, stok):
        self.id = id_buku
        self.judul = judul
        self.pengarang = pengarang
        self.stok = stok
        self.tahun = tahun
        self.antrean = QueueAntrean()
        self.left = None
        self.right = None

def __repr__(self):
    return f"[ID: {self.id} | {self.tahun}] {self.judul} - {self.pengarang} (Stok: {self.stok})"
    
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, id_buku, judul, pengarang, stok, tahun):
        new_node = BSTNode(id_buku, judul, pengarang, stok, tahun)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_rekursif(self.root, new_node)

    def _insert_rekursif(self, current, new_node):
        if new_node.id < current.id:
            if current.left is None:
                current.left = new_node
            else:
                self._insert_rekursif(current.left, new_node)
        elif new_node.id > current.id:
            if current.right is None:
                current.right = new_node
            else:
                self._insert_rekursif(current.right, new_node)
        
    def search(self, id_buku):
        return self._search_rekursif(self.root, id_buku)

    def _search_rekursif(self, current, id_buku):
        if current is None or current.id == id_buku:
            return current
        if id_buku < current.id:
            return self._search_rekursif(current.left, id_buku)
        return self._search_rekursif(current.right, id_buku)

    def get_all_books(self):
        books = []
        self._inorder(self.root, books)
        return books

    def _inorder(self, current, books):
        if current:
            self._inorder(current.left, books)
            books.append(current)
            self._inorder(current.right, books)

#Implementasi algoritma sorting (bubble)
   def urutkan_berdasarkan_abjad(daftar_buku):
    jumlah_buku = len(daftar_buku)
    for i in range(jumlah_buku):
        for j in range(0, jumlah_buku - i - 1):
            if daftar_buku[j].judul.lower() > daftar_buku[j + 1].judul.lower():
                temp = daftar_buku[j]
                daftar_buku[j] = daftar_buku[j + 1]
                daftar_buku[j + 1] = temp
                
    return daftar_buku

   def urutkan_berdasarkan_tahun(daftar_buku):
    jumlah_buku = len(daftar_buku)
    for i in range(jumlah_buku):
        for j in range(0, jumlah_buku - i - 1):
            # Di sini kuncinya! Kita membandingkan atribut .tahun milik objek buku
            if daftar_buku[j].tahun > daftar_buku[j + 1].tahun:
                # Proses tukar posisi pakai temp
                temp = daftar_buku[j]
                daftar_buku[j] = daftar_buku[j + 1]
                daftar_buku[j + 1] = temp
    return daftar_buku

#implementasi algoritma searching
   def linear_search_by_title(daftar_buku, kata_kunci):
       hasil = []
       for buku in daftar_buku:
           if kata_kunci.lower() in buku.judul.lower():
               hasil.append(buku)
      return hasil

#class untuk data peminjam
  class Peminjam:
    def __init__(self, nama, no_telp, alamat, tgl_pinjam, waktu_pinjam):
        self.nama = nama
        self.no_telp = no_telp
        self.alamat = alamat
        self.tgl_pinjam = tgl_pinjam      # Contoh isi: "28-05-2026"
        self.waktu_pinjam = waktu_pinjam  # Contoh isi: "14:30"
        
    def __repr__(self):
        return f"{self.nama} ({self.no_telp}) - Tgl: {self.tgl_pinjam} Jam: {self.waktu_pinjam}"
