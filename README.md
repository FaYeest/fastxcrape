# 🐦 FastXcrape

Aplikasi ini memungkinkan Anda untuk melakukan **scraping cuitan dari Twitter secara otomatis** berdasarkan kata kunci tertentu menggunakan antarmuka grafis (GUI). Hasil cuitan akan disimpan dalam file `.csv`.

> ⚠️ **Catatan:** Aplikasi ini membutuhkan token autentikasi Twitter aktif dan koneksi internet.

---

## 📦 Fitur Utama

- Antarmuka pengguna grafis sederhana (dengan Tkinter)
- Scraping tanpa membuka jendela browser (headless)
- Progres scraping ditampilkan secara real-time
- Hasil scraping otomatis disimpan dalam file `CSV`

---

## 🛠️ Instalasi & Persiapan

### 1. **Clone/Download Proyek**
Unduh file `scrape_twitter.py` atau clone repo ini jika tersedia di GitHub.

### 2. **Pasang Python & Modul**
Pastikan Python sudah terinstal, lalu buka terminal dan jalankan:

```bash
pip install undetected-chromedriver selenium
```

### 3. **Jalankan Aplikasinya**
Buka terminal dan jalankan:

```bash
python scrape_twitter.py
```

---

## ▶️ Cara Menggunakan
1. Buka aplikasi: jalankan `scrape_twitter.py` dengan cara di cmd/terminal:
   ```bash
   python scrape.twitter.py
   ```
2. Isi kolom-kolom berikut:
  -  🔐 Auth Token: Masukkan token autentikasi Twitter Anda (didapatkan melalui login dengan browser dan melihat cookie auth_token)
  -  🔍 Kata Kunci Pencarian: Kata/frasa untuk mencari tweet (contoh: makanan, jalanan, ataupun politik)
  -  🔢 Jumlah Cuitan: Jumlah maksimal cuitan yang ingin diambil (Disarankan tidak usah mengambil sampai 10 ribu tolong berikan yang masuk diakal :) for your best experiences)
3. Klik tombol "Mulai Scraping"
4. Tunggu hingga proses selesai. File CSV akan tersimpan otomatis pada folder yang sama disimpannya aplikasi `scrape_twitter.py` (file bernama: data_twitter.csv, data_twitter_1.csv, dst.)

---

## ✏️ Cara Modifikasi

### **Ubah Lokasi Simpan File**
Cari bagian kode berikut di `scrape_twitter.py`:
```bash
base_name = "data_twitter"
```

### **Ubah ke nama lain sesuai keinginan, misal:**
```bash
base_name = "hasil_scraping_bakso"
```

## Tampilkan Browser Saat Scraping
### **Hapus atau beri komentar (#) baris berikut agar browser muncul saat scraping:**
```bash
options.add_argument("--headless")
```

## Tambahkan Kolom Tanggal
Untuk menambahkan tanggal tweet, Anda perlu memodifikasi bagian pengambilan data tweet dan menambahkan kolom pada CSV. Hal ini membutuhkan penyesuaian lanjutan dengan struktur HTML Twitter. (Nanti saya update jika ada waktu senggang)

---

## ❓ FAQ
Q: Dapat auth token dari mana?
A: Buka `twitter.com/x.com` di browser, login, lalu gunakan `DevTools (F12)` → `tab Application` → `Cookies` → `cari auth_token`.

Q: Apakah aplikasi ini aman?
A: Aplikasi ini berjalan lokal di komputer Anda, tidak mengirim data keluar.

Q: Apakah ini resmi dari Twitter?
A: Tidak. Ini adalah tool pihak ketiga yang menggunakan scraping.

---

## 🧑‍💻 Developer
- Dibuat dengan Python, Selenium, dan Tkinter
- Modul khusus: undetected_chromedriver untuk bypass deteksi bot

---

## 📄 Lisensi
Proyek ini bebas digunakan untuk edukasi dan eksperimen pribadi. Tidak untuk penggunaan komersial tanpa izin.

---

## ❤️ Support Me :)
Jika proyek ini bermanfaat, silakan beri ⭐ atau bagikan ke teman Anda!
