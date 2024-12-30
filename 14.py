# Program menentukan angka terbesar
print("Program menentukan angka terbesar.")
print("Dibuat oleh ")

# Meminta input dari user
bilangan = input("Masukkan 5 buah bilangan: ")

# Memisahkan input menjadi daftar bilangan
angka_list = bilangan.split()

# Inisialisasi bilangan terbesar dengan nilai bilangan pertama
bilangan_terbesar = int(angka_list[0])

# Menentukan bilangan terbesar
for angka in angka_list:
    angka = int(angka)
    if angka > bilangan_terbesar:
        bilangan_terbesar = angka

# Menampilkan hasil
print(f"Bilangan terbesar adalah {bilangan_terbesar}")
