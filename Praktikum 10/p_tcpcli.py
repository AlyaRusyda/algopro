import socket

hostname = 'localhost'
pesan = ''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50003))
print('Mesin penjawab otomatis sudah siap')

while pesan.lower() != 'q':  # Terus meminta input sampai pengguna mengetik 'q'
    pesan = input('Pertanyaan: ')
    s.send(pesan.encode('utf-8'))  # Kirim pesan dalam bentuk byte
    if pesan.lower() != 'q':
        response = s.recv(1024).decode('utf-8')  # Terima dan decode jawaban dari server
        print('Jawaban:', response)

s.close()  # Tutup koneksi
