# Program menghitung kata
print("Program menghitung kata.")
print("Dibuat oleh ")

# Meminta input dari pengguna
kalimat = input("Masukkan kalimat: ")

# Memisahkan kalimat menjadi daftar kata
kata_kata = kalimat.split()

# Inisialisasi penghitung kata
jumlah_kata = 0

# Menghitung jumlah kata dengan perulangan
for kata in kata_kata:
    jumlah_kata += 1

# Menampilkan hasil
print(f"Kalimat '{kalimat}' memiliki {jumlah_kata} kata.")
