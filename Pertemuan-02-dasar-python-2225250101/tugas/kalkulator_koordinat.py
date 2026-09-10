"""
Nama: Reva Liyanasari
NIM: 22252610101
Kelas: 3A
Tugas: Kalkulator Koordinat Dua Titik
"""

print("KALKULATOR KOORDINAT DUA TITIK")

# Input koordinat titik A
x1 = float(input("x titik A: "))
y1 = float(input("y titik A: "))

# Input koordinat titik B
x2 = float(input("x titik B: "))
y2 = float(input("y titik B: "))

# Menghitung perubahan koordinat
dx = x2 - x1
dy = y2 - y1

# Menghitung jarak antara titik A dan B
jarak = ((dx ** 2) + (dy ** 2)) ** 0.5

# Menghitung titik tengah
tengah_x = (x1 + x2) / 2
tengah_y = (y1 + y2) / 2

# Menampilkan hasil
print()
print(f"Titik A     : ({x1:.2f}, {y1:.2f})")
print(f"Titik B     : ({x2:.2f}, {y2:.2f})")
print(f"Perubahan   : dx = {dx:.2f}, dy = {dy:.2f}")
print(f"Jarak A ke B: {jarak:.2f}")
print(f"Titik tengah: ({tengah_x:.2f}, {tengah_y:.2f})")