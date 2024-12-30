# Program menjumlah angka pada teks
print("Program menjumlah angka pada teks.")
print("Dibuat oleh ")

# Meminta input teks dari user
teks = input("Masukkan sebuah teks: ")

# Inisialisasi variabel untuk menyimpan jumlah angka
jumlah = 0

# Memeriksa setiap karakter pada teks
for karakter in teks:
    if karakter.isdigit():  # Jika karakter adalah angka
        jumlah += int(karakter)

# Menampilkan hasil penjumlahan angka
print(f"Jumlah angka pada teks adalah {jumlah}")
