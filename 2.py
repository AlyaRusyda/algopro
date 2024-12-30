# Mulai program.
# Cetak "Program menampilkan tanda bilangan."
# Cetak "Dibuat oleh ..." (nama pembuat program).
# Tentukan koleksi yang terdiri dari 20 bilangan bulat.
# Lakukan perulangan for untuk setiap bilangan dalam koleksi.
# Jika bilangan lebih dari 0, cetak "positif."
# Jika bilangan kurang dari 0, cetak "negatif."
# Jika bilangan sama dengan 0, cetak "nol."
# Ulangi langkah 5 hingga seluruh bilangan selesai diproses.
# Akhiri program.

# Mulai
#   Cetak "Program menampilkan tanda bilangan."
#   Cetak "Dibuat oleh ..."
  
#   Definisikan koleksi 20 bilangan
  
#   Untuk setiap bilangan dalam koleksi:
#     Jika bilangan > 0, cetak "positif"
#     Jika bilangan < 0, cetak "negatif"
#     Jika bilangan == 0, cetak "nol"
    
# Selesai

# Program menampilkan tanda bilangan
print("Program menampilkan tanda bilangan.")
print("Dibuat oleh ")

# Definisikan koleksi 20 bilangan
koleksi_bilangan = [5, -8, 0, 4, -3, 12, -7, 0, 19, -2, 0, 7, -6, 10, 0, -15, 3, -9, 8, 0]

# Tampilkan judul kolom
print("Angka\tTanda")

# Perulangan untuk menampilkan setiap bilangan dan tanda
for bilangan in koleksi_bilangan:
    if bilangan > 0:
        print(f"{bilangan}\tpositif")
    elif bilangan < 0:
        print(f"{bilangan}\tnegatif")
    else:
        print(f"{bilangan}\tnol")