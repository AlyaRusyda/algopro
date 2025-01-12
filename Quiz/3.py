import tkinter as tk

my_app = tk.Tk()
my_app.title("Data diri")

Font_style = ("Arial", 24, "bold")
tk.Label(master=my_app, text='Data diri', font = Font_style).grid(column=0, row=0)

tk.Label(master=my_app, text='Nama', font = 'Arial 10').grid(column=0, row=1)
tk.Label(master=my_app, text='Namamu', font = 'Arial 10').grid(column=1, row=1)

tk.Label(master=my_app, text='Nim', font = 'Arial 10').grid(column=0, row=2)
tk.Label(master=my_app, text='NIM mu', font = 'Arial 10').grid(column=1, row=2)

tk.Button(master=my_app, text='Keluar', command=my_app.quit).grid(column=1, row=4)

my_app.mainloop()