import tkinter as tk
from tkinter import ttk
from tkinter import font


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
    result_label.configure(text="Result=" + str(firstValue + secondValue))



my_button = ttk.Button(master = window, text="Add", command = my_button_handler)
my_button.place(x = 180, y = 180)

result_label = ttk.Label(master = window, text="Result=", font = font.Font(size=16))
result_label.place(x = 180, y = 220)

window.mainloop()
