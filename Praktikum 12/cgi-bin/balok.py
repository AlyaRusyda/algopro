p = 12
l = 7
t = 9

def hitung_luas(p, l, t):
    "fungsi hitung luas balok"
    return 2 * (p * l + l * t + p * t)
    
print("Content-type: text/html\n")
print("""<html>
<head><title>Website Luas Balok</title></head>
<body>""")
print("""
      <h1>Bangun Geometri</h1>
      <p>Nama bangun: Balok</p>
      <p>Dimensi: 3D</p>
      <p>Rumus luas: 2 &times; (p &times; l + l &times; t + p &times; t)
      """)
print(f"<p>Panjang: {p}</p>")
print(f"Lebar: {l}</p>")
print(f"Tinggi: {t}</p>")
print(f"Luas: {hitung_luas(p, l, t)}</p>")
print("</body></html>")