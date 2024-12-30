import shelve

# Membaca data dari shelve
with shelve.open("Alya.data") as db:
    nama = db["nama"]
    ttl = db["ttl"]
    nim = db["nim"]

# Menampilkan data ke layar
print(f"{nama}\n{ttl}\n{nim}")