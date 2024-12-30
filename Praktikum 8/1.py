import modul1

def bantuan():
    print('''Pilihan yang tersedia:
      b - Menampilkan bantuan ini
      N - Menampilkan NIM
      a - Menampilkan Nama
      A - Menampilkan Alamat
      K - Menampilkan Kode pos
      F - Menampilkan Fakultas
      P - Menampilkan Prodi
      U - Menampilkan Umur
      k - Keluar''')

def main():
    bantuan()
    opsi = input("Pilihan saudara: ")
    
    while opsi != 'k':
        if opsi == 'b':
            bantuan()
        elif opsi == 'N':
            modul1.tampilNIM()
        elif opsi == 'a':
            modul1.tampilNama()
        elif opsi == 'A':
            modul1.tampilAlamat()
        elif opsi == 'K':
            modul1.tampilKodepos()
        elif opsi == 'F':
            modul1.tampilFakultas()
        elif opsi == 'P':
            modul1.tampilProdi()
        elif opsi == 'U':
            modul1.tampilUmur()
        else:
            print('Perintah tidak dikenal')
        opsi = input("\nPilihan saudara: ")
    print("Selesai")

if __name__ == "__main__":
    main()
