# Program menjumlah lima angka
print("Program menjumlah lima angka.")
print("Dibuat oleh ")

# Meminta user memasukkan 5 bilangan sekaligus
bilangan = input("Masukkan 5 buah bilangan: ")

# Memisahkan input menjadi daftar angka
angka_list = bilangan.split()

# Inisialisasi jumlah total bilangan
total = 0

# Menjumlahkan semua bilangan
for angka in angka_list:
    total += int(angka)

# Menampilkan hasil penjumlahan
print(f"Jumlah semua bilangan adalah {total}")
