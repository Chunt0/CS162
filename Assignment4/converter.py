#!/usr/bin/env python3

import tkinter as tk


# Converter inherit from the Tk class
class Converter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Distance Converter Program")
        
        frame = MilesToKm(self)
        frame.grid(column=0, row=0)


class MilesToKm(tk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.input = tk.StringVar()

        self.mile_to_km_label = tk.Label(self, text="Miles to Km")
        self.user_input = tk.Entry(self, textvariable=self.input) 
        self.convert_button = tk.Button(self, text="convert", command=self.calculate)
        self.result_label = tk.Label(self)
        
        self.mile_to_km_label.grid(column=0, row=0)
        self.user_input.grid(column=1, row=0)
        self.convert_button.grid(column=0, row=1)
        self.result_label.grid(column=1, row=1)

    def calculate(self):
        try:
            mi = self.user_input.get()
            km = 1.60934 * float(mi)
            self.result_label.config(text=f"{mi} mi -> {km: .2f} km")
        except:
            pass

converter = Converter()

converter.mainloop()
