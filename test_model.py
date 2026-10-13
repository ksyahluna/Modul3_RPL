from models.buku_model import BukuModel

model = BukuModel()

# 1. Menguji fungsi Create (menambah buku baru)
print("\nMenambahkan data buku...")
model.create_buku("Pemrograman Python MVC", "Guido van Rossum", 2023)
print("Data berhasil disimpan ke Laravel MySQL!")

# 2. Menguji fungsi Read (menampilkan data)
print("\n=== Daftar Buku ===")
daftar_buku = model.get_all_buku()
for buku in daftar_buku:
    print(f"[{buku['id_buku']}] {buku['judul']} - {buku['penulis']} ({buku['tahun_terbit']})")

# 3. Menguji fungsi Update
print("\nMengubah data buku...")
model.update_buku(
    1,
    "Pemrograman Python",
    "Guido van Rossum",
    2024
)
print("Data buku berhasil diubah!")

# 4. Menguji fungsi Delete
print("\nMenghapus data buku...")
model.delete_buku(10)
print("Data buku berhasil dihapus!")

# 5. Menampilkan data setelah Update dan Delete
print("\n=== Daftar Buku Setelah Perubahan ===")
daftar_buku = model.get_all_buku()

for buku in daftar_buku:
    print(
        f"[{buku['id_buku']}] "
        f"{buku['judul']} - "
        f"{buku['penulis']} "
        f"({buku['tahun_terbit']})"
    )


from models.anggota_model import AnggotaModel

anggota = AnggotaModel()

#1. Menguji fungsi Create
print("\nMenambahkan data anggota...")
anggota.create_anggota(
    "Kissya",
    "Palu"
)
print("Data anggota berhasil disimpan!")

#2. Menguji fungsi Read
print("\n=== Daftar Anggota ===")

daftar_anggota = anggota.get_all_anggota()

for data in daftar_anggota:
    print(
        f"[{data['id_anggota']}] "
        f"{data['nama']} - "
        f"{data['alamat']}"
    )