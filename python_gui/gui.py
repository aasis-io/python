import tkinter as tk
from tkinter import ttk


window = tk.Tk()

window.geometry("500x400")
window.title("Hello World")

my_textfield = tk.Entry(master = window)
my_textfield.place(x=180, y=100)


#Button

def  my_button_handler():
    print("Button Clicked!")

my_button = tk.Button(master = window, text="Click Me", command = my_button_handler)
my_button.place(x = 180, y = 150)

window.mainloop()
