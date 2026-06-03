import tkinter as tk
from tkinter import messagebox
from logic import SistemPerpustakaan

class AplikasiPerpustakaanGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Manajemen Perpustakaan")
        self.root.geometry("700x500")

        self.perpus = SistemPerpustakaan()

        # DATA CONTOH
        self.perpus.tambah_buku_baru(101, "Algoritma Pemrograman", "Andi", 2, 2022)
        self.perpus.tambah_buku_baru(102, "Struktur Data Python", "Budi", 1, 2023)
        self.perpus.tambah_buku_baru(103, "Sistem Operasi", "Cici", 0, 2024)

        tk.Label(
            root,
            text="SISTEM MANAJEMEN PERPUSTAKAAN",
            font=("Arial", 16, "bold")
        ).pack(pady=20)

        tk.Button(
            root,
            text="Tambah Buku Baru",
            width=40,
            command=self.tambah_buku
        ).pack(pady=5)

        tk.Button(
            root,
            text="Lihat Semua Koleksi Buku (BST Inorder)",
            width=40,
            command=self.lihat_semua_buku
        ).pack(pady=5)

        tk.Button(
            root,
            text="Lihat Buku yang Terakhir Ditambahkan (Stack)",
            width=40,
            command=self.lihat_riwayat
        ).pack(pady=5)

        tk.Button(
            root,
            text="Pinjam Buku / Masuk Daftar Tunggu (Queue)",
            width=40,
            command=self.pinjam_buku
        ).pack(pady=5)

        tk.Button(
            root,
            text="Kembalikan Buku",
            width=40,
            command=self.kembalikan_buku
        ).pack(pady=5)

        tk.Button(
            root,
            text="Keluar",
            width=40,
            command=self.root.destroy
        ).pack(pady=20)

    # TAMBAH BUKU
    def tambah_buku(self):
        window = tk.Toplevel(self.root)
        window.title("Tambah Buku Baru")
        window.geometry("350x250")

        tk.Label(window, text="ID Buku").grid(row=0, column=0, padx=5, pady=5)
        id_entry = tk.Entry(window)
        id_entry.grid(row=0, column=1)

        tk.Label(window, text="Judul Buku").grid(row=1, column=0, padx=5, pady=5)
        judul_entry = tk.Entry(window)
        judul_entry.grid(row=1, column=1)

        tk.Label(window, text="Pengarang").grid(row=2, column=0, padx=5, pady=5)
        pengarang_entry = tk.Entry(window)
        pengarang_entry.grid(row=2, column=1)

        tk.Label(window, text="Stok").grid(row=3, column=0, padx=5, pady=5)
        stok_entry = tk.Entry(window)
        stok_entry.grid(row=3, column=1)

        tk.Label(window, text="Tahun Terbit").grid(row=4, column=0, padx=5, pady=5)
        tahun_entry = tk.Entry(window)
        tahun_entry.grid(row=4, column=1)

        def simpan():
            try:
                sukses, pesan = self.perpus.tambah_buku_baru(
                    int(id_entry.get()),
                    judul_entry.get(),
                    pengarang_entry.get(),
                    int(stok_entry.get()),
                    int(tahun_entry.get())
                )

                if sukses:
                    messagebox.showinfo("Berhasil", pesan)
                    window.destroy()
                else:
                    messagebox.showerror("Gagal", pesan)

            except ValueError:
                messagebox.showerror(
                    "Error",
                    "ID, Stok, dan Tahun harus berupa angka!"
                )

        tk.Button(
            window,
            text="Simpan",
            command=simpan
        ).grid(row=5, columnspan=2, pady=10)

    # LIHAT SEMUA BUKU
    def lihat_semua_buku(self):
        daftar = self.perpus.lihat_semua_buku()
        hasil = ""

        for buku in daftar:
            hasil += (
                f"ID Buku    : {buku.id}\n"
                f"Judul      : {buku.judul}\n"
                f"Pengarang  : {buku.pengarang}\n"
                f"Stok       : {buku.stok}\n"
                f"Tahun      : {buku.tahun}\n"
            )

            if not buku.antrean.is_empty():
                hasil += (
                    f"Daftar Tunggu : "
                    f"{', '.join(buku.antrean.get_all_antrean())}\n"
                )

            hasil += "\n----------------------------------\n\n"

        if hasil == "":
            hasil = "Belum ada buku dalam sistem."

        messagebox.showinfo(
            "Daftar Koleksi Buku (BST Inorder)",
            hasil
        )

    # RIWAYAT STACK
    def lihat_riwayat(self):
        data = self.perpus.lihat_riwayat_terbaru()

        if not data:
            messagebox.showinfo(
                "Riwayat",
                "Belum ada buku yang ditambahkan."
            )
            return

        hasil = ""
        for i, buku in enumerate(reversed(data), start=1):
            hasil += f"{i}. {buku.judul} (ID: {buku.id})\n"

        messagebox.showinfo(
            "Buku Terakhir Ditambahkan (Stack)",
            hasil
        )

    # PINJAM BUKU
    def pinjam_buku(self):
        window = tk.Toplevel(self.root)
        window.title("Pinjam Buku")
        window.geometry("350x180")

        tk.Label(window, text="ID Buku").grid(row=0, column=0, padx=5, pady=5)
        id_entry = tk.Entry(window)
        id_entry.grid(row=0, column=1)

        tk.Label(window, text="Nama Peminjam").grid(row=1, column=0, padx=5, pady=5)
        nama_entry = tk.Entry(window)
        nama_entry.grid(row=1, column=1)

        def proses():
            try:
                sukses, pesan = self.perpus.pinjam_atau_antre(
                    int(id_entry.get()),
                    nama_entry.get()
                )
                messagebox.showinfo("Informasi", pesan)
                window.destroy()

            except ValueError:
                messagebox.showerror(
                    "Error",
                    "ID Buku harus berupa angka."
                )

        tk.Button(
            window,
            text="Proses",
            command=proses
        ).grid(row=2, columnspan=2, pady=10)

    # KEMBALIKAN
    def kembalikan_buku(self):
        window = tk.Toplevel(self.root)
        window.title("Kembalikan Buku")
        window.geometry("300x150")

        tk.Label(window, text="ID Buku").grid(row=0, column=0, padx=5, pady=5)
        id_entry = tk.Entry(window)
        id_entry.grid(row=0, column=1)

        def proses():
            try:
                sukses, pesan = self.perpus.kembalikan_buku(int(id_entry.get()))
                messagebox.showinfo("Informasi", pesan)
                window.destroy()

            except ValueError:
                messagebox.showerror(
                    "Error",
                    "ID Buku harus berupa angka."
                )

        tk.Button(
            window,
            text="Proses",
            command=proses
        ).grid(row=1, columnspan=2, pady=10)