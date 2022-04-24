# CHRISTOPHER HUNT
# CS 162

import tkinter as tk
import random

##COLORS
GREEN = "#05C005"
PURPLE = "#4B00D0"
YELLOW = "#FFCA03"
RED = "#F90716"
ORANGE = "#FF5403"

##STUDY TIMES
STUDY = 25
SHORT = 5
LONG = 15

INTERVAL = 1
def count_down(count):
    global INTERVAL
    count_mins = count // 60 # floor division
    count_secs = count % 60 # modulus

    if(count_secs < 10): # modify the format of count_secs
        count_secs = f"{count_secs:02d}"
    canvas.itemconfig(timer_text, text=f"{count_mins}:{count_secs}")
    if(count > 0):
        window.after(1, count_down, count - 1)
    if(count == 0):
        INTERVAL += 1

def start_timer():
    global INTERVAL
    study_sec = STUDY * 60
    short_break = SHORT * 60
    long_break = LONG * 60
    if(INTERVAL == 1 or INTERVAL == 3 or INTERVAL == 5 or INTERVAL == 7):
        count_down(study_sec)
    elif(INTERVAL == 2 or INTERVAL == 4 or INTERVAL == 6):
        count_down(short_break)
    elif(INTERVAL == 8):
        count_down(long_break)

def restart_timer():
    global INTERVAL
    INTERVAL = 1

# Create Window
window =tk.Tk()
window.title("pomodoro")

# Upper Image
canvas = tk.Canvas(width=500, height=500, bg=PURPLE)
pomo_png_path = "/home/chunt/Code/CS162/Assignment4/png/pomo2.png"
pomo_img = tk.PhotoImage(file=pomo_png_path)
canvas.create_image(200,200, image=pomo_img)
canvas.grid(column=1, row=0)
interval_label = tk.Label(text="TIMER", bg=GREEN, fg=PURPLE, font=("Helvetica", 48, "bold"))
interval_label.grid(column=1,row=0)
timer_text = canvas.create_text(200,200, text="00:00", fill=YELLOW, font =("Helvetica", 48, "bold"))

# Button
start_button = tk.Button(text="START", bd=50, command=start_timer)
start_button.grid(column=0,row=0)
restart_button = tk.Button(text="RESTART", bd=50, command=restart_timer)
restart_button.grid(column=2,row=0)

window.mainloop()
