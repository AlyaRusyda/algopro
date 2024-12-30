import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 8888))
s.listen(5)
print("Program siap")

biodata = {
    'nama': 'alya',
    'NIM': 'L200240290',
    'angkatan': '2024',
    'keluar': 'siap!!'
}

while True:
    komm, addr = s.accept()
    print(f"Koneksi dari {addr}")
    while True:
        data = komm.recv(1024).decode('utf-8')
        if not data:
            break
        print("Pertanyaan:", data)
        
        if data in biodata:
            response = biodata[data]
            if data.lower() == 'keluar':
                komm.close()
                break
        else:
            response = "Pertanyaan tidak relevan"
        
        komm.send(response.encode('utf-8')) 
