class Tabung(object):    
    def __init__(self, jejari, tinggi):
        self.r = jejari
        self.t = tinggi
        
    def luas(self):
        return 3.14 * self.r ** 2
    
    def volume(self):
        return 3.14 * self.r ** 2 * self.t
    
tabung1 = Tabung(3, 4)
print("Jari-jari: ", tabung1.r, ", Tinggi: ", tabung1.t)
print("Luas: ", tabung1.luas())
print("Volume: ", tabung1.volume())