# 🎵 SONARA — Music Playlist Manager

Aplikasi manajemen playlist musik berbasis desktop yang dikembangkan menggunakan **Python** dan **PySide6**. Proyek ini menerapkan struktur data **Doubly Linked List** untuk mengelola antrean lagu secara efisien dan dinamis.

---

## 👥 Anggota Kelompok 3
Penyusun proyek ini adalah mahasiswa Informatika Angkatan 2025:

| No | Nama | NPM |
|:---:|:---|:---:|
| 1 | **Tryanda Finoza Dewantara** | `G1A025017` |
| 2 | **Abdillah Siraj Al Haqqi** | `G1A025021` |
| 3 | **Daifullah Haffizh Farrash** | `G1A025041` |
| 4 | **Royana Dwi Rohmah** | `G1A025045` |
| 5 | **Sri Wahyuni** | `G1A025047` |

---

## 🚀 Fitur Aplikasi
Aplikasi ini dilengkapi dengan berbagai fungsionalitas utama:
* ➕ **Insert Lagu**: Menambah data lagu ke akhir playlist.
* 🗑️ **Delete Lagu**: Menghapus lagu tertentu berdasarkan judul yang dipilih di tabel.
* 🔍 **Search**: Mencari lagu berdasarkan Judul, Penyanyi, atau Genre.
* 📊 **Sort**: Mengurutkan playlist secara alfabetis (A-Z) menggunakan *Bubble Sort*.
* ⏭️ **Navigation**: Navigasi baris tabel secara berurutan (*Next/Previous*).

---

## 🛠️ Penjelasan Teknis

### 1. Struktur Data (`TubesKel3.py`)
Inti dari aplikasi ini adalah **Doubly Linked List**. Setiap lagu disimpan dalam sebuah `Node` yang memiliki dua pointer (`prev` dan `next`). 
* **Keunggulan**: Memungkinkan aplikasi untuk melakukan transversal dua arah dan mempermudah penghapusan data tanpa harus menggeser seluruh elemen seperti pada array biasa.

### 2. Antarmuka Pengguna (`main.ui` & `main_ui.py`)
Didesain menggunakan **Qt Designer** dengan sentuhan modern:
* **Dark Theme**: Menggunakan palet warna *Midnight Blue* (#1a1a2e) dan *Emerald Green* (#00c85d).
* **Responsif**: Layout menggunakan `QHBoxLayout` agar panel kiri (kontrol) dan panel kanan (tabel) tetap proporsional.

### 3. Logika Utama (`main.py`)
Berperan sebagai *Controller* yang menghubungkan UI dengan struktur data. Menangani validasi input, pembaruan `QTableWidget`, dan interaksi pengguna melalui tombol-tombol yang tersedia.

---

## 💻 Cara Instalasi & Menjalankan
Pastikan Anda telah menginstal Python di sistem Anda, kemudian ikuti langkah berikut:

1. **Clone Repositori**
   ```bash
   git clone [https://github.com/username/Tubes_PSDA_Kelompok3.git](https://github.com/username/Tubes_PSDA_Kelompok3.git)
