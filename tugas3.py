import re

# Kelas Akun digunakan untuk menyimpan dan mengelola data akun
class Akun():
    def __init__(self, email, username, password):
        self.email = email  # Menyimpan email akun
        self.username = username  # Menyimpan username akun
        self.password = password  # Menyimpan password akun
    
    def save_account(self):
        # Menyimpan data akun ke dalam file akun.txt
        with open("akun.txt", "w") as file:
            file.write(f"{self.email}\n{self.username}\n{self.password}\n")
    
    def load_data():
        # Membaca data akun dari file akun.txt dan mengembalikannya dalam bentuk objek Akun
        try:
            with open("akun.txt", "r") as file:
                lines = file.readlines()
                email = lines[0].strip()
                username = lines[1].strip()
                password = lines[2].strip()
                return Akun(email, username, password)
        except FileNotFoundError:
            return None  # Jika file tidak ditemukan, mengembalikan None

# Fungsi validasi email
def validate_email(email):
    # Mengecek apakah email memiliki format yang benar (harus mengandung @ dan .)
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

# Fungsi validasi username
def validate_username(username):
    # Mengecek apakah username sesuai dengan format yang diizinkan (5-15 karakter)
    pattern = r'^[a-zA-Z0-9_]{5,15}$'
    return bool(re.match(pattern, username))

# Fungsi validasi password
def validate_password(password):
    # Mengecek apakah password memenuhi kriteria (min 8 karakter, huruf besar/kecil, angka, simbol)
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    return bool(re.match(pattern, password))

# Fungsi untuk mendaftar akun baru
def daftar():
    print("=== Daftar Akun Baru ===")
    
    while True:  # Meminta input email dan memvalidasi formatnya
        email = input("Masukkan email: ")
        if validate_email(email):
            break
        print("Email tidak valid, coba lagi.")
    
    while True:  # Meminta input username dan memvalidasi formatnya
        username = input("Masukkan username (5-15 karakter, huruf/angka/_): ")
        if validate_username(username):
            break
        print("Username tidak valid, coba lagi.")
    
    while True:  # Meminta input password dan memvalidasi formatnya
        password = input("Masukkan password (min 8 karakter, huruf besar/kecil, angka, simbol): ")
        if validate_password(password):
            break
        print("Password tidak valid, coba lagi.")
    
    while True:  # Meminta konfirmasi password
        confirm_password = input("Konfirmasi password: ")
        if confirm_password == password:
            break
        print("Konfirmasi password tidak cocok, coba lagi.")
    
    # Menyimpan data akun setelah semua input valid
    akun_baru = Akun(email, username, password)
    akun_baru.save_account()
    print("Registrasi akun berhasil!")

# Fungsi untuk login ke akun
def login():
    print("=== Login Akun ===")
    
    akun_tersimpan = Akun.load_data()  # Memuat data akun yang tersimpan
    
    if not akun_tersimpan:
        print("Belum ada akun terdaftar. Silakan daftar terlebih dahulu.")
        main()  # Kembali ke fungsi main jika belum ada akun
        return
    
    while True:  # Meminta input email atau username dan memvalidasi keberadaannya
        input_user = input("Masukkan email atau username: ").strip()
        if "@" in input_user and "." in input_user:
            if not validate_email(input_user):
                print("Format email tidak valid, coba lagi.")
                continue
        
        # Mengecek apakah input cocok dengan data akun yang tersimpan
        if input_user == akun_tersimpan.email or input_user == akun_tersimpan.username:
            break
        else:
            print("Email/Username yang Anda masukkan belum terdaftar.")
            main()  # Kembali ke fungsi main jika input tidak terdaftar
            return
    
    attempts = 0  # Inisialisasi percobaan password
    while attempts < 3:  # Membatasi percobaan password sebanyak 3 kali
        input_password = input("Masukkan password: ").strip()
        if input_password == akun_tersimpan.password:
            print("Login berhasil!")
            return
        else:
            attempts += 1
            print(f"Password salah. Kesempatan tersisa: {3 - attempts}")
    
    print("Kesempatan 3 kali gagal. Login dibatalkan.")
    main()  # Kembali ke fungsi main jika login gagal

# Fungsi utama program
def main():
    # Meminta input apakah pengguna sudah memiliki akun atau belum
    choice = input("Apakah Anda sudah memiliki akun? (sudah/belum): ").strip().lower()
    
    if choice == "sudah":  # Jika sudah, lakukan login
        login()
    elif choice == "belum":  # Jika belum, lakukan registrasi
        daftar()
    else:
        print("Input tidak valid. Harap masukkan 'sudah' atau 'belum'.")
        main()  # Kembali ke fungsi main jika input tidak valid

# Bagian yang dieksekusi pertama ketika program dijalankan
if __name__ == "__main__":
    print("Selamat datang!")  # Menampilkan pesan sambutan
    main()  # Memulai program dengan memanggil fungsi main
