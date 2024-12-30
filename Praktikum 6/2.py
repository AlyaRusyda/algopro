# Program akun
# Dibuat oleh Alya Rusyda L200240290 
import random

nama = 'Alya Rusyda Maharistya'
tanggalLahir = '31 Juli 2006'

# Split nama
partName = nama.split()
inisial = ''
for part in partName[:-1]:
    inisial += part[0] + '. '
shortName = inisial + partName[-1]
print(shortName)

# Buat username
# Username dibuat dari inisial, tanggal, dan tahun lahir. ex: 'A312006'
# Ambil tanggal dan tahun lahir dari tanggalLahir
tanggal = tanggalLahir.split()[0]
tahun = tanggalLahir.split()[-1]

# Gabungkan menjadi username
username = nama[0] + tanggal + tahun
print("Username:", username)

# Buat password dengan mengambil 3 huruf awal ditambah 3 angka acak
password = nama[0:3] + str(random.randint(100, 999))
print("Password: ", password)