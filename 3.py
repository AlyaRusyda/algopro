print("Program menampilkan angka")
print("Dibuat oleh ")

for bilangan in range(1, 31):
    if bilangan % 12 == 0:
        print(f"{bilangan} snack and drink")
    elif bilangan % 3 == 0:
        print(f"{bilangan} snack")
    elif bilangan % 4 == 0:
        print(f"{bilangan} drink")
    else:
        print(bilangan)