

import tkinter as tk

def mi_to_km():
    miles = float(my_input.get())
    miles_label.config(text=f"Miles: {miles}")
    kilometers = miles * 1.609344
    kilometers_label.config(text=f"Kilometers: {kilometers}")

root = tk.Tk()
root.title(":D")
root.geometry("400x125")
root.config(padx=20, pady=20)

welcome_label = tk.Label(root, text="Miles to Kilometer Converter!")
welcome_label.grid(column=0, row=0)

name_label= tk.Label(root, text="Enter Miles: ")
name_label.grid(column=0, row=1)

my_input = tk.Entry(root)
my_input.grid(column=1, row=1)

my_button = tk.Button(root, text="Click", command=mi_to_km)
my_button.grid(column=0, row=2)

miles_label = tk.Label(root, text="")
miles_label.grid(column=1, row=2)

kilometers_label = tk.Label(root, text="")
kilometers_label.grid(column=1, row=3)

root.mainloop()