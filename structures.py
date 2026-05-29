#pertama buat fitur buku yang treakhir di tambahin dulu ya 
class StackBuku:
    def __init__(self):
        self.items = []

    def push(self, data_buku):
        self.items.append(data_buku)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def get_all(self):
        return self.items

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

def urutkan_buku(
