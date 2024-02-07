import tkinter as tk
from tkinter import ttk


window = tk.Tk()

window.geometry("500x400")
window.title("Hello World")

my_textfield = ttk.Entry(master = window)
my_textfield.place(x=180, y=100)

my_textfield2 = ttk.Entry(master = window)
my_textfield2.place(x=180, y=140)


#Button

def  my_button_handler():
    firstValue = int(my_textfield.get())
    secondValue = int(my_textfield2.get())
    print("Sum =", firstValue + secondValue)


my_button = ttk.Button(master = window, text="Click Me", command = my_button_handler)
my_button.place(x = 180, y = 180)

window.mainloop()
