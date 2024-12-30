import socket

def hitung_luas_balok(s, t):
    return s * s + 4 * (1/2 * s * t)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50003))
s.listen(5)
print("Server siap menerima parameter dan perintah")

sisi = tinggi = 0

while True:
    komm, addr = s.accept()
    print(f"Koneksi dari {addr}")
    while True:
        data = komm.recv(1024).decode('utf-8')
        if not data:
            break

        print("Pesan diterima:", data)
        
        if data.startswith("sisi"):
            try:
                _, value = data.split('=')
                sisi = float(value.strip())
                response = "Parameter dicatat"
            except ValueError:
                response = "Format salah. Gunakan format: sisi = <nilai>"
        
        elif data.startswith("tinggi"):
            try:
                _, value = data.split('=')
                tinggi = float(value.strip())
                response = "Parameter dicatat"
            except ValueError:
                response = "Format salah. Gunakan format: tinggi = <nilai>"
        
        elif data.lower() == "hitung":
            if sisi > 0 and tinggi > 0:
                luas = hitung_luas_balok(sisi, tinggi)
                response = f"Luas piramid dengan panjang sisi {sisi} cm dan tinggi {tinggi} cm adalah {luas} cm2"
            else:
                response = "Parameter belum diatur. Masukkan panjang sisi dan tinggi terlebih dahulu."
        
        elif data.lower() == "keluar":
            response = "-"
            komm.send(response.encode('utf-8'))
            komm.close()
            print("Koneksi ditutup.")
            break
        
        else:
            response = "Perintah tidak dikenali"
        
        komm.send(response.encode('utf-8'))
