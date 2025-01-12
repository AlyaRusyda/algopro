import modul1

def bantuan():
    print('''
Daftar pilihan:
b - Menampilkan bantuan
V - Menghitung volume balok
L - Menghitung luas permukaan balok
K - Menghitung keliling balok
x - Keluar
    ''')

def masukkan_nilai():
    try:
        p = int(input("Masukkan panjang balok: "))
        l = int(input("Masukkan lebar balok: "))
        t = int(input("Masukkan tinggi balok: "))
        return p, l, t
    except ValueError:
        print("Input harus berupa angka. Silakan coba lagi.")
        return masukkan_nilai()

def choice():
    bantuan()
    while True:
        pilihan = input("Masukkan pilihan: ").lower()
        if pilihan == "b":
            bantuan()
        elif pilihan == "v":
            p, l, t = masukkan_nilai()
            modul1.volume(p, l, t)
        elif pilihan == "l":
            p, l, t = masukkan_nilai()
            modul1.luas(p, l, t)
        elif pilihan == "k":
            p, l, t = masukkan_nilai()
            modul1.keliling(p, l, t)
        elif pilihan == "x":
            print("Terima kasih telah mencoba program.")
            break
        else:
            print("Perintah tidak dikenal. Silakan coba lagi.")
            bantuan()
            pilihan = input("Masukkan pilihan: ").lower()

print("Selamat datang")
print("Program menghitung volume, luas permukaan, dan keliling balok")
choice()
