import tkinter as tk
from tkinter import ttk
from tkinter import font


window = tk.Tk()

window.geometry("500x400")
window.title("Hello World")


input_label1 = ttk.Label(master = window, text="Number 1=", font = font.Font(size=16))
input_label1.grid(row = 1, column = 0,pady = 10)

my_textfield = ttk.Entry(master = window)
my_textfield.grid(row = 1, column = 1,pady = 10)

input_label2 = ttk.Label(master = window, text="Number 2=", font = font.Font(size=16))
input_label2.grid(row = 2, column = 0,pady = 10)

my_textfield2 = ttk.Entry(master = window)
my_textfield2.grid(row = 2 , column = 1,pady = 10)


#Button

def  my_button_handler():
    firstValue = int(my_textfield.get())
    secondValue = int(my_textfield2.get())
    print("Sum =", firstValue + secondValue)
    result_label.configure(text="Result=" + str(firstValue + secondValue))



my_button = ttk.Button(master = window, text="Add", command = my_button_handler)
my_button.grid(row = 3, column = 1, sticky="w", pady = 10)

result_label = ttk.Label(master = window, text="Result=", font = font.Font(size=16))
result_label.grid(row = 4, column = 0, columnspan=2, pady = 10)

window.mainloop()
