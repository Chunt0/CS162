"""
Working with tkinter
"""

import tkinter as tk
from turtle import width

def count_down(text):
    my_canvas.itemconfig(text, text ="CHANGED TEXT")

window = tk.Tk()
window.title("Focus-To-Do")

my_canvas = tk.Canvas(width=1000, height=1000, bg="#EBFAD0")
path = "/home/chunt/Code/CS162/Assignment4/forest.png"
img = tk.PhotoImage(file=path)

my_canvas.create_image(200,225, image= img)
hello_text = my_canvas.create_text(200,800, text="Hello world", font=("Arial", 50, "bold"))
my_canvas.grid(column=1, row=1)

# start_button = tk.Button(text="Start", command=count_down(hello_text))
# start_button.grid(column=1,row=0)


window.mainloop()
