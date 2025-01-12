def volume(p, l , t):
    volume = p * l * t
    output = print(f"Volume balok adalah {volume} \n")
    return output

def luas(p, l, t):
    luas = 2 * (p * l + p * t + l * t)
    output = print(f"Luas permukaan balok adalah {luas} \n")
    return output

def keliling(p, l, t):
    keliling = 4 * (p + l + t)
    output = print(f"Keliling balok adalah {keliling} \n")
    return output