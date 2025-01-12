nama = input("Masukkan nama saudara: ")
jam = float(input("Pukul berapa sekarang?: "))
time = ('pagi', 'siang', 'sore', 'petang', 'malam')

if 0 <= jam < 09.00:
    salam = time[0]  # Pagi
elif 09.00 <= jam < 14.00:
    salam = time[1]  # Siang
elif 14.00 <= jam < 18.00:
    salam = time[2]  # Sore
elif 18.00 <= jam < 20.00:
    salam = time[3]  # Petang
elif 20.00 <= jam <= 23.59:
    salam = time[4]  
else:
    salam = None
    
if salam:
    print(f"Selamat {salam}, {nama}")
else:
    print("Waktu yang dimasukkan tidak valid.")