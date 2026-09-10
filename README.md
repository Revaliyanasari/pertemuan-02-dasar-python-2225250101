# Tugas Pertemuan 02 - Dasar Python

## Identitas Mahasiswa

- **Nama:** Reva Liyanasari
- **NIM:** 22252610101
- **Kelas:** 3A
- **Mata Kuliah:** Algoritma dan Pemrograman
- **Dosen Pengampu:** Dr. Aan Hendrayana, S.Si., M.Pd.

---

## 1. Tujuan Repositori

Repositori ini dibuat untuk menyimpan hasil latihan dan tugas Pertemuan 02 Mata Kuliah Algoritma dan Pemrograman. Materi yang dipelajari meliputi variabel, konstanta, tipe data, input-output, operator, serta dasar penggunaan Python di VS Code.

---

## 2. Daftar Berkas

### Latihan

1. **`01_biodata.py`**
   - Program untuk menerima data nama, NIM, kelas, dan tahun lahir, kemudian menampilkan biodata serta perkiraan umur.

2. **`02_persegi_panjang.py`**
   - Program untuk menghitung luas dan keliling persegi panjang.

3. **`03_konversi_suhu.py`**
   - Program untuk mengonversi suhu Celsius ke Fahrenheit dan Kelvin.

4. **`04_nilai_akhir.py`**
   - Program untuk menghitung nilai akhir berdasarkan bobot nilai tugas, UTS, dan UAS.

### Tugas Utama

**`kalkulator_koordinat.py`**

Program untuk menghitung perubahan koordinat, jarak antara dua titik, dan titik tengah dari dua koordinat.

---

## 3. Cara Menjalankan Program

Buka terminal pada folder project, kemudian jalankan program menggunakan perintah berikut:

```bash
python latihan/01_biodata.py
```

Untuk menjalankan latihan lainnya, sesuaikan nama file dengan program yang ingin dijalankan.

Untuk menjalankan tugas utama:

```bash
python tugas/kalkulator_koordinat.py
```

---

## 4. Hasil Pengujian

Pengujian dilakukan pada program **`kalkulator_koordinat.py`** menggunakan tiga test case berikut:

| **Test Case** | **Titik A** | **Titik B** | **Jarak** | **Titik Tengah** | **Hasil** |
|---|---|---|---:|---|---|
| **Test Case 1** | (0, 0) | (3, 4) | 5.00 | (1.50, 2.00) | Berhasil |
| **Test Case 2** | (-2, 1) | (4, 1) | 6.00 | (1.00, 1.00) | Berhasil |
| **Test Case 3** | (2.5, -1) | (2.5, 3) | 4.00 | (2.50, 1.00) | Berhasil |

---

## 5. Refleksi

Konsep yang paling saya pahami adalah penggunaan variabel, input-output, dan operator dalam Python karena konsep tersebut dapat langsung diterapkan dalam pembuatan program sederhana.

Kesalahan yang saya temukan selama proses pengerjaan adalah memahami bahwa data yang dimasukkan pengguna melalui `input()` perlu dikonversi ke tipe data yang sesuai sebelum digunakan dalam proses perhitungan. Saya memperbaikinya dengan menggunakan fungsi `int()` atau `float()` sesuai dengan kebutuhan program.

Melalui latihan dan tugas pada pertemuan ini, saya mulai memahami bagaimana sebuah program sederhana dibangun dari proses menerima input, mengolah data, hingga menampilkan output. Pada pertemuan berikutnya, saya ingin lebih memahami materi pemrograman Python yang lebih kompleks.

---

## 6. Sumber

- Materi Pertemuan 02 Algoritma dan Pemrograman.
- Python Software Foundation, Python Tutorial.
