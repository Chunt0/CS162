import tkinter as tk

# Homework for this week is to expand on this app

# Extra - Make an image with tkinter and post image on discord

window = tk.Tk()
window.title("Pomodoro")

canvas = tk.Canvas(width=1000, height=1000, bg="#4B00D0")

forest_png = "./forest.png"
forest_img = tk.PhotoImage(file=forest_png)

lotus1_png = "./lotus1.png"
lotus1_img = tk.PhotoImage(file=lotus1_png)

violet1_png = "./violet1.png"
violet1_img = tk.PhotoImage(file=violet1_png)

toadstool1_png = "./toadstool1.png"
toadstool1_img = tk.PhotoImage(file=toadstool1_png)

canvas.create_image(600,500, image=forest_img)
#canvas.create_image(100,50, image=lotus1_img)
#canvas.create_image(100,50, image=violet1_img)
#canvas.create_image(200,225, image=toadstool1_img)

canvas.grid(column=0, row=0)


window.mainloop()
