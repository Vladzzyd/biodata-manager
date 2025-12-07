# Biodata Manager (Python CLI)

Program sederhana berbasis terminal untuk mengelola biodata. Dibuat menggunakan Python dan cocok sebagai latihan dasar logika, input–output, serta manajemen data.

## Fitur Utama
- Input biodata lengkap (nama, umur, alamat, nomor telepon, email)
- Menampilkan biodata terbaru
- Menampilkan seluruh riwayat biodata
- Mengedit biodata berdasarkan field
- Menghapus data berdasarkan nomor indeks
- Validasi input (angka, nomor telepon, dan lainnya)
- Tampilan CLI berwarna menggunakan ANSI escape codes
- Border dan tampilan rapi untuk memudahkan pembacaan

## Struktur Program
Program berjalan langsung di terminal tanpa file tambahan.  
Semua data disimpan sementara di dalam list Python (`riwayat_biodata`).

## Cara Menggunakan
1. Jalankan program:
2. Pilih fungsi:
- `input`  → memasukkan biodata baru
- `show`   → menampilkan riwayat biodata
- `delete` → menghapus data
- `edit`   → mengedit field tertentu
- `quit`   → keluar dari program
3. Ikuti instruksi di terminal.
4. Pastikan input mengikuti format yang diminta (misalnya nomor telepon harus angka).

## Teknologi
- Python 3.x
- ANSI Escape Colors

## Tujuan Dibuat
Project ini dibuat sebagai latihan pemrograman Python fundamental:
- Fungsi
- Perulangan
- Validasi input
- Manipulasi list & dictionary
- Aplikasi CLI interaktif

## Pengembangan Ke Depan
- Menyimpan biodata ke file JSON/CSV
- Menambah fitur pencarian
- Membuat versi GUI (Tkinter / PyQt)
- Menambahkan sistem login sederhana
