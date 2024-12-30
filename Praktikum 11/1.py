import tkinter as tk

my_app = tk.Tk()
my_app.title("Kegiatan 1 - Data diri")

main_frame = tk.Frame(master=my_app, padx=32, pady=28)
main_frame.grid(column=0, row=0)

Font_style = ("Arial", 24, "bold")
tk.Label(master=main_frame, text='Data diri', font=Font_style).grid(column=0, row=0, columnspan=2, sticky="w", pady=10)

tk.Label(master=main_frame, text='Nama', font='Arial 12').grid(column=0, row=1, sticky="w", pady=5)
tk.Label(master=main_frame, text=': Alya Rusyda Maharistya', font='Arial 12').grid(column=1, row=1, sticky="w", pady=5)

tk.Label(master=main_frame, text='NIM', font='Arial 12').grid(column=0, row=2, sticky="w", pady=5)
tk.Label(master=main_frame, text=': L200240290', font='Arial 12').grid(column=1, row=2, sticky="w", pady=5)

tk.Label(master=main_frame, text='Buku Favorit', font='Arial 12').grid(column=0, row=3, sticky="w", pady=5)
tk.Label(master=main_frame, text=': ', font='Arial 12').grid(column=1, row=3, sticky="w", pady=5)

tk.Label(master=main_frame, text='Idola', font='Arial 12').grid(column=0, row=4, sticky="w", pady=5)
tk.Label(master=main_frame, text=': ', font='Arial 12').grid(column=1, row=4, sticky="w", pady=5)

tk.Label(master=main_frame, text='Motto', font='Arial 12').grid(column=0, row=5, sticky="w", pady=5)
tk.Label(master=main_frame, text=': I believe I can', font='Arial 12').grid(column=1, row=5, sticky="w", pady=5)

tk.Button(master=main_frame, text='Keluar', command=my_app.quit, bg="red", fg="white", font=("Arial", 12, "bold"), padx=5, pady=3).grid(column=0, row=6, sticky="w", pady=10)

my_app.mainloop()