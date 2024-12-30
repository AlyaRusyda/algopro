# Program menghitung banyaknya angka negatif
print("Program menjumlah angka negatif.")
print("Dibuat oleh ")

# Koleksi bilangan
bilangan = [1, 2, -3, 4, -5, 6, 7, 8, -9, 10, 11, 12]
print(f"Ada 12 bilangan yaitu {tuple(bilangan)}")

# Inisialisasi jumlah angka negatif
count_negatif = 0

# Menghitung banyaknya angka negatif
for angka in bilangan:
    if angka < 0:
        count_negatif += 1

# Menampilkan hasil
print(f"Banyaknya angka negatif adalah {count_negatif} buah.")
