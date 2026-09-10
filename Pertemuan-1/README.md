# Tugas Pertemuan 1 - Algoritma dan Pemrograman

**Identitas Mahasiswa**
- **Nama:** Reva Liyanasari
- **NIM:** 2225250101
- **Kelas:** 3A
- **Mata Kuliah:** Algoritma dan Pemrograman
- **Dosen Pengampu:** Dr. Aan Hendrayana, S.Si., M.Pd.
- **Topik:** Menentukan Jenis Akar dari Suatu Persamaan Kuadrat Berdasarkan Nilai Diskriminan

---

## 1. Deskripsi Masalah
Program ini dirancang untuk menentukan jenis akar dari suatu persamaan kuadrat berdasarkan nilai diskriminannya. Persamaan kuadrat memiliki bentuk umum **ax² + bx + c = 0**, dengan syarat utama koefisien **a ≠ 0**. Pengguna memasukkan nilai koefisien a, b, dan c.

Sebelum melakukan perhitungan diskriminan, sistem terlebih dahulu memverifikasi nilai a. Jika pengguna memasukkan nilai **a = 0**, program akan menampilkan pesan kesalahan karena persamaan tersebut bukan merupakan persamaan kuadrat. Namun jika **a ≠ 0**, program akan menghitung nilai diskriminan menggunakan rumus **D = b² − 4ac**.

Berdasarkan nilai diskriminan (D) yang diperoleh, program menentukan jenis akar persamaan kuadrat, yaitu:
- Jika **D > 0**, persamaan mempunyai dua akar real berbeda.
- Jika **D = 0**, persamaan mempunyai dua akar real sama/kembar.
- Jika **D < 0**, persamaan mempunyai akar tidak real atau kompleks.

---

## 2. Identifikasi Input – Proses – Output

| Komponen | Keterangan |
| :--- | :--- |
| **Input** | Nilai koefisien persamaan kuadrat yaitu `a`, `b`, dan `c` (dengan syarat `a ≠ 0`). |
| **Proses** | 1. Memvalidasi nilai koefisien `a` agar `a ≠ 0`.<br>2. Menghitung diskriminan dengan rumus `D = b² − 4ac`.<br>3. Membandingkan nilai `D` dengan 0.<br>4. Menentukan jenis akar berdasarkan kondisi nilai `D`. |
| **Output** | 1. Pesan kesalahan jika `a = 0`.<br>2. Nilai diskriminan (`D`).<br>3. Jenis akar persamaan kuadrat:<br>&nbsp;&nbsp;&nbsp;&nbsp;• Dua akar real berbeda, jika `D > 0`<br>&nbsp;&nbsp;&nbsp;&nbsp;• Akar real sama/kembar, jika `D = 0`<br>&nbsp;&nbsp;&nbsp;&nbsp;• Akar tidak real atau kompleks, jika `D < 0` |

---

## 3. Pseudocode

```text
ALGORITMA MenentukanJenisAkarKuadratBerdasarkanDiskriminan

BEGIN 
    INPUT a, b, c
```text
ALGORITMA MenentukanJenisAkarKuadratBerdasarkanDiskriminan

BEGIN 
    INPUT a, b, c
    IF a == 0 THEN
        OUTPUT "Bukan persamaan kuadrat (a tidak boleh sama dengan 0)"
    ELSE
        D ← (b * b) - (4 * a * c)
        OUTPUT "Nilai diskriminan =", D
        IF D > 0 THEN 
            OUTPUT "Dua akar real berbeda" 
        ELSE IF D = 0 THEN 
            OUTPUT "Akar real sama/kembar" 
        ELSE 
            OUTPUT "Akar tidak real atau kompleks"
        END IF 
    END IF
END
```

---

## 4. Test Case

| Test Case | Input (a, b, c) | Perhitungan (D = b² - 4ac) | Output |
| :--- | :--- | :--- | :--- |
| **Test Case 1** | a = 1, b = -5, c = 6 | D = (-5)² - 4(1)(6) = 25 - 24 = 1 | D = 1<br>Jenis Akar: "Dua akar real berbeda" |
| **Test Case 2** | a = 1, b = -4, c = 4 | D = (-4)² - 4(1)(4) = 16 - 16 = 0 | D = 0<br>Jenis Akar: "Akar real sama/kembar" |
| **Test Case 3** | a = 1, b = 2, c = 5 | D = (2)² - 4(1)(5) = 4 - 20 = -16 | D = -16<br>Jenis Akar: "Akar tidak real atau kompleks" |
| **Test Case 4** | a = 0, b = 3, c = 2 | Tidak dihitung (Dilewati) | Error: "Bukan persamaan kuadrat (a tidak boleh sama dengan 0)" |