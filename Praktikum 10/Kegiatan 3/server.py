import socket

def hitung_luas_balok(p, l, t):
    return 2 * (p * l + p * t + l * t)

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
        
        if data.startswith("panjang"):
            try:
                _, value = data.split('=')
                panjang = float(value.strip())
                response = "Parameter dicatat"
            except ValueError:
                response = "Format salah. Gunakan format: panjang = <nilai>"
        
        elif data.startswith("lebar"):
            try:
                _, value = data.split('=')
                lebar = float(value.strip())
                response = "Parameter dicatat"
            except ValueError:
                response = "Format salah. Gunakan format: lebar = <nilai>"
        
        elif data.startswith("tinggi"):
            try:
                _, value = data.split('=')
                tinggi = float(value.strip())
                response = "Parameter dicatat"
            except ValueError:
                response = "Format salah. Gunakan format: tinggi = <nilai>"
        
        elif data.lower() == "hitung":
            if panjang > 0 and lebar > 0 and tinggi > 0:
                luas = hitung_luas_balok(panjang, lebar, tinggi)
                response = f"Luas balok dengan panjang {panjang} cm, lebar {lebar} cm, dan tinggi {tinggi} cm adalah {luas} cm2"
            else:
                response = "Parameter belum diatur. Masukkan panjang, lebar, dan tinggi terlebih dahulu."
        
        elif data.lower() == "keluar":
            response = "-"
            komm.send(response.encode('utf-8'))
            komm.close()
            print("Koneksi ditutup.")
            break
        
        else:
            response = "Perintah tidak dikenali"
        
        komm.send(response.encode('utf-8'))
