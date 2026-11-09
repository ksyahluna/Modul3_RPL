from models.buku_model import BukuModel

model = BukuModel()

# 1. Menguji Fungsi Create (menambahkan buku baru)
print("Menambahkan data buku...")
model.create_buku("Pemrograman Python MVC", "Guido van Rossum", 2023)
print("Data berhasil disimpan ke Laragon MySQL!")

#Menguji Fungsi Read (menampilkan data)
print("\n=== Data Buku ===")
daftar_buku = model.get_all_buku()
for buku in daftar_buku:
    print(f"[{buku['id_buku']}] {buku['judul']} - {buku['penulis']} ({buku['tahun_terbit']})")

# # 2. Menguji Fungsi Update
# print("\n=== Update Data Buku ===")
# if model.update_buku(1, "Harry Potter dan Batu Bertuah", "J.K Rowling", 1997):
#     print("Data buku berhasil diupdate!")

# print("\n=== Data Buku Setelah Update ===")
# daftar_buku = model.get_all_buku()
# for buku in daftar_buku:
#     print(f"[{buku['id_buku']}] {buku['judul']} - {buku['penulis']} ({buku['tahun_terbit']})")

# # 3. Menguji Fungsi Delete
# print("\n=== Delete Data Buku ===")
# if model.delete_buku(3):
#     print("Data buku berhasil dihapus!")

# print("\n=== Data Buku Setelah Delete ===")
# daftar_buku = model.get_all_buku()
# for buku in daftar_buku:
#     print(f"[{buku['id_buku']}] {buku['judul']} - {buku['penulis']} ({buku['tahun_terbit']})")

# from models.anggota_model import AnggotaModel

# model = AnggotaModel()

# # 1. Menguji fungsi Create
# print("Menambahkan data anggota...")
# model.create_anggota("Maulidyah", "Tondo")
# print("Data anggota berhasil disimpan!")

# # 2. Menguji fungsi Read
# print("\n=== Daftar Anggota ===")
# daftar_anggota = model.get_all_anggota()
# for anggota in daftar_anggota:
#     print(f"[{anggota['id_anggota']}] {anggota['nama']} - {anggota['alamat']}")