class JajarGenjang(object):    
    def __init__(self, alas, tinggi):
        self.a = alas
        self.t = tinggi
        
    def luas(self):
        return self.a * self.t
    
jajar_genjang1 = JajarGenjang(3, 4)
print("Alas: ",jajar_genjang1.a)
print("Luas: ", jajar_genjang1.luas())