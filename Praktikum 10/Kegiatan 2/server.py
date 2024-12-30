import socket
import platform

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 8888))
s.listen(5)
print("Program siap")

while True:
    komm, addr = s.accept()
    print(f"Koneksi dari {addr}")
    while True:
        data = komm.recv(1024).decode('utf-8')
        if not data:
            break
        print("Pertanyaan:", data)
        
        if data.lower() == 'machine':
            response = platform.machine()
        elif data.lower() == 'system':
            response = platform.system()
        elif data.lower() == 'node':
            response = platform.node()
        elif data.lower() == 'release':
            response = platform.release()
        elif data.lower() == 'version':
            response = platform.version()
        elif data.lower() == 'quit':
            response = "Program dihentikan. Selamat tinggal!"
            komm.send(response.encode('utf-8'))
            print("Koneksi ditutup.")
            komm.close()
            exit()
        else:
            response = "unknown command"

        komm.send(response.encode('utf-8'))
