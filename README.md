# Aplikasi Perpustakaan

## 1. Deskripsi Aplikasi

Aplikasi Perpustakaan merupakan aplikasi desktop berbasis Python yang digunakan untuk mengelola data buku. Aplikasi ini menggunakan CustomTkinter sebagai antarmuka pengguna dan MySQL sebagai database untuk menyimpan data.

Aplikasi ini memiliki sistem autentikasi dengan dua hak akses pengguna:

- **Admin/Petugas:** Dapat melihat, menambahkan, memperbarui, dan menghapus data buku.
- **Anggota/Mahasiswa:** Hanya dapat melihat daftar buku.

Pengembangan aplikasi menerapkan konsep arsitektur Model-View-Controller (MVC).

## 2. Struktur Direktori

```text
Modul3_RPL/
│
├── .github/
│   └── workflows/
│       └── ci_pipeline.yml
│
├── config/
│   └── database.py
│
├── controllers/
│   ├── auth_controller.py
│   └── buku_controller.py
│
├── models/
│   ├── user_model.py
│   └── buku_model.py
│
├── views/
│   ├── login_view.py
│   └── buku_view.py
│
├── test/
│   ├── test_auth.py
│   └── test_buku.py
│
├── main.py
├── test_model.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

### Penjelasan Struktur MVC

- **Models:** Mengelola data dan komunikasi dengan database MySQL.
- **Views:** Mengatur tampilan antarmuka aplikasi.
- **Controllers:** Menghubungkan Model dan View serta mengatur proses aplikasi.
- **Config:** Menyimpan konfigurasi koneksi database.
- **Test:** Menyimpan file pengujian aplikasi.
- **.github/workflows:** Menyimpan konfigurasi GitHub Actions untuk proses Continuous Integration.

## 3. Instalasi dan Konfigurasi

### A. Persyaratan

Sebelum menjalankan aplikasi, pastikan perangkat sudah memiliki:

- Python 3.11 atau versi yang sesuai dengan dependensi proyek.
- MySQL atau Laragon.
- Visual Studio Code.
- Git.

### B. Clone Repository

Buka terminal dan jalankan perintah berikut:

```bash
git clone https://github.com/ksyahluna/Modul3_RPL.git
```

Masuk ke direktori proyek:

```bash
cd Modul3_RPL
```

### C. Membuat Virtual Environment

Buat lingkungan virtual menggunakan perintah:

```bash
python -m venv env
```

Aktifkan virtual environment:

```bash
env\Scripts\activate
```

### D. Menginstal Dependensi

Instal seluruh library yang dibutuhkan aplikasi:

```bash
pip install -r requirements.txt
```

### E. Konfigurasi Database MySQL

1. Jalankan Laragon dan aktifkan MySQL.
2. Buka phpMyAdmin.
3. Buat database sesuai nama database yang digunakan pada file `config/database.py`.
4. Siapkan tabel `users`, `buku`, dan `peminjaman` sesuai struktur database proyek.
5. Sesuaikan host, username, password, dan nama database pada file `config/database.py`.

Pastikan database dan tabel sudah tersedia sebelum menjalankan aplikasi.

## 4. Cara Menjalankan Aplikasi

Pastikan virtual environment sudah aktif dan MySQL sedang berjalan.

Jalankan aplikasi menggunakan perintah:

```bash
python main.py
```

Aplikasi akan menampilkan halaman login. Masukkan username dan password yang telah terdaftar pada database.

## 5. Pengujian Aplikasi

Pengujian aplikasi dilakukan menggunakan Pytest untuk memastikan fungsi aplikasi berjalan dengan baik.

Jalankan perintah:

```bash
pytest -v
```

Pemeriksaan kualitas kode dilakukan menggunakan Flake8:

```bash
flake8 models/ controllers/ --count --select=E9,F63,F7,F82 --show-source --statistics
```

## 6. Continuous Integration (CI)

Proyek ini menggunakan GitHub Actions sebagai proses Continuous Integration.

Setiap terjadi `push` atau `pull request` ke branch `main`, sistem akan menjalankan beberapa tahapan:

1. Mengambil kode dari repository.
2. Menyiapkan lingkungan Python 3.11.
3. Menginstal dependensi proyek.
4. Menjalankan pemeriksaan kode menggunakan Flake8.
5. Menjalankan pengujian otomatis menggunakan Pytest.

Proses ini bertujuan untuk memastikan kode telah melewati pemeriksaan dan pengujian secara otomatis.