# Program Menentukan Jenis Akar Persamaan Kuadrat Berdasarkan Nilai Diskriminan

print("=== Program Jenis Akar Persamaan Kuadrat ===")

try:
    # INPUT
    a = float(input("Masukkan koefisien a: "))
    b = float(input("Masukkan koefisien b: "))
    c = float(input("Masukkan koefisien c: "))

    print("\nHasil:")
    # Validasi Nilai a
    if a == 0:
        print("Error: Bukan persamaan kuadrat (nilai 'a' tidak boleh nol)!")
    else:
        # PROSES (Hitung Diskriminan)
        D = (b**2) - (4 * a * c)

        # Mengubah ke bilangan bulat jika nilainya tidak memiliki desimal
        D_tampil = int(D) if D.is_integer() else D

        # OUTPUT Nilai Diskriminan
        print("Nilai diskriminan =", D_tampil)

        # PROSES & OUTPUT Jenis Akar
        if D > 0:
            print("Dua akar real berbeda")
        elif D == 0:
            print("Akal real sama/kembar")
        else:
            print("Akar tidak real atau kompleks")

except ValueError:
    print("\nError: Input harus berupa angka yang valid!")