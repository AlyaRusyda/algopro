#!/usr/bin/env python3

print("Content-Type: text/html\n")
print("<!DOCTYPE html>")
print("""
<html>
<head><title>Akses dengan CGI</title></head>
<body>
""")
print("""
      <div style="float: left; margin-right: 20px;">
        <img src="/foto.png" alt="foto alya" width="170" height="230">
      </div>
""")
print("""
    <h3>Data Diri</h3>
    <p>Nama: Alya Rusyda Maharistya</p>
    <p>Alamat tinggal: Sukoharjo</p>
    <p>Tempat, tanggal lahir: Sukoharjo, 31 Juli 2006</p>
    <p>Tempat wisata favorit: Pantai</p>
    <p>Motto: Mantap</p>
""")
print("</body></html>")
