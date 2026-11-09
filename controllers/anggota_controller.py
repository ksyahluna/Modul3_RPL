import tkinter.messagebox as messagebox
from models.anggota_model import AnggotaModel
from view.anggota_view import AnggotaView


class AnggotaController:
    def __init__(self):
        # Inisialisasi Model dan View
        self.model = AnggotaModel()
        self.view = AnggotaView()

        # Menghubungkan tombol dengan fungsi Controller
        self.view.btn_simpan.configure(
            command=self.simpan_data
        )
        self.view.btn_bersihkan.configure(
            command=self.bersihkan_form
        )

        # Memuat data anggota dari database
        self.muat_data_tabel()

    def muat_data_tabel(self):
        # Mengosongkan tabel terlebih dahulu
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        # Mengambil data dari database
        data_anggota = self.model.get_all_anggota()

        # Menampilkan data ke tabel
        for anggota in data_anggota:
            self.view.tabel.insert(
                "",
                "end",
                values=(
                    anggota["nama"],
                    anggota["alamat"]
                )
            )

    def simpan_data(self):
        # Mengambil data dari form
        nama = self.view.entry_nama.get().strip()
        alamat = self.view.entry_alamat.get().strip()

        # Validasi form
        if not nama or not alamat:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom form harus diisi!"
            )
            return

        # Menyimpan data melalui Model
        berhasil = self.model.create_anggota(nama, alamat)

        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data anggota berhasil disimpan!"
            )
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Data anggota gagal disimpan."
            )

    def bersihkan_form(self):
        self.view.entry_nama.delete(0, "end")
        self.view.entry_alamat.delete(0, "end")

    def run(self):
        self.view.mainloop()


if __name__ == "__main__":
    app = AnggotaController()
    app.run()
