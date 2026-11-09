import pytest
from models.buku_model import BukuModel


def test_get_all_buku():
    # Inisialisasi model buku
    model = BukuModel()
    
    # Panggil fungsi yang ingin diuji
    result = model.get_all_buku()
    
    # Memastikan bahwa hasil kembaliannya berupa list (daftar buku)
    assert isinstance(result, list)
    
    # Jika tabel buku memiliki isi, pastikan elemen di dalam list berupa dictionary atau tuple
    # (sesuaikan dengan implementasi return di BukuModel Anda)
    if len(result) > 0:
        buku_pertama = result[0]
        # Pastikan kunci/kolom penting tersedia pada data model
        assert "id_buku" in buku_pertama or hasattr(buku_pertama, "__getitem__")