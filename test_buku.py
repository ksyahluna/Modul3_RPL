from unittest.mock import MagicMock
from models.buku_model import BukuModel


def test_create_buku_berhasil():
    # Menginisialisasi Model
    model = BukuModel()

    # Memanipulasi koneksi database agar tidak mengakses database asli
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor

    # Melakukan eksekusi fungsi
    hasil = model.create_buku("Buku Testing", "Penulis QA", 2026)

    # Memverifikasi fungsi mengembalikan nilai True
    assert hasil is True

    # Memverifikasi perintah SQL benar-benar dipanggil
    mock_cursor.execute.assert_called_once()

    # Memverifikasi perintah commit dipanggil
    model.conn.commit.assert_called_once()
