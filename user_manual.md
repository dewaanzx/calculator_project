# Kalkulator LSP UNS

## Pendahuluan
Selamat datang di aplikasi Kalkulator LSP UNS. Aplikasi ini adalah kalkulator berbasis GUI yang memungkinkan Anda untuk melakukan operasi matematika dasar seperti penjumlahan, pengurangan, perkalian, dan pembagian. Aplikasi ini juga menyimpan riwayat kalkulasi Anda ke dalam database dan memungkinkan Anda untuk melihat riwayat tersebut.

## Persiapan dan Instalasi

1. **Persyaratan Sistem:**
   - Python 3.x
   - MySQL Server
   - Library Python: `customtkinter`, `mysql-connector-python`

2. **Instalasi Pustaka yang Dibutuhkan:**
   ```bash
   pip install customtkinter mysql-connector-python
Konfigurasi Database:

Buat database MySQL dengan nama calculator_db.
Pastikan MySQL Server berjalan dan dapat diakses dengan kredensial yang sesuai (host: localhost, user: root, password: ``, database: calculator_db).
Menjalankan Aplikasi:

Simpan kode aplikasi dalam file dengan ekstensi .py, misalnya calculator_app.py.
Jalankan aplikasi dengan perintah berikut:

python calculator.py
Penggunaan Aplikasi
Antarmuka Pengguna:
Layar Utama:

Layar utama terdiri dari label untuk menampilkan ekspresi yang sedang dibangun dan hasil kalkulasi.
Tombol-tombol untuk operasi matematika dasar dan kontrol kalkulator.
Tombol Utama:

AC: Menghapus ekspresi saat ini. Jika ditekan dua kali berturut-turut, akan menghapus semua riwayat.
<: Menghapus karakter terakhir dari ekspresi.
%: Mengubah nilai menjadi persen.
/: Operasi pembagian.
x: Operasi perkalian.
-: Operasi pengurangan.
+: Operasi penjumlahan.
=: Menghitung hasil ekspresi.
0-9: Angka untuk membangun ekspresi.
.: Titik desimal.
Tombol Riwayat:

Riwayat: Membuka jendela baru yang menampilkan riwayat kalkulasi. Setiap entri riwayat dapat ditekan untuk mengisi kembali ekspresi di layar utama.
Melakukan Kalkulasi:

Masukkan ekspresi matematika menggunakan tombol yang tersedia.
Tekan tombol = untuk menghitung hasil ekspresi.
Hasil kalkulasi akan ditampilkan di layar.
Menghapus Ekspresi dan Riwayat:
Tekan tombol AC untuk menghapus ekspresi saat ini.
Tekan tombol AC dua kali berturut-turut untuk menghapus semua riwayat kalkulasi.
Tekan tombol < untuk menghapus karakter terakhir dari ekspresi.
Melihat dan Menggunakan Riwayat Kalkulasi:
Tekan tombol Riwayat untuk membuka jendela riwayat.
Riwayat kalkulasi akan ditampilkan dalam urutan waktu dengan ekspresi dan hasilnya.
Klik pada entri riwayat untuk mengisi kembali ekspresi di layar utama.

Fitur Tambahan
Mode Gelap: Aplikasi ini menggunakan mode gelap secara default untuk kenyamanan mata pengguna.
Desain Responsif: Antarmuka pengguna telah diatur untuk menyesuaikan ukuran komponen agar sesuai dengan layar dan memastikan pengalaman pengguna yang optimal.
Penanganan Kesalahan
Jika terjadi kesalahan saat menghitung ekspresi, pastikan ekspresi yang dimasukkan valid.
Jika aplikasi tidak dapat terhubung ke database, periksa konfigurasi MySQL Server dan pastikan database calculator_db sudah dibuat dan dapat diakses.

Penutup
Terima kasih telah menggunakan aplikasi Kalkulator LSP UNS. Jika Anda memiliki pertanyaan atau memerlukan bantuan lebih lanjut, jangan ragu untuk menghubungi pengembang aplikasi.
