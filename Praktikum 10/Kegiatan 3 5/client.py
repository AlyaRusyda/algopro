import socket

hostname = 'localhost'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50003))
print("Menghitung luas permukaan piramid")

while True:
    pesan = input("Pesan: ")
    s.send(pesan.encode('utf-8'))
    
    response = s.recv(1024).decode('utf-8')
    print("Respon:", response)
    
    if pesan.lower() == "keluar":
        s.close()
        break
