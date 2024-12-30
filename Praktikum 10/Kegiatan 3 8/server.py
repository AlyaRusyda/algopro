import socket

def hitung_luas_balok(s):
    return s * s

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 8888))
s.listen(5)
print("Server siap menerima parameter dan perintah")

panjang = lebar = tinggi = 0

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
        
        elif data.lower() == "hitung":
            if sisi > 0:
                luas = hitung_luas_balok(sisi)
                response = f"Luas persegi dengan sisi {sisi} cm adalah {luas} cm2"
            else:
                response = "Parameter belum diatur. Masukkan sisi terlebih dahulu."
        
        elif data.lower() == "keluar":
            response = "-"
            komm.send(response.encode('utf-8'))
            komm.close()
            print("Koneksi ditutup.")
            break
        
        else:
            response = "Perintah tidak dikenali"
        
        komm.send(response.encode('utf-8'))
