from tkinter import *
import tkinter as tk

my_app = tk.Tk()
my_app.title("Kalkulator Luas Prisma")

main_frame = tk.Frame(master=my_app, padx=20, pady=20)
main_frame.grid(column=0, row=0)

Font_style = ("Arial", 20, "bold")
tk.Label(master=main_frame, text='Kalkulator Luas Balok', font=Font_style).grid(column=0, row=0, columnspan=2, pady=(0, 20))

tk.Label(master=main_frame, text='Alas', font='Arial 12').grid(column=0, row=1, sticky="w", pady=5)
length = StringVar()
tk.Entry(master=main_frame, textvariable=length, font='Arial 12', width=15).grid(column=1, row=1, pady=5, sticky="w")

tk.Label(master=main_frame, text='Tinggi alas', font='Arial 12').grid(column=0, row=2, sticky="w", pady=5)
width = StringVar()
tk.Entry(master=main_frame, textvariable=width, font='Arial 12', width=15).grid(column=1, row=2, pady=5, sticky="w")

tk.Label(master=main_frame, text='Tinggi', font='Arial 12').grid(column=0, row=3, sticky="w", pady=5)
height = StringVar()
tk.Entry(master=main_frame, textvariable=height, font='Arial 12', width=15).grid(column=1, row=3, pady=5, sticky="w")

result = StringVar()

tk.Label(master=main_frame, text='Hasil', font='Arial 12').grid(column=0, row=4, sticky="w", pady=10)
tk.Label(master=main_frame, textvariable=result, font='Arial 12', bg="lightgray", width=20, anchor="w").grid(column=1, row=4, pady=10, sticky="w")

def calculate_volume():
    try:
        panjang = float(length.get())
        lebar = float(width.get())
        tinggi = float(height.get())
        luas = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
        result.set(luas)
    except ValueError:
        result.set("Input tidak valid")

button_font = ("Arial", 12)
tk.Button(master=main_frame, text='Hitung', command=calculate_volume, font=button_font, width=10, bg="green", fg="white").grid(column=1, row=5, columnspan=2, pady=10, sticky="w")

tk.Button(master=main_frame, text='Keluar', command=my_app.quit, font=button_font, bg="red", fg="white", width=10).grid(column=1, row=6, pady=10, sticky="w")

my_app.mainloop()
