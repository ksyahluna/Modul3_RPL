import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_view import BukuView


class BukuController:
    def __init__(self, user_role="anggota"):
        self.user_role = user_role
        self.model = BukuModel()
        self.view = BukuView()

        # Menampilkan role pada judul aplikasi
        self.view.title(
            f"Aplikasi Perpustakaan - {self.user_role.upper()}"
        )

        # Menghubungkan tombol dengan fungsi
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_update.configure(command=self.update_data)
        self.view.btn_hapus.configure(command=self.hapus_data)
        self.view.btn_logout.configure(command=self.logout)

        # Menghubungkan tabel dengan fungsi pilih data
        self.view.tabel.bind(
            "<<TreeviewSelect>>",
            self.pilih_data
        )

        # Mengatur hak akses berdasarkan role
        if self.user_role != "admin":
            self.view.btn_simpan.configure(state="disabled")
            self.view.btn_update.configure(state="disabled")
            self.view.btn_hapus.configure(state="disabled")

            self.view.entry_judul.configure(state="disabled")
            self.view.entry_penulis.configure(state="disabled")
            self.view.entry_tahun.configure(state="disabled")

        # Menampilkan data buku
        self.muat_data_tabel()

    # Menampilkan data buku ke tabel
    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        data_buku = self.model.get_all_buku()

        for buku in data_buku:
            self.view.tabel.insert(
                "",
                "end",
                values=(
                    buku["id_buku"],
                    buku["judul"],
                    buku["penulis"],
                    buku["tahun_terbit"]
                )
            )

    # Menyimpan data buku
    def simpan_data(self):
        if self.user_role != "admin":
            messagebox.showerror(
                "Akses Ditolak",
                "Anda tidak memiliki izin untuk menambahkan buku!"
            )
            return

        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan",
                "Semua data harus diisi!"
            )
            return

        try:
            berhasil = self.model.create_buku(
                judul,
                penulis,
                tahun
            )

            if berhasil:
                messagebox.showinfo(
                    "Berhasil",
                    "Data buku berhasil ditambahkan!"
                )
                self.muat_data_tabel()
                self.kosongkan_form()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Memilih data dari tabel
    def pilih_data(self, event):
        selected = self.view.tabel.selection()

        if selected:
            data = self.view.tabel.item(
                selected[0],
                "values"
            )

            self.kosongkan_form()

            self.view.entry_judul.insert(0, data[1])
            self.view.entry_penulis.insert(0, data[2])
            self.view.entry_tahun.insert(0, data[3])

    # Memperbarui data buku
    def update_data(self):
        if self.user_role != "admin":
            messagebox.showerror(
                "Akses Ditolak",
                "Anda tidak memiliki izin untuk memperbarui buku!"
            )
            return

        selected = self.view.tabel.selection()

        if not selected:
            messagebox.showwarning(
                "Peringatan",
                "Pilih data buku terlebih dahulu!"
            )
            return

        data = self.view.tabel.item(
            selected[0],
            "values"
        )

        id_buku = data[0]

        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan",
                "Semua data harus diisi!"
            )
            return

        try:
            berhasil = self.model.update_buku(
                id_buku,
                judul,
                penulis,
                tahun
            )

            if berhasil:
                messagebox.showinfo(
                    "Berhasil",
                    "Data buku berhasil diperbarui!"
                )
                self.muat_data_tabel()
                self.kosongkan_form()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Menghapus data buku
    def hapus_data(self):
        if self.user_role != "admin":
            messagebox.showerror(
                "Akses Ditolak",
                "Anda tidak memiliki izin untuk menghapus buku!"
            )
            return

        selected = self.view.tabel.selection()

        if not selected:
            messagebox.showwarning(
                "Peringatan",
                "Pilih data buku terlebih dahulu!"
            )
            return

        data = self.view.tabel.item(
            selected[0],
            "values"
        )

        id_buku = data[0]

        konfirmasi = messagebox.askyesno(
            "Konfirmasi",
            "Apakah Anda yakin ingin menghapus buku ini?"
        )

        if konfirmasi:
            try:
                berhasil = self.model.delete_buku(id_buku)

                if berhasil:
                    messagebox.showinfo(
                        "Berhasil",
                        "Data buku berhasil dihapus!"
                    )
                    self.muat_data_tabel()
                    self.kosongkan_form()

            except Exception as e:
                messagebox.showerror("Error", str(e))

    # Mengosongkan form input
    def kosongkan_form(self):
        self.view.entry_judul.delete(0, "end")
        self.view.entry_penulis.delete(0, "end")
        self.view.entry_tahun.delete(0, "end")

    # Logout dan kembali ke halaman login
    def logout(self):
        konfirmasi = messagebox.askyesno(
            "Logout",
            "Apakah Anda yakin ingin logout?"
        )

        if konfirmasi:
            self.view.destroy()

            from controllers.auth_controller import AuthController
            app = AuthController()
            app.run()

    # Menjalankan aplikasi
    def run(self):
        self.view.mainloop()