# CHRISTOPHER HUNT
# CS 162
# WORDL

import tkinter as tk

##COLORS
GREEN = "#05C005"
PURPLE = "#4B00D0"
YELLOW = "#FFCA03"
RED = "#F90716"
ORANGE = "#FF5403"

# Create Window
window =tk.Tk()
window.title("pomodoro")
window.config(padx=50, pady=50, bg="black")

################################### LDROW #######################################
canvas = tk.Canvas(width=50, height=50, bg=PURPLE)
canvas.grid(column=1, row=0)
L_label = tk.Label(text="L", bg=GREEN, fg=PURPLE, font=("Helvetica", 48, "bold"))
L_label.grid(column=1,row=0)

canvas = tk.Canvas(width=50, height=50, bg=PURPLE)
canvas.grid(column=2, row=0)
D_label = tk.Label(text="D", bg=GREEN, fg=PURPLE, font=("Helvetica", 48, "bold"))
D_label.grid(column=2,row=0)

canvas = tk.Canvas(width=50, height=50, bg=PURPLE)
canvas.grid(column=3, row=0)
R_label = tk.Label(text="R", bg=GREEN, fg=PURPLE, font=("Helvetica", 48, "bold"))
R_label.grid(column=3,row=0)

canvas = tk.Canvas(width=50, height=50, bg=PURPLE)
canvas.grid(column=4, row=0)
O_label = tk.Label(text="O", bg=GREEN, fg=PURPLE, font=("Helvetica", 48, "bold"))
O_label.grid(column=4,row=0)

canvas = tk.Canvas(width=50, height=50, bg=PURPLE)
canvas.grid(column=5, row=0)
W_label = tk.Label(text="W", bg=GREEN, fg=PURPLE, font=("Helvetica", 48, "bold"))
W_label.grid(column=5,row=0)
#################################################################################

################################### ROW 1 #######################################
canvas = tk.Canvas(width=50, height=50, bg=PURPLE)
canvas.grid(column=1, row=3)
R3_C1_label = tk.Label(text="", bg=GREEN, fg=PURPLE, font=("Helvetica", 48, "bold"))
R3_C1_label.grid(column=1,row=3)

canvas = tk.Canvas(width=50, height=50, bg=PURPLE)
canvas.grid(column=2, row=3)
D_label = tk.Label(text="", bg=GREEN, fg=PURPLE, font=("Helvetica", 48, "bold"))
D_label.grid(column=2,row=3)

canvas = tk.Canvas(width=50, height=50, bg=PURPLE)
canvas.grid(column=3, row=3)
R_label = tk.Label(text="", bg=GREEN, fg=PURPLE, font=("Helvetica", 48, "bold"))
R_label.grid(column=3,row=3)

canvas = tk.Canvas(width=50, height=50, bg=PURPLE)
canvas.grid(column=4, row=3)
O_label = tk.Label(text="", bg=GREEN, fg=PURPLE, font=("Helvetica", 48, "bold"))
O_label.grid(column=4,row=3)

canvas = tk.Canvas(width=50, height=50, bg=PURPLE)
canvas.grid(column=5, row=3)
W_label = tk.Label(text="", bg=GREEN, fg=PURPLE, font=("Helvetica", 48, "bold"))
W_label.grid(column=5,row=3)
#################################################################################

################################### ROW 2 #######################################
canvas = tk.Canvas(width=50, height=50, bg=PURPLE)
canvas.grid(column=1, row=4)
L_label = tk.Label(text="", bg=GREEN, fg=PURPLE, font=("Helvetica", 48, "bold"))
L_label.grid(column=1,row=4)

canvas = tk.Canvas(width=50, height=50, bg=PURPLE)
canvas.grid(column=2, row=4)
D_label = tk.Label(text="", bg=GREEN, fg=PURPLE, font=("Helvetica", 48, "bold"))
D_label.grid(column=2,row=4)

canvas = tk.Canvas(width=50, height=50, bg=PURPLE)
canvas.grid(column=3, row=4)
R_label = tk.Label(text="", bg=GREEN, fg=PURPLE, font=("Helvetica", 48, "bold"))
R_label.grid(column=3,row=4)

canvas = tk.Canvas(width=50, height=50, bg=PURPLE)
canvas.grid(column=4, row=4)
O_label = tk.Label(text="", bg=GREEN, fg=PURPLE, font=("Helvetica", 48, "bold"))
O_label.grid(column=4,row=4)

canvas = tk.Canvas(width=50, height=50, bg=PURPLE)
canvas.grid(column=5, row=4)
W_label = tk.Label(text="", bg=GREEN, fg=PURPLE, font=("Helvetica", 48, "bold"))
W_label.grid(column=5,row=4)
#################################################################################

################################## ROW 3 #######################################
canvas = tk.Canvas(width=50, height=50, bg=PURPLE)
canvas.grid(column=1, row=5)
L_label = tk.Label(text="", bg=GREEN, fg=PURPLE, font=("Helvetica", 48, "bold"))
L_label.grid(column=1,row=5)

canvas = tk.Canvas(width=50, height=50, bg=PURPLE)
canvas.grid(column=2, row=5)
D_label = tk.Label(text="", bg=GREEN, fg=PURPLE, font=("Helvetica", 48, "bold"))
D_label.grid(column=2,row=5)

canvas = tk.Canvas(width=50, height=50, bg=PURPLE)
canvas.grid(column=3, row=5)
R_label = tk.Label(text="", bg=GREEN, fg=PURPLE, font=("Helvetica", 48, "bold"))
R_label.grid(column=3,row=5)

canvas = tk.Canvas(width=50, height=50, bg=PURPLE)
canvas.grid(column=4, row=5)
O_label = tk.Label(text="", bg=GREEN, fg=PURPLE, font=("Helvetica", 48, "bold"))
O_label.grid(column=4,row=5)

canvas = tk.Canvas(width=50, height=50, bg=PURPLE)
canvas.grid(column=5, row=5)
W_label = tk.Label(text="", bg=GREEN, fg=PURPLE, font=("Helvetica", 48, "bold"))
W_label.grid(column=5,row=5)
#################################################################################

################################### ROW 4 #######################################
canvas = tk.Canvas(width=50, height=50, bg=PURPLE)
canvas.grid(column=1, row=6)
L_label = tk.Label(text="", bg=GREEN, fg=PURPLE, font=("Helvetica", 48, "bold"))
L_label.grid(column=1,row=6)

canvas = tk.Canvas(width=50, height=50, bg=PURPLE)
canvas.grid(column=2, row=6)
D_label = tk.Label(text="", bg=GREEN, fg=PURPLE, font=("Helvetica", 48, "bold"))
D_label.grid(column=2,row=6)

canvas = tk.Canvas(width=50, height=50, bg=PURPLE)
canvas.grid(column=3, row=6)
R_label = tk.Label(text="", bg=GREEN, fg=PURPLE, font=("Helvetica", 48, "bold"))
R_label.grid(column=3,row=6)

canvas = tk.Canvas(width=50, height=50, bg=PURPLE)
canvas.grid(column=4, row=6)
O_label = tk.Label(text="", bg=GREEN, fg=PURPLE, font=("Helvetica", 48, "bold"))
O_label.grid(column=4,row=6)

canvas = tk.Canvas(width=50, height=50, bg=PURPLE)
canvas.grid(column=5, row=6)
W_label = tk.Label(text="", bg=GREEN, fg=PURPLE, font=("Helvetica", 48, "bold"))
W_label.grid(column=5,row=6)
#################################################################################

################################### ROW 5 #######################################
canvas = tk.Canvas(width=50, height=50, bg=PURPLE)
canvas.grid(column=1, row=7)
L_label = tk.Label(text="", bg=GREEN, fg=PURPLE, font=("Helvetica", 48, "bold"))
L_label.grid(column=1,row=7)

canvas = tk.Canvas(width=50, height=50, bg=PURPLE)
canvas.grid(column=2, row=7)
D_label = tk.Label(text="", bg=GREEN, fg=PURPLE, font=("Helvetica", 48, "bold"))
D_label.grid(column=2,row=7)

canvas = tk.Canvas(width=50, height=50, bg=PURPLE)
canvas.grid(column=3, row=7)
R_label = tk.Label(text="", bg=GREEN, fg=PURPLE, font=("Helvetica", 48, "bold"))
R_label.grid(column=3,row=7)

canvas = tk.Canvas(width=50, height=50, bg=PURPLE)
canvas.grid(column=4, row=7)
O_label = tk.Label(text="", bg=GREEN, fg=PURPLE, font=("Helvetica", 48, "bold"))
O_label.grid(column=4,row=7)

canvas = tk.Canvas(width=50, height=50, bg=PURPLE)
canvas.grid(column=5, row=7)
W_label = tk.Label(text="", bg=GREEN, fg=PURPLE, font=("Helvetica", 48, "bold"))
W_label.grid(column=5,row=7)
#################################################################################








# Button
#start_button = tk.Button(text="START", bd=50, command=start_timer)
#restart_button = tk.Button(text="RESTART", bd=50, command=restart_timer)

window.mainloop()
