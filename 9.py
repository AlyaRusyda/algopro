# Program menampilkan kelipatan 3 antara bilangan awal dan akhir
print("Program menampilkan kelipatan 3 antara bilangan awal dan akhir.")
print("Dibuat oleh ")

# Meminta input dari user
awal = int(input("Masukkan bilangan awal: "))
akhir = int(input("Masukkan bilangan akhir: "))

print(f"Kelipatan 3 antara {awal} dan {akhir}: ", end="")

# Inisialisasi bilangan
bilangan = awal

# Perulangan while untuk menampilkan bilangan yang habis dibagi 3
while bilangan <= akhir:
    if bilangan % 3 == 0:
        print(bilangan, end=" ")
    bilangan += 1

print()  # untuk pindah baris setelah daftar bilangan
