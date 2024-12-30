print("Program menentukan angka terkecil.")
print("Dibuat oleh Kelompok C12")

# meminta input dari user
bilangan = input("Masukkan 8 buah bilangan: ")
# memisahkan input menjadi tuple
angka_list = bilangan.split()
# melakukan perulangan apabila panjang angka_list != 8
while len(angka_list) != 8:
    # meminta input dari user
    print("Anda wajib memasukkan 8 bilangan")
    # meminta input dari user
    bilangan = input("Masukkan 8 buah bilangan: ")
    # memisahkan input menjadi tuple
    angka_list = bilangan.split()

# Inisialisasi bilangan terkecil dengan nilai bilangan pertama
bilangan_terkecil = int(angka_list[0])

# melakukan perulangan angka sebanyak angka_list
for angka in angka_list:
    # mengubah nilai angka menjadi integer
    angka = int(angka)
    # mengecek apakah angka lebih kecil daripada bilangan_terkecil
    if angka < bilangan_terkecil:
        # mengubah isi bilangan_terkecil menjadi angka
        bilangan_terkecil = angka

# menampilkan hasil
print("Bilangan terkecil adalah ", bilangan_terkecil)