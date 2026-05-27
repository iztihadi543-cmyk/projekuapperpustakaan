from structures import BinarySearchTree, StackBuku, urutkan_buku_by_judul, cari_buku_by_keyword

class KontrolPerpustakaan:
    def __init__(self):
        self.db_buku = BinarySearchTree()
        self.riwayat_stack = StackBuku()

    def tambah_buku(self, id_buku, judul, pengarang, stok):
        if not id_buku or not judul or not pengarang or stok == "":
            return False, "Semua kolom input wajib diisi!"

        try:
            id_int = int(id_buku)
            stok_int = int(stok)
        except ValueError:
            return False, "ID Buku dan Stok harus berupa angka!"

        if self.db_buku.search(id_int):
            return False, f"Gagal! Buku dengan ID {id_int} sudah terdaftar."

        self.db_buku.insert(id_int, judul, pengarang, stok_int)
        self.riwayat_stack.push(f"[{id_int}] {judul}")

        return True, "Buku berhasil ditambahkan ke sistem!"

    def ambil_semua(self):
        return self.db_buku.get_all_books()

    def edit_buku(self, id_buku, judul, pengarang, stok):
        try:
            id_int = int(id_buku)
            stok_int = int(stok)
        except ValueError:
            return False, "ID dan Stok validasi harus angka!"

        buku = self.db_buku.search(id_int)

        if buku:
            buku.judul = judul
            buku.pengarang = pengarang
            buku.stok = stok_int
            return True, "Data buku berhasil diperbarui!"

        return False, "Buku tidak ditemukan!"

    def hapus_buku(self, id_buku):
        try:
            id_int = int(id_buku)
        except ValueError:
            return False, "ID Buku tidak valid!"

        buku = self.db_buku.search(id_int)

        if buku:
            buku.judul = f"[DIHAPUS] {buku.judul}"
            buku.stok = 0
            return True, "Buku berhasil dihapus dari katalog aktif!"

        return False, "Buku tidak ditemukan!"

    def pinjam_buku(self, id_buku, nama_peminjam):
        if not nama_peminjam:
            return False, "Nama peminjam tidak boleh kosong!"

        buku = self.db_buku.search(int(id_buku))

        if not buku:
            return False, "Buku tidak ditemukan!"

        if buku.stok > 0:
            buku.stok -= 1
            return True, f"Berhasil meminjam! Stok sisa: {buku.stok}"

        buku.antrean.enqueue(nama_peminjam)
        return True, f"Stok habis! {nama_peminjam} dimasukkan ke Daftar Tunggu (Queue)."