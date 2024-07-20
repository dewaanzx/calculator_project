# Testing Kalkulator LSP UNS

Dokumentasi ini menjelaskan cara melakukan testing pada kelas `HistoryManager` yang merupakan bagian dari aplikasi Kalkulator LSP UNS. Testing dilakukan menggunakan framework `unittest` dan `unittest.mock` untuk membuat mock objek.

## Pendahuluan

Testing adalah proses penting untuk memastikan bahwa setiap komponen aplikasi berfungsi sesuai dengan yang diharapkan. Pada aplikasi ini, kami melakukan unit testing pada kelas `HistoryManager` yang bertanggung jawab untuk mengelola riwayat kalkulasi.

## Struktur File

```plaintext
.
├── calculator.py       # File utama aplikasi
├── user_manual.md      # Dokumentasi user manual
├── testing.md          # Dokumentasi testing (file ini)
└── test_calculator.py  # File script untuk unit testing

Menjalankan Unit Testing
Pastikan semua dependensi telah diinstal:

pip install customtkinter mysql-connector-python
Jalankan File test_calculator.py
Jalankan unit testing dengan perintah:

python test_calculator.py
Penjelasan Unit Test
TestHistoryManager
setUp: Metode ini dipanggil sebelum setiap unit test dijalankan. Ini membuat mock objek database dan cursor, kemudian membuat instance HistoryManager dengan mock database.

test_fetch_riwayat: Menguji apakah metode fetch_riwayat mengambil data riwayat dengan benar dari database dan mengembalikan hasil yang sesuai.

test_insert_riwayat: Menguji apakah metode insert_riwayat menyimpan entri baru ke dalam database dengan benar.

test_delete_all_riwayat: Menguji apakah metode delete_all_riwayat menghapus semua entri riwayat dari database dan mengosongkan daftar riwayat lokal.

test_delete_all_riwayat_when_empty: Menguji apakah metode delete_all_riwayat berfungsi dengan benar ketika daftar riwayat kosong.

test_fetch_riwayat_after_insert: Menguji apakah metode fetch_riwayat mengambil data riwayat yang diperbarui setelah menambahkan entri baru ke database.

Penutup
Dokumentasi ini menjelaskan langkah-langkah untuk melakukan unit testing pada aplikasi Kalkulator LSP UNS. Testing yang tepat memastikan bahwa setiap bagian dari aplikasi berfungsi dengan benar dan membantu mengidentifikasi masalah sejak dini. Terima kasih telah menggunakan aplikasi ini dan menjalankan tes dengan seksama.
