# gui.py
from logic import SistemPerpustakaan

class MenuAplikasi:
    def __init__(self):
        self.perpus = SistemPerpustakaan()

    def tampilkan_menu(self):
        # Mengisi data dummy awal untuk mempermudah demonstrasi/pengujian
        self.perpus.tambah_buku_baru(102, "Struktur Data Python", "Budi", 1, 2023)
        self.perpus.tambah_buku_baru(101, "Algoritma Pemrograman", "Andi", 2, 2022)
        self.perpus.tambah_buku_baru(103, "Sistem Operasi", "Cici", 0, 2024)

        while True:
            print("\n================ SYSTEM MANAJEMEN PERPUSTAKAAN ================")
            print("1. Tambah Buku Baru")
            print("2. Lihat Semua Koleksi Buku (Urutan ID - BST Inorder)")
            print("3. Lihat Buku yang Terakhir Ditambahkan (Stack)")
            print("4. Pinjam Buku / Masuk Daftar Tunggu (Queue)")
            print("5. Kembalikan Buku")
            print("6. Keluar")
            print("===============================================================")
            
            pilihan = input("Pilih menu (1-6): ")

            if pilihan == "1":
                try:
                    id_buku = int(input("Masukkan ID Buku (Angka): "))
                    judul = input("Masukkan Judul Buku: ")
                    pengarang = input("Masukkan Pengarang: ")
                    stok = int(input("Masukkan Jumlah Stok: "))
                    tahun = int(input("Masukkan Tahun Terbit: "))
                    
                    sukses, pesan = self.perpus.tambah_buku_baru(id_buku, judul, pengarang, stok, tahun)
                    print(f"\n{'✅' if sukses else '❌'} {pesan}")
                except ValueError:
                    print("\n❌ Input gagal! ID, Stok, dan Tahun harus berupa angka.")

            elif pilihan == "2":
                print("\n--- DAFTAR BUKU DI PERPUSTAKAAN ---")
                buku_list = self.perpus.lihat_semua_buku()
                if not buku_list:
                    print("Kosong. Belum ada buku di perpustakaan.")
                for buku in buku_list:
                    print(buku)
                    # Jika ada antrean di buku tersebut, tampilkan jalurnya
                    if not buku.antrean.is_empty():
                        print(f"   ↳ ⏳ Daftar Tunggu: {buku.antrean.get_all_antrean()}")

            elif pilihan == "3":
                print("\n--- BUKU YANG TERAKHIR DITAMBAHKAN (Stack) ---")
                riwayat = self.perpus.lihat_riwayat_terbaru()
                if not riwayat:
                    print("Belum ada riwayat penambahan buku.")
                for i, buku in enumerate(riwayat, 1):
                    print(f"{i}. {buku.judul} (ID: {buku.id})")

            elif pilihan == "4":
                try:
                    id_buku = int(input("Masukkan ID Buku yang ingin dipinjam: "))
                    nama = input("Masukkan Nama Peminjam: ")
                    sukses, pesan = self.perpus.pinjam_atau_antre(id_buku, nama)
                    print(f"\n📢 {pesan}")
                except ValueError:
                    print("\n❌ ID Buku harus berupa angka.")

            elif pilihan == "5":
                try:
                    id_buku = int(input("Masukkan ID Buku yang dikembalikan: "))
                    sukses, pesan = self.perpus.kembalikan_buku(id_buku)
                    print(f"\n📢 {pesan}")
                except ValueError:
                    print("\n❌ ID Buku harus berupa angka.")

            elif pilihan == "6":
                print("\n👋 Keluar dari sistem perpustakaan. Terima kasih!")
                break
            else:
                print("\n❌ Pilihan tidak valid! Silakan masukkan angka 1-6.")