import tkinter as tk
from tkinter import ttk
r = tk.Tk()  
r.title('Main window') 
r.configure(background='blue')
button1 = tk.Button(r, text='Convertor', width=40, height=3,bg='white') 
button2 = tk.Button(r,text='Processing', width=40, height=3, bg='white') 
button3 = tk.Button(r, text='Plot', width=40, height=3, bg='white')
button4 = tk.Button(r, text='Google map', width=40, height=3, bg='white')
button1.grid(row=0, column=1, padx=10, pady=10)
button2.grid(row=0, column=2, padx=10, pady=10)
button3.grid(row=0, column=3, padx=10, pady=10)
button4.grid(row=0, column=4, padx=10, pady=10)

from tkinter import filedialog
from tkinter import Button
from tkinter import *
def browsefunc():
    filename = filedialog.askopenfilename()
    pathlabel.config(text=filename)

browsebutton = Button(r, text="Browse", command=browsefunc)
browsebutton.grid(row=3, column=3, padx=10, pady=10)

pathlabel = Label(r)
pathlabel.grid()
r.mainloop()


