# Program menjadikan list angka
print("Program menjadikan list angka.")
print("Dibuat oleh ")

# List berisi 20 item
data = [2, 4, 5, 6, 9, 'No', 1, 3, 5, 10, 'Ok', 5, 4, 'Yes', 5, 8, 'My', 9, 8, 1]

# Menampilkan list awal
print(f"Awalnya terdapat list berikut: {data}")

# Memeriksa setiap item di dalam list dan mengganti string dengan angka 0
for i in range(len(data)):
    if isinstance(data[i], str):
        data[i] = 0

# Menampilkan list setelah perubahan
print(f"Setelah dijadikan angka, list menjadi: {data}")
