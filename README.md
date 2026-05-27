/projek uap
│
├── main.py                  # File utama untuk menjalankan aplikasi dan inisialisasi Tkinter.
├── gui.py             # Menyimpan kelas-kelas tampilan antarmuka (Tkinter Windows/Frames).
├── structures.py       # Berisi implementasi manual Stack, Queue, LinkedList, BST, dll.
└── logic.py         # Berisi fungsi CRUD yang menghubungkan data_structures dengan GUI.

1. Fitur Utama : Manajemen Buku (CRUD)
    Sesuai dengan instruksi pengerjaan, sistem ini wajib memiliki fungsi operasional dasar:
    - Tambah Buku Baru (Create): Menginput ID buku, judul, pengarang, dan jumlah stok awal ke dalam sistem. Data ini otomatis disimpan secara terstruktur di dalam Binary Search Tree (BST).
    - Tampilkan Daftar Buku (Read): Menampilkan seluruh koleksi buku yang ada di perpustakaan dalam bentuk tabel (GUI) agar mudah dilihat oleh pengguna.
    - Edit Informasi Buku (Update): Mengubah detail informasi buku (seperti memperbaiki salah ketik pada judul atau memperbarui jumlah stok) berdasarkan ID bukunya.
    - Hapus Buku (Delete): Menghapus data buku tertentu dari sistem jika buku tersebut sudah tidak tersedia atau rusak.

2. Fitur Pendukung (Implementasi 6 Materi Algoritma)
    Fitur-fitur ini dirancang khusus untuk memenuhi bobot penilaian struktur data terbesar (40%) tanpa menggunakan library bantuan:
    a. Fitur Waiting List (Antrean Peminjam): * Struktur Data: Queue & Linked List
        - Cara Kerja: Jika seorang anggota ingin meminjam buku namun stok buku tersebut sedang habis (Stok = 0), nama anggota tersebut akan dimasukkan ke dalam daftar tunggu (antrean). Orang yang pertama kali mengantre akan mendapatkan buku terlebih dahulu saat stok kembali tersedia.
    b. Fitur Riwayat Buku Terbaru (Recently Added):
        - Fitur Riwayat Buku Terbaru (Recently Added):
        - Cara Kerja: Menampilkan daftar buku yang paling akhir dimasukkan oleh admin. Buku yang paling baru diinput akan muncul di urutan paling atas.
    c. Fitur Pengurutan Alfabetis (Sorting):
        - Struktur Data: Bubble Sort (Manual)
        - Cara Kerja: Menyediakan tombol di GUI untuk mengurutkan tampilan daftar buku berdasarkan abjad Judul Buku (A-Z) agar pencarian manual oleh admin lebih nyaman.
    d. Fitur Pencarian Pintar (Searching):
        - Struktur Data: Linear Search & BST Search
        - Cara Kerja: Admin bisa mencari buku secara instan. Jika mencari berdasarkan ID Buku, sistem menggunakan efisiensi BST Search. Jika mencari berdasarkan kata kunci (keyword) nama judul atau pengarang, sistem menggunakan Linear Search.