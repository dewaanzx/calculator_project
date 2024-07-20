import unittest
from unittest.mock import MagicMock

class RiwayatManager:
    def __init__(self, db):
        self.db = db  # Menyimpan referensi ke objek database
        self.cursor = self.db.cursor()  # Membuat objek cursor untuk eksekusi query
        self.histories = []  # Inisialisasi histories untuk unit test

    def fetch_riwayat(self):
        self.cursor.execute("SELECT expression, result FROM riwayat ORDER BY id DESC")  # Menjalankan query untuk mengambil riwayat
        return self.cursor.fetchall()  # Mengembalikan hasil query sebagai daftar tuple

    def insert_riwayat(self, expression, result):
        self.cursor.execute("INSERT INTO riwayat (expression, result) VALUES (%s, %s)", (expression, result))  # Menyimpan entri riwayat ke database
        self.db.commit()  # Menyimpan perubahan ke database

    def delete_all_riwayat(self):
        self.cursor.execute("DELETE FROM riwayat")  # Menghapus semua entri riwayat dari database
        self.db.commit()  # Menyimpan perubahan ke database
        self.histories = []  # Mengosongkan daftar riwayat lokal
        self.update_riwayat_expression('')  # Memperbarui tampilan expression riwayat
        self.update_expression('')  # Memperbarui tampilan expression kalkulasi

    def update_riwayat_expression(self, expression):
        # Dummy implementation for unit test
        pass

    def update_expression(self, expression):
        # Dummy implementation for unit test
        pass

class TestRiwayatManager(unittest.TestCase):
    def setUp(self):
        self.mock_db = MagicMock()  # Membuat mock objek database
        self.mock_cursor = MagicMock()  # Membuat mock objek cursor
        self.mock_db.cursor.return_value = self.mock_cursor  # Mengatur cursor mock untuk mengembalikan objek cursor mock
        self.riwayat_manager = RiwayatManager(self.mock_db)  # Membuat instance RiwayatManager dengan mock database

    def test_fetch_riwayat(self):
        expected_result = [("1+1", "2"), ("2+2", "4")]  # Data yang diharapkan
        self.mock_cursor.fetchall.return_value = expected_result  # Mengatur mock cursor untuk mengembalikan data yang diharapkan

        result = self.riwayat_manager.fetch_riwayat()  # Memanggil metode fetch_riwayat

        self.mock_cursor.execute.assert_called_once_with("SELECT expression, result FROM riwayat ORDER BY id DESC")  # Memastikan query yang benar dipanggil
        self.assertEqual(result, expected_result)  # Memastikan hasil yang dikembalikan sesuai dengan data yang diharapkan

    def test_insert_riwayat(self):
        expression = "3+3"  # Expression yang akan disimpan
        result = "6"  # Hasil kalkulasi

        self.riwayat_manager.insert_riwayat(expression, result)  # Memanggil metode insert_riwayat

        self.mock_cursor.execute.assert_called_once_with("INSERT INTO riwayat (expression, result) VALUES (%s, %s)", (expression, result))  # Memastikan query yang benar dipanggil
        self.mock_db.commit.assert_called_once()  # Memastikan commit database dipanggil

    def test_delete_all_riwayat(self):
        # Set up initial state
        self.riwayat_manager.histories = [("1+1", "2"), ("2+2", "4")]  # Menetapkan state awal riwayat

        self.riwayat_manager.delete_all_riwayat()  # Memanggil metode delete_all_riwayat

        self.mock_cursor.execute.assert_called_once_with("DELETE FROM riwayat")  # Memastikan query yang benar dipanggil
        self.mock_db.commit.assert_called_once()  # Memastikan commit database dipanggil
        self.assertEqual(self.riwayat_manager.histories, [])  # Memastikan histories telah dikosongkan

    def test_delete_all_riwayat_when_empty(self):
        # Set up initial state with empty riwayat
        self.riwayat_manager.histories = []  # Menetapkan state awal riwayat kosong

        self.riwayat_manager.delete_all_riwayat()  # Memanggil metode delete_all_riwayat

        self.mock_cursor.execute.assert_called_once_with("DELETE FROM riwayat")  # Memastikan query yang benar dipanggil
        self.mock_db.commit.assert_called_once()  # Memastikan commit database dipanggil
        self.assertEqual(self.riwayat_manager.histories, [])  # Memastikan histories tetap kosong

    def test_fetch_riwayat_after_insert(self):
        # Set up mock data
        self.mock_cursor.fetchall.return_value = [("1+1", "2"), ("2+2", "4")]  # Mengatur data riwayat awal
        self.riwayat_manager.insert_riwayat("5+5", "10")  # Menambahkan entri riwayat baru

        # Fetch riwayat and check if it includes the new entry
        expected_result = [("5+5", "10"), ("1+1", "2"), ("2+2", "4")]  # Data yang diharapkan setelah penambahan
        self.mock_cursor.fetchall.return_value = expected_result  # Mengatur mock cursor untuk mengembalikan data yang diharapkan

        result = self.riwayat_manager.fetch_riwayat()  # Memanggil metode fetch_riwayat

        self.mock_cursor.execute.assert_called_with("SELECT expression, result FROM riwayat ORDER BY id DESC")  # Memastikan query yang benar dipanggil
        self.assertEqual(result, expected_result)  # Memastikan hasil yang dikembalikan sesuai dengan data yang diharapkan

if __name__ == '__main__':
    unittest.main()  # Menjalankan semua tes
