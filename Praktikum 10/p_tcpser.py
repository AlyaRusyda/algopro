import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50003))
s.listen(5)
print("Server penjawab otomatis sudah siap")

kamus = {'nama': 'Apalah artinya sebuah nama',
         'umur': 'Saya lebih muda dari anda',
         'alamat': 'Tepi bukit',
         'motto': 'Sesat di jalan',
         'kuliah': 'ya'}

while True:  # Menunggu koneksi klien
    komm, addr = s.accept()
    print(f"Koneksi diterima dari {addr}")
    while True:  # Loop untuk komunikasi dengan klien
        data = komm.recv(1024).decode('utf-8')  # Terima data dari klien
        if not data or data.lower() == 'q':  # Jika 'q' atau tidak ada data, keluar dari loop
            print("Koneksi ditutup oleh klien.")
            komm.close()
            break
        print('Pertanyaan:', data)
        if data in kamus:  # Cek jika pertanyaan ada di kamus
            response = kamus[data]
        else:
            response = 'Pertanyaan anda tidak relevan'
        komm.send(response.encode('utf-8'))  # Kirim jawaban dalam bentuk byte
