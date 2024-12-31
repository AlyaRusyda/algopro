print("""<!DOCTYPE html>\n
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Geometri Balok</title>
  </head>
  <body>
    <h3>Bangun Geometri</h3>
    <form class="form1">
      <ol>
        <li><label for="nama">Nama Bangun : </label></li>
        <li><input type="text" id="nama" /> <br /></li>
        <li><label for="dimensi">Dimensi 2D/3D : </label></li>
        <li><input type="text" id="dimensi" /> <br /></li>
        <li><label for="rumus">Rumus Luas : </label></li>
        <li><input type="text" id="rumus" /> <br /></li>
        <li><label for="panjang">Panjang : </label></li>
        <li><input type="text" id="panjang" /> <br /></li>
        <li><label for="lebar">Lebar : </label></li>
        <li><input type="text" id="lebar" /> <br /></li>
        <li><label for="tinggi">Tinggi : </label></li>
        <li><input type="text" id="tinggi" /> <br /></li>
        <li><label for="luas">Luas : </label> <br /></li>
        <li><input type="button" id="submit" value="Hitung Luas" onclick="hitung()"/> <br /></li>
      </ol>
      </form>
    <form class="form2">
      <ol>
        <li><span id="hasilNama"></span> <br /></li>
        <li><span id="hasilDimensi"></span> <br /></li>
        <li><span id="hasilRumus"></span> <br /></li>
        <li><span id="hasilPanjang"></span> <br /></li>
        <li><span id="hasilLebar"></span> <br /></li>
        <li><span id="hasilTinggi"></span> <br /></li>
        <li><span id="hasilLuas"></span> <br /></li>
      </ol>
      </form>
    <script>
      function hitung() {
        var panjang = document.getElementById("panjang").value;
        var lebar = document.getElementById("lebar").value;
        var tinggi = document.getElementById("tinggi").value;
        var nama = document.getElementById("nama").value;
        var dimensi = document.getElementById("dimensi").value;
        var rumus = document.getElementById("rumus").value;
        var luas = 2 * (panjang * lebar + lebar * tinggi + panjang * tinggi);
      
        document.getElementById("hasilNama").innerHTML = nama;
        document.getElementById("hasilDimensi").innerHTML = dimensi;
        document.getElementById("hasilRumus").innerHTML = rumus;
        document.getElementById("hasilPanjang").innerHTML = panjang;
        document.getElementById("hasilLebar").innerHTML = lebar;
        document.getElementById("hasilTinggi").innerHTML = tinggi;
        document.getElementById("hasilLuas").innerHTML = luas;
      }
    </script>
    <style>
      *{
        background-color: lightblue;
      }
      h3{
        text-align: center;
        font-size: 30px;
      }
      .form1{
        text-align: center;
        margin-right: 35vh;
      }
      .form1 ol li{
        list-style-type: none;
        padding-top: 5px;
      }
      .form2{
        text-align: center;
        margin-right: 35vh;
      }
      .form2 ol li{
        list-style-type: none;
        padding-top: 5px;
      }
    </style>
  </body>
</html>""")