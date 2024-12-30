# Program menjumlah angka negatif
print("Program menjumlah angka negatif.")
print("Dibuat oleh ")

# Koleksi bilangan
bilangan = [1, 2, -3, 4, -5, 6, 7, 8, -9, 10, 11, 12]
print(f"Ada 12 bilangan yaitu {tuple(bilangan)}")

# Inisialisasi jumlah angka negatif
jumlah_negatif = 0

# Menjumlahkan semua angka negatif
for angka in bilangan:
    if angka < 0:
        jumlah_negatif += angka

# Menampilkan hasil penjumlahan
print(f"Jumlah semua angka negatif adalah {jumlah_negatif}")
