import socket

hostname = 'localhost'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 8888))
print("Menghitung luas permukaan balok")
print('''Perintah yang tersedia:
      - sisi: memasukkan value ke parameter sisi
      - hitung: menghitung luas permukaan berdasarkan parameter yang dimasukkan
      - keluar: menghentikan program''')

while True:
    pesan = input("Pesan: ")
    s.send(pesan.encode('utf-8'))
    
    response = s.recv(1024).decode('utf-8')
    print("Respon:", response)
    
    if pesan.lower() == "keluar":
        s.close()
        break
