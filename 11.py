# Program menjumlah 6 bilangan pada koleksi
print("Program menjumlah 6 bilangan pada koleksi.")
print("Dibuat oleh ")

# Koleksi bilangan
bilangan = [10, 2, -3, 4, -5, 6, 7, 8, -9, 10, 11, 12]
print(f"Pada koleksi ini: {tuple(bilangan)}")

# Inisialisasi variabel untuk menyimpan hasil penjumlahan
jumlah = 0

# Menjumlahkan 6 bilangan pertama
for i in range(6):
    jumlah += bilangan[i]

# Menampilkan hasil penjumlahan
print(f"Jumlah 6 bilangan pertama adalah {jumlah}")
