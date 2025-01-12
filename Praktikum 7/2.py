password_benar = "Alyaaq"
kesempatan = 3
while kesempatan > 0:
    password = input("Masukkan password: ")
    if password == password_benar:
        print("Anda behasil login")
        break
    else:
        kesempatan -= 1
        if kesempatan > 0:
            print("Maaf, anda salah memasukkan password.")
        else:
            print("Anda telah mecoba 3 kali. Akses anda ditolak.")