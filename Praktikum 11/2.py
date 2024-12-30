from tkinter import *
import tkinter as tk

my_app = tk.Tk()
my_app.title("Kegiatan 2 - Kalkulator")

main_frame = tk.Frame(master=my_app, padx=24, pady=24)
main_frame.grid(column=0, row=0)

Font_style = ("Arial", 24, "bold")
tk.Label(master=main_frame, text='Kalkulator', font=Font_style).grid(column=0, row=0, columnspan=4, pady=(0, 20))

tk.Label(master=main_frame, text='Angka 1', font='Arial 12').grid(column=0, row=1, sticky="w", pady=5)
str1 = StringVar()
tk.Entry(master=main_frame, textvariable=str1, font='Arial 12', width=15).grid(column=1, row=1, columnspan=3, pady=5)

tk.Label(master=main_frame, text='Angka 2', font='Arial 12').grid(column=0, row=2, sticky="w", pady=5)
str2 = StringVar()
tk.Entry(master=main_frame, textvariable=str2, font='Arial 12', width=15).grid(column=1, row=2, columnspan=3, pady=5)

result = StringVar()

def tambah():
    try:
        a = int(str1.get())
        b = int(str2.get())
        result.set(a + b)
    except ValueError:
        result.set("Input tidak valid")

def kurang():
    try:
        a = int(str1.get())
        b = int(str2.get())
        result.set(a - b)
    except ValueError:
        result.set("Input tidak valid")

def kali():
    try:
        a = int(str1.get())
        b = int(str2.get())
        result.set(a * b)
    except ValueError:
        result.set("Input tidak valid")

def bagi():
    try:
        a = int(str1.get())
        b = int(str2.get())
        result.set(a / b)
    except ValueError:
        result.set("Input tidak valid")

button_padx = 10
button_pady = 5
button_font = ("Arial", 12)

tk.Button(master=main_frame, text='+', command=tambah, font=button_font, width=5).grid(column=0, row=3, padx=button_padx, pady=button_pady)
tk.Button(master=main_frame, text='-', command=kurang, font=button_font, width=5).grid(column=1, row=3, padx=button_padx, pady=button_pady)
tk.Button(master=main_frame, text='x', command=kali, font=button_font, width=5).grid(column=2, row=3, padx=button_padx, pady=button_pady)
tk.Button(master=main_frame, text=':', command=bagi, font=button_font, width=5).grid(column=3, row=3, padx=button_padx, pady=button_pady)

tk.Label(master=main_frame, text='Hasil', font='Arial 12').grid(column=0, row=4, sticky="w", pady=10)
tk.Label(master=main_frame, textvariable=result, font='Arial 12', bg="lightgray", width=20, anchor="w").grid(column=1, row=4, columnspan=3, pady=10)

tk.Button(master=main_frame, text='Keluar', command=my_app.quit, font=button_font, bg="red", fg="white", width=10).grid(column=1, row=5, columnspan=2, pady=(10, 0))

my_app.mainloop()