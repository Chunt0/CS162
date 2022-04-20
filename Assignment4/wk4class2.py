"""
Working with tkinter
"""

import tkinter as tk

# def mi_to_km():
#     miles = float(my_input.get())
#     miles_label.config(text=f"Miles: {miles}")
#     kilometers = miles * 1.609344
#     kilometers_label.config(text=f"Kilometers: {kilometers}")

# root = tk.Tk()
# root.title(":D")
# root.geometry("400x125")
# root.config(padx=20, pady=20)

# welcome_label = tk.Label(root, text="Miles to Kilometer Converter!")
# welcome_label.grid(column=0, row=0)

# name_label= tk.Label(root, text="Enter Miles: ")
# name_label.grid(column=0, row=1)

# my_input = tk.Entry(root)
# my_input.grid(column=1, row=1)

# my_button = tk.Button(root, text="Click", command=mi_to_km)
# my_button.grid(column=0, row=2)

# miles_label = tk.Label(root, text="")
# miles_label.grid(column=1, row=2)

# kilometers_label = tk.Label(root, text="")
# kilometers_label.grid(column=1, row=3)

# root.mainloop()

import tkinter as tk
from turtle import width

def count_down(text):
    my_canvas.itemconfig(text, text ="CHANGED TEXT")

window = tk.Tk()
window.title("Focus-To-Do")

my_canvas = tk.Canvas(width=1000, height=1000, bg="#EBFAD0")
path = "/home/chunt/VScode/CS162/Assignment4/forest.png"
img = tk.PhotoImage(file=path)

my_canvas.create_image(200,225, image= img)
hello_text = my_canvas.create_text(200,800, text="Hello world", font=("Arial", 50, "bold"))
my_canvas.grid(column=1, row=1)

# start_button = tk.Button(text="Start", command=count_down(hello_text))
# start_button.grid(column=1,row=0)

x=5

window.mainloop()
