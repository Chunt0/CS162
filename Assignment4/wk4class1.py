"""
Working with tkinter
"""

import tkinter as tk

def button_click():
    welcome_label.config(text=f"Welcome {my_input.get()}!")
    

root = tk.Tk()
root.title(":D")
root.geometry("800x800")
root.config(padx=20, pady=20)

welcome_label = tk.Label(root, text="Welcome!")
welcome_label.grid(column=0, row=0)

name_label= tk.Label(root, text="Name: ")
name_label.grid(column=0, row=1)

my_input = tk.Entry(root)
my_input.grid(column=1, row=1)

my_button = tk.Button(root, text="Click", command=button_click)
my_button.grid(column=0, row=2)

root.mainloop()
