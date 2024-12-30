def konversiSuhu(C = 0, F = 0):
    if C != '':
        F = 9 / 5 * C + 32
        print(f'Suhu {C} Celcius setara dengan {F} Fahrenheit')
    elif F != '':
        C = (F - 32) * 5 / 9
        print(f'Suhu {F} Fahrenheit setara dengan {C} Celcius')
    