import socket

hostname = 'localhost'
pesan = ''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 8888))
print("Program komunikasi tentang data diri")

while pesan.lower() != 'keluar':
    pesan = input('Perintah: ')
    s.send(pesan.encode('utf-8')) 
    
    response = s.recv(1024).decode('utf-8')
    print('Jawab:', response)
