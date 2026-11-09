# Pendaftaran Kegiatan Mahasiswa

Praktikum Sesi 11 — Advanced Widgets dan Event Handling.
Pengembangan dari formulir identitas mahasiswa menggunakan Python Tkinter.

## Tujuan
Membangun GUI untuk menerima pendaftaran kegiatan mahasiswa, memvalidasi input,
menangani interaksi pengguna, dan menampilkan ringkasan pendaftaran.

## Fitur
- Entry nama dan NIM (opsional), Combobox program studi.
- Radiobutton jenis kelamin dan Checkbutton untuk memilih satu atau lebih kegiatan.
- Listbox katalog kegiatan; klik item untuk membaca deskripsi. Pilihan pendaftaran
  ditentukan oleh Checkbutton, bukan sorotan pada Listbox.
- Text untuk alasan mengikuti kegiatan dan ringkasan dengan scrollbar.
- Submit, Reset, validasi, dan notifikasi Messagebox.
- Menu File > Keluar dan Bantuan > About (jendela Toplevel).
- Enter menjalankan Submit; Shift+Enter membuat baris baru pada kolom alasan.
- Frame, grid, dan pack digunakan pada container terpisah.

Nama, program studi, jenis kelamin, dan minimal satu kegiatan wajib diisi.
NIM dan alasan boleh kosong. Data hanya berada di memori selama aplikasi berjalan;
tidak ada database atau penyimpanan permanen.

## Cara menjalankan
1. Pasang Python 3 dengan komponen Tcl/Tk (umumnya tersedia pada installer Python Windows).
2. Ekstrak ZIP dan buka folder ini di VS Code.
3. Jalankan dari terminal:
   ```bash
   python main.py
   ```
   Di Windows, bisa menggunakan `py main.py` jika perintah `python` tidak tersedia.
4. Isi formulir, centang kegiatan, lalu klik Submit atau tekan Enter.
5. Tutup notifikasi untuk membaca ringkasan. Reset mengosongkan semua input dan hasil.

Tidak perlu menginstal paket dari pip. Jika Tkinter tidak tersedia pada Linux,
pasang paket python3-tk dari pengelola paket sistem.

## Berkas pengumpulan
- main.py: program utama.
- README.md: tujuan, fitur, dan cara menjalankan.
- screenshot.png: ambil screenshot saat aplikasi berjalan dan menampilkan ringkasan.
  Jika belum ada pada paket ini, jalankan aplikasi di komputer sendiri, isi formulir,
  tutup notifikasi berhasil, lalu gunakan Win+Shift+S dan simpan sebagai screenshot.png.

Unggah ketiga berkas ke repository GitHub bernama `praktikum-tkinter-sesi-11`.
