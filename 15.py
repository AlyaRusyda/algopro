# Program menampilkan simbol
print("Program menampilkan simbol.")
print("Dibuat oleh ")

# Meminta input dari user
teks = input("Pada teks ini: ")

# Inisialisasi variabel untuk menyimpan simbol
simbol = ""

# Memeriksa setiap karakter pada teks
for karakter in teks:
    if not karakter.isalnum():  # Jika karakter bukan huruf atau angka
        simbol += karakter

# Menampilkan hasil simbol yang ditemukan
print(f"Terdapat simbol: {simbol}")
