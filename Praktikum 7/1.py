bangun_datar = {
    1: {"nama bangun": "Segitiga", "rumus luas": "L = 0.5 * a * t"},
    2: {"nama bangun": "Persegi", "rumus luas": "L = s ** 2"},
    3: {"nama bangun": "Persegi Panjang", "rumus luas": "L = p * l"},
    4: {"nama bangun": "Lingkaran", "rumus luas": "L = pi * r ** 2"},
    5: {"nama bangun": "Jajar Genjang", "rumus luas": "L = a * t"}
}
print(f"{'No':<3} | {'Nama Bangun':<15} | {'Rumus Luas'}")
print("-" * 3, "|", "-" * 15, "|", "-" * 15)

for no, data in bangun_datar.items():
    print(f"{no:<3} | {data ['nama bangun']:<15} | {data['rumus luas']}")