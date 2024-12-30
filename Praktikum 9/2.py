with open("L200240290", "r") as file:
    nim, tanggalLahir, nama = file.readlines()

kota = "Sukoharjo"
with open("L200240290", "w") as file:
    file.write(f"{nama}\n{kota}, 07/31/2006\n{nim}")

file = open("L200240290", "r")
read = file.read()
print(read)
file.close()