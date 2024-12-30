# Mulai
#   Cetak "Program menampilkan bilangan ganjil."
#   Baca bilangan_awal
#   Baca bilangan_akhir
  
#   Jika bilangan_awal genap, maka bilangan_awal = bilangan_awal + 1
  
#   Selama bilangan_awal <= bilangan_akhir
#     Cetak bilangan_awal
#     bilangan_awal = bilangan_awal + 2
# Selesai

# Mulai program.
# Cetak "Program menampilkan bilangan ganjil."
# Minta input dari pengguna untuk bilangan awal.
# Minta input dari pengguna untuk bilangan akhir.
# Jika bilangan awal adalah genap, tambahkan 1 agar dimulai dari bilangan ganjil.
# Cetak bilangan ganjil dari bilangan awal hingga bilangan akhir dengan menggunakan perulangan while.
# Hentikan perulangan jika bilangan telah melebihi bilangan akhir.
# Akhiri program.

# Program menampilkan bilangan ganjil
print("Program menampilkan bilangan ganjil.")
print("Dibuat oleh ")
bilangan_awal = int(input("Masukkan bilangan awal: "))
bilangan_akhir = int(input("Masukkan bilangan akhir: "))

# Jika bilangan awal genap, mulai dari bilangan ganjil berikutnya
if bilangan_awal % 2 == 0:
    bilangan_awal += 1

print("Bilangan ganjil antara", bilangan_awal, "dan", bilangan_akhir, "adalah:", end=" ")

while bilangan_awal <= bilangan_akhir:
    print(bilangan_awal, end=" ")
    bilangan_awal += 2