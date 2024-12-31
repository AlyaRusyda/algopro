#!/usr/bin/env python3

import os
import urllib.parse

def hitung_luas_persegi(sisi):
    """Fungsi menghitung luas persegi."""
    return sisi * sisi

query = os.environ.get("QUERY_STRING", "")
params = urllib.parse.parse_qs(query)

try:
    sisi = float(params.get('sisi', [0])[0])
    luas = hitung_luas_persegi(sisi)
except (ValueError, IndexError):
    sisi = luas = 0

print("Content-Type: text/html\n")
print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hitung Luas Persegi</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f9f9f9;
        }}
        h1 {{
            color: #2c3e50;
        }}
        form {{
            margin-bottom: 20px;
        }}
        label {{
            display: inline-block;
            margin-top: 10px;
        }}
        input[type="number"] {{
            width: 100%;
            padding: 8px;
            margin-top: 5px;
        }}
        input[type="submit"] {{
            padding: 10px 20px;
            background-color: #2c3e50;
            color: white;
            border: none;
            cursor: pointer;
        }}
        table {{
            border-collapse: collapse;
            margin-top: 20px;
            width: 50%;
        }}
        table, th, td {{
            border: 1px solid #ddd;
            padding: 8px;
        }}
        th {{
            background-color: #f4f4f4;
        }}
        td {{
            text-align: left;
        }}
    </style>
</head>
<body>
    <h1>Hitung Luas Persegi</h1>
    <form method="get" action="persegi.py">
        <label for="sisi">Sisi (cm):</label>
        <input type="number" id="sisi" name="sisi" step="0.01" required>
        <input type="submit" value="Hitung">
    </form>

    <h2>Hasil Perhitungan</h2>
    <table>
        <tr>
            <th>Nama Bangun</th>
            <td>Persegi</td>
        </tr>
        <tr>
            <th>Dimensi</th>
            <td>2D</td>
        </tr>
        <tr>
            <th>Rumus Luas</th>
            <td>Sisi × Sisi</td>
        </tr>
        <tr>
            <th>Parameter</th>
            <td>Sisi: {sisi}</td>
        </tr>
        <tr>
            <th>Luas</th>
            <td>{luas:.2f} cm²</td>
        </tr>
    </table>
</body>
</html>
""")