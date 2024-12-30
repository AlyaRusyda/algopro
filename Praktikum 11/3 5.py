from tkinter import *
import tkinter as tk

my_app = tk.Tk()
my_app.title("Kalkulator Luas Piramid")

main_frame = tk.Frame(master=my_app, padx=20, pady=20)
main_frame.grid(column=0, row=0)

Font_style = ("Arial", 20, "bold")
tk.Label(master=main_frame, text='Kalkulator Luas Piramid', font=Font_style).grid(column=0, row=0, columnspan=2, pady=(0, 20))

tk.Label(master=main_frame, text='Panjang Sisi', font='Arial 12').grid(column=0, row=1, sticky="w", pady=5)
sisi = StringVar()
tk.Entry(master=main_frame, textvariable=sisi, font='Arial 12', width=15).grid(column=1, row=1, pady=5, sticky="w")

tk.Label(master=main_frame, text='Tinggi', font='Arial 12').grid(column=0, row=3, sticky="w", pady=5)
tinggi = StringVar()
tk.Entry(master=main_frame, textvariable=tinggi, font='Arial 12', width=15).grid(column=1, row=3, pady=5, sticky="w")

result = StringVar()

tk.Label(master=main_frame, text='Hasil', font='Arial 12').grid(column=0, row=4, sticky="w", pady=10)
tk.Label(master=main_frame, textvariable=result, font='Arial 12', bg="lightgray", width=20, anchor="w").grid(column=1, row=4, pady=10, sticky="w")

def calculate_volume():
    try:
        s = float(sisi.get())
        t = float(tinggi.get())
        volume = s * s + 4 * (1/2 * s * t)
        result.set(volume)
    except ValueError:
        result.set("Input tidak valid")

button_font = ("Arial", 12)
tk.Button(master=main_frame, text='Hitung', command=calculate_volume, font=button_font, width=10, bg="green", fg="white").grid(column=1, row=5, columnspan=2, pady=10, sticky="w")

tk.Button(master=main_frame, text='Keluar', command=my_app.quit, font=button_font, bg="red", fg="white", width=10).grid(column=1, row=6, pady=10, sticky="w")

my_app.mainloop()
