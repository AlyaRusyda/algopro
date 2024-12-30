import socket

hostname = 'localhost'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 8888))
print("Program komunikasi tentang server")

while True:
    pesan = input('Perintah: ')
    s.send(pesan.encode('utf-8'))

    response = s.recv(1024).decode('utf-8')
    print('Jawab:', response)

    if pesan.lower() == 'quit':
        s.close()
        break