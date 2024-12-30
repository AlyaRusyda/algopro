class Balok(object):    
    def __init__(self, pjg, lbr, tg):
        self.p = pjg
        self.l = lbr
        self.t = tg
        
    def luas(self):
        return 2 * ((self.p * self.t) + (self.t * self.l) + (self.p * self.l))
    
    def volume(self):
        return self.p * self.t * self.l
    
balok1 = Balok(5, 3, 4)
print("Panjang: ", balok1.p, ", Lebar: ", balok1.l)
print("Luas Permukaan: ", balok1.luas())
print("Volume: ", balok1.volume())