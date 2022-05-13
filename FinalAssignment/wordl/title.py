# Christopher Hunt
# CS162
# Title Class

import tkinter as tk

class Title(tk.Label):
    """Creates the title label"""
    def __init__(self):
        super().__init__()

        self.L_label = tk.Label(text="L", bg="black", fg="white", font=("Helvetica", 48, "bold"))
        self.L_label.grid(column=1,row=0)

        self.D_label = tk.Label(text="D", bg="black", fg="white", font=("Helvetica", 48, "bold"))
        self.D_label.grid(column=2,row=0)

        self.R_label = tk.Label(text="R", bg="black", fg="white", font=("Helvetica", 48, "bold"))
        self.R_label.grid(column=3,row=0)

        self.O_label = tk.Label(text="O", bg="black", fg="white", font=("Helvetica", 48, "bold"))
        self.O_label.grid(column=4,row=0)

        self.W_label = tk.Label(text="W", bg="black", fg="white", font=("Helvetica", 48, "bold"))
        self.W_label.grid(column=5,row=0)
