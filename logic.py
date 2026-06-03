# logic.py
from structures import BinarySearchTree, StackBuku

class SistemPerpustakaan:
    def __init__(self):
        self.bst_buku = BinarySearchTree()
        self.stack_terbaru = StackBuku()

    def tambah_buku_baru(self, id_buku, judul, pengarang, stok, tahun):
        if self.bst_buku.search(id_buku):
            return False, f"Gagal! Buku dengan ID {id_buku} sudah terdaftar."
        
        buku_baru = self.bst_buku.insert(id_buku, judul, pengarang, stok, tahun)
        
        self.stack_terbaru.push(buku_baru)
        return True, f"Buku '{judul}' berhasil ditambahkan ke sistem."

    def pinjam_atau_antre(self, id_buku, nama_peminjam):
        buku = self.bst_buku.search(id_buku)
        if not buku:
            return False, "Buku tidak ditemukan!"

        if buku.stok > 0:
            buku.stok -= 1
            return True, f"Berhasil! {nama_peminjam} meminjam '{buku.judul}'. Sisa stok: {buku.stok}"
        else:
            buku.antrean.enqueue(nama_peminjam)
            return True, f"Stok habis! {nama_peminjam} dimasukkan ke DAFTAR TUNGGU buku '{buku.judul}'."

    def kembalikan_buku(self, id_buku):
        buku = self.bst_buku.search(id_buku)
        if not buku:
            return False, "Buku tidak ditemukan!"

        if not buku.antrean.is_empty():
            peminjam_berikutnya = buku.antrean.dequeue()
            return True, f"Buku '{buku.judul}' dikembalikan. [Antrean Otomatis] Buku langsung dipinjamkan ke: {peminjam_berikutnya}."
        else:
            buku.stok += 1
            return True, f"Buku '{buku.judul}' dikembalikan. Stok kini bertambah menjadi: {buku.stok}"

    def lihat_semua_buku(self):
        return self.bst_buku.get_all_books()

    def lihat_riwayat_terbaru(self):
        return self.stack_terbaru.get_all()