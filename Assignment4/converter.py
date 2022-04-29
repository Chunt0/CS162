import tkinter as tk


# Converter inherit from the Tk class
class Converter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Distance Converter Program")

        frame = MilesToKm(self)
        frame.grid(column=0, row=0, sticky="nsew")


class MilesToKm(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        
        mile_to_km_label = tk.Label(self, text="Miles to Km")
        user_input = tk.Entry(self)
        convert_button = tk.Button(self, text="convert")
        
        mile_to_km_label.grid(column=0, row=0)
        user_input.grid(column=1, row=0)
        convert_button.grid(column=0, row=1)

converter = Converter()

converter.mainloop()
