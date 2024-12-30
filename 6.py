# Program menghitung jumlah vokal
print("Program menghitung vokal.")
print("Dibuat oleh ")

# Teks yang akan diperiksa
teks = "Pembunuhan rakyat sipil adalah kejahatan perang."
print(f"Pada teks ini: {teks}")

# Daftar huruf vokal
vokal = "aeiouAEIOU"

# Inisialisasi jumlah vokal
count_vokal = 0

# Menghitung banyaknya huruf vokal
for huruf in teks:
    if huruf in vokal:
        count_vokal += 1

# Menampilkan hasil
print(f"Terdapat {count_vokal} huruf vokal.")
