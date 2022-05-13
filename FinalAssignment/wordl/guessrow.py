# Christopher Hunt
# CS162
# GuessRow Class

import tkinter as tk

class GuessRow(tk.Label):
    """Generates labels of the players guess."""
    def __init__(self,ROW):
        super().__init__()
        self.C1_label = tk.Label(text="", bg="black", fg="white", font=("Helvetica", 48, "bold"))
        self.C1_label.grid(column=1,row=ROW)

        self.C2_label = tk.Label(text="", bg="black", fg="white", font=("Helvetica", 48, "bold"))
        self.C2_label.grid(column=2,row=ROW)

        self.C3_label = tk.Label(text="", bg="black", fg="white", font=("Helvetica", 48, "bold"))
        self.C3_label.grid(column=3,row=ROW)

        self.C4_label = tk.Label(text="", bg="black", fg="white", font=("Helvetica", 48, "bold"))
        self.C4_label.grid(column=4,row=ROW)

        self.C5_label = tk.Label(text="", bg="black", fg="white", font=("Helvetica", 48, "bold"))
        self.C5_label.grid(column=5,row=ROW)

        self.row = [self.C1_label, self.C2_label, self.C3_label, self.C4_label, self.C5_label]


