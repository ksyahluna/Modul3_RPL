import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_view import BukuView


class BukuController:
    def __init__(self, user_role="anggota"):
        self.user_role = user_role
        self.model = BukuModel()
        self.view = BukuView()

        # Menampilkan informasi role pada judul jendela aplikasi
        self.view.title(f"Sistem Manajemen Perpustakaan - Mode: {self.user_role.upper()}")

        # Binding tombol simpan
        self.view.btn_simpan.configure(command=self.simpan_data)

        # OTORISASI: Jika bukan admin, nonaktifkan form input dan tombol simpan
        if self.user_role != "admin":
            self.view.btn_simpan.configure(state="disabled", text="Akses Terkunci (Khusus Admin)")
            self.view.entry_judul.configure(state="disabled")
            self.view.entry_penulis.configure(state="disabled")
            self.view.entry_tahun.configure(state="disabled")

        self.muat_data_tabel()

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        data_buku = self.model.get_all_buku()
        for buku in data_buku:
            self.view.tabel.insert(
                "", "end",
                values=(
                    buku['id_buku'],
                    buku['judul'],
                    buku['penulis'],
                    buku['tahun_terbit']
                )
            )

    def simpan_data(self):
        # Proteksi ganda di Level Controller
        if self.user_role != "admin":
            messagebox.showerror("Akses Ditolak", "Anda tidak memiliki izin untuk menambah data!")
            return

        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        if self.model.create_buku(judul, penulis, tahun):
            messagebox.showinfo("Sukses", "Data buku berhasil disimpan!")
            self.view.entry_judul.delete(0, 'end')
            self.view.entry_penulis.delete(0, 'end')
            self.view.entry_tahun.delete(0, 'end')
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Gagal menyimpan data.")

    def run(self):
        self.view.mainloop()

    def pilih_data(self, event=None):
        # Mengambil baris tabel yang dipilih
        pilihan = self.view.tabel.selection()

        if not pilihan:
            return

        # Mengambil nilai dari baris yang dipilih
        data = self.view.tabel.item(pilihan[0], "values")

        # Memasukkan data terpilih ke dalam form
        self.view.entry_judul.delete(0, 'end')
        self.view.entry_judul.insert(0, data[1])

        self.view.entry_penulis.delete(0, 'end')
        self.view.entry_penulis.insert(0, data[2])

        self.view.entry_tahun.delete(0, 'end')
        self.view.entry_tahun.insert(0, data[3])

    def update_data(self):
        # Mengambil baris tabel yang dipilih
        pilihan = self.view.tabel.selection()

        if not pilihan:
            messagebox.showwarning(
                "Peringatan",
                "Pilih data buku yang ingin diperbarui!"
            )
            return

        # Mengambil id_buku dari baris yang dipilih
        data = self.view.tabel.item(pilihan[0], "values")
        id_buku = data[0]

        # Mengambil data terbaru dari form
        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        # Validasi form kosong
        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom form harus diisi!"
            )
            return

        # Mengirim perubahan data ke Model
        berhasil = self.model.update_buku(
            id_buku, judul, penulis, tahun
        )

        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data buku berhasil diperbarui!"
            )

            # Memuat ulang tabel
            self.muat_data_tabel()

            # Membersihkan form input
            self.view.entry_judul.delete(0, 'end')
            self.view.entry_penulis.delete(0, 'end')
            self.view.entry_tahun.delete(0, 'end')
        else:
            messagebox.showerror(
                "Error",
                "Terjadi kesalahan saat memperbarui data."
            )

    def hapus_data(self):
        # Mengambil baris tabel yang dipilih
        pilihan = self.view.tabel.selection()

        if not pilihan:
            messagebox.showwarning(
                "Peringatan",
                "Pilih data buku yang ingin dihapus!"
            )
            return

        # Mengambil id_buku dari baris yang dipilih
        data = self.view.tabel.item(pilihan[0], "values")
        id_buku = data[0]

        # Meminta konfirmasi sebelum menghapus
        konfirmasi = messagebox.askyesno(
            "Konfirmasi",
            "Apakah Anda yakin ingin menghapus data buku ini?"
        )

        if not konfirmasi:
            return

        # Mengirim id_buku ke Model untuk dihapus
        berhasil = self.model.delete_buku(id_buku)

        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data buku berhasil dihapus!"
            )

            # Memuat ulang tabel
            self.muat_data_tabel()

            # Membersihkan form input
            self.view.entry_judul.delete(0, 'end')
            self.view.entry_penulis.delete(0, 'end')
            self.view.entry_tahun.delete(0, 'end')
        else:
            messagebox.showerror(
                "Error",
                "Terjadi kesalahan saat menghapus data."
            )

    # Fungsi untuk menjalankan aplikasi
    def run(self):
        self.view.mainloop()
