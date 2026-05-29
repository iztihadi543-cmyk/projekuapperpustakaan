# =====================================================================
# FILE: gui_app.py
# Menangani Tampilan Antarmuka Grafis (GUI) Menggunakan Tkinter
# =====================================================================
import tkinter as tk
from tkinter import messagebox, ttk
from logic import KontrolPerpustakaan
from structures import urutkan_buku_by_judul, cari_buku_by_keyword

class AplikasiPerpustakaanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Manajemen Perpustakaan - Tema B")
        self.root.geometry("850x600")
        
        # Inisialisasi logika kontrol
        self.kontrol = KontrolPerpustakaan()

        # --- FRAME FORM INPUT ---
        frame_input = tk.LabelFrame(root, text=" Form Kendali Buku (CRUD) ", padx=10, pady=10)
        frame_input.pack(fill="x", padx=15, pady=10)

        tk.Label(frame_input, text="ID Buku:").grid(row=0, column=0, sticky="w")
        self.ent_id = tk.Entry(frame_input, width=15)
        self.ent_id.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_input, text="Judul Buku:").grid(row=0, column=2, sticky="w")
        self.ent_judul = tk.Entry(frame_input, width=25)
        self.ent_judul.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(frame_input, text="Pengarang:").grid(row=1, column=0, sticky="w")
        self.ent_pengarang = tk.Entry(frame_input, width=15)
        self.ent_pengarang.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_input, text="Stok:").grid(row=1, column=2, sticky="w")
        self.ent_stok = tk.Entry(frame_input, width=10)
        self.ent_stok.grid(row=1, column=3, padx=5, pady=5)

        # Tombol Operasi CRUD
        tk.Button(frame_input, text="[C] Tambah Buku", bg="green", fg="white", command=self.aksi_tambah).grid(row=0, column=4, padx=10)
        tk.Button(frame_input, text="[U] Update Detail", bg="orange", command=self.aksi_update).grid(row=1, column=4, padx=10)
        tk.Button(frame_input, text="[D] Hapus Buku", bg="red", fg="white", command=self.aksi_hapus).grid(row=0, column=5, padx=10)

        # --- FRAME FITUR TAMBAHAN (Pencarian & Transaksi) ---
        frame_fitur = tk.LabelFrame(root, text=" Fitur Tambahan & Transaksi ", padx=10, pady=5)
        frame_fitur.pack(fill="x", padx=15, pady=5)

        tk.Label(frame_fitur, text="Cari Keyword:").grid(row=0, column=0)
        self.ent_cari = tk.Entry(frame_fitur, width=15)
        self.ent_cari.grid(row=0, column=1, padx=5)
        tk.Button(frame_fitur, text="Cari (Linear Search)", command=self.aksi_cari).grid(row=0, column=2, padx=5)
        tk.Button(frame_fitur, text="Urut Judul (Bubble Sort)", command=self.aksi_urutkan).grid(row=0, column=3, padx=5)

        tk.Label(frame_fitur, text="Nama Peminjam:").grid(row=0, column=4, padx=10)
        self.ent_peminjam = tk.Entry(frame_fitur, width=15)
        self.ent_peminjam.grid(row=0, column=5, padx=5)
        tk.Button(frame_fitur, text="Pinjam / Antre (Queue)", bg="blue", fg="white", command=self.aksi_pinjam).grid(row=0, column=6, padx=5)

        # --- TABEL DATA BUKU (TREEVIEW) ---
        tk.Label(root, text="Daftar Buku Terdaftar (Read BST):", font=("Arial", 10, "bold")).pack(anchor="w", padx=15, pady=5)
        self.tabel = ttk.Treeview(root, columns=("id", "judul", "pengarang", "stok", "antrean"), show="headings", height=12)
        self.tabel.heading("id", text="ID Buku")
        self.tabel.heading("judul", text="Judul Buku")
        self.tabel.heading("pengarang", text="Pengarang")
        self.tabel.heading("stok", text="Stok Tersedia")
        self.tabel.heading("antrean", text="Waiting List (Queue)")
        self.tabel.pack(fill="both", expand=True, padx=15, pady=5)

        # --- LOG RIWAYAT STACK ---
        self.lbl_riwayat = tk.Label(root, text="Riwayat Buku Terakhir Ditambahkan (Stack): Kosong", fg="purple", font=("Arial", 9, "italic"))
        self.lbl_riwayat.pack(anchor="w", padx=15, pady=10)

        self.refresh_tabel()

    # Fungsi untuk menyegarkan isi tabel Treeview
    def refresh_tabel(self, daftar_buku=None):
        for i in self.tabel.get_children():
            self.tabel.delete(i)
        
        if daftar_buku is None:
            daftar_buku = self.kontrol.ambil_semua()

        for b in daftar_buku:
            antrean_str = ", ".join(b.antrean.get_all_antrean()) if not b.antrean.is_empty() else "-"
            self.tabel.insert("", "end", values=(b.id, b.judul, b.pengarang, b.stok, antrean_str))
        
        # Update teks info stack riwayat terbaru
        riwayat = self.kontrol.riwayat_stack.get_all()
        if riwayat:
            self.lbl_riwayat.config(text=f"Buku Terakhir Diinput (Stack): {riwayat[0]}")

    def aksi_tambah(self):
        sukses, pesan = self.kontrol.tambah_buku(self.ent_id.get(), self.ent_judul.get(), self.ent_pengarang.get(), self.ent_stok.get())
        if sukses: messagebox.showinfo("Sukses", pesan)
        else: messagebox.showerror("Error", pesan)
        self.refresh_tabel()

    def aksi_update(self):
        sukses, pesan = self.kontrol.edit_buku(self.ent_id.get(), self.ent_judul.get(), self.ent_pengarang.get(), self.ent_stok.get())
        if sukses: messagebox.showinfo("Sukses", pesan)
        else: messagebox.showerror("Error", pesan)
        self.refresh_tabel()

    def aksi_hapus(self):
        sukses, pesan = self.kontrol.hapus_buku(self.ent_id.get())
        if sukses: messagebox.showinfo("Sukses", pesan)
        else: messagebox.showerror("Error", pesan)
        self.refresh_tabel()

    def aksi_cari(self):
        kw = self.ent_cari.get()
        if kw:
            hasil = cari_buku_by_keyword(self.kontrol.ambil_semua(), kw)
            self.refresh_tabel(hasil)
        else:
            self.refresh_tabel()

    def aksi_urutkan(self):
        buku_terurut = urutkan_buku_by_judul(self.kontrol.ambil_semua())
        self.refresh_tabel(buku_terurut)

    def aksi_pinjam(self):
        id_b = self.ent_id.get()
        nama = self.ent_peminjam.get()
        if not id_b:
            messagebox.showerror("Error", "Pilih atau ketik ID Buku terlebih dahulu!")
            return
        sukses, pesan = self.kontrol.pinjam_buku(id_b, nama)
        if sukses: messagebox.showinfo("Info Transaksi", pesan)
        else: messagebox.showerror("Error", pesan)
        self.refresh_tabel()