# CHRISTOPHER HUNT
# CS 162

import tkinter as tk
import random

################################# CONSTANTS ####################################
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
POMO_PNG_PATH = "/home/chunt/Code/CS162/Assignment4/png/pomo2.png"
timer = None
################################################################################


############################### WIDGET FUNCTIONS ###############################

def count_down(count: int):
    """count_down takes an int, that is the amount of seconds to count down from
    and decrements that intial time each time count_down is called.
    """
    global INTERVAL
    global timer
    count_mins = count // 60 # floor division:window
    count_secs = count % 60 # modulus

    if count_secs < 10: # modify the format of count_secs
        count_secs = f"{count_secs:02d}"
    canvas.itemconfig(timer_text, text=f"{count_mins}:{count_secs}")
    if count > 0:
        timer = window.after(1, count_down, count - 1)
    if count == 0:
        INTERVAL += 1
        start_button["state"] = "active"

def start_timer():
    """start_timer is the command that the start button runs when clicked. It
    checks to see which interval the timer is on and then sends the appropriate
    count value to count_down.
    """
    global INTERVAL
    start_button["state"] = "disabled"
    pause_button["state"] = "active"
    restart_button["state"] = "active"

    study_sec = STUDY * 60
    short_break = SHORT * 60
    long_break = LONG * 60
    if INTERVAL in (1,3,5,7):
        count_down(study_sec)
    elif INTERVAL in (2,4,6):
        count_down(short_break)
    elif INTERVAL== 8:
        count_down(long_break)

def restart_timer():
    """restart_timer resests the interval value to 1."""
    global INTERVAL
    INTERVAL = 1
    start_button["state"] = "active"
    pause_button["state"] = "active"

def pause_timer():
    """pause_timer stops the timer, restarts the timer when start_button pressed"""
    global timer
    pause_button["state"] = "disabled"
    start_button["state"] = "active"
    restart_button["state"] = "active"

    if timer:
        window.after_cancel(timer)
        timer = None

    pass

################################################################################


############################### WIDGET OBJECTS #################################
# Create Window
window =tk.Tk()
window.title("pomodoro")
window.config(bg=RED)
window.resizable(False, False)

# Image
canvas = tk.Canvas(width=500, height=500, bg=PURPLE)
pomo_img = tk.PhotoImage(file=POMO_PNG_PATH)
canvas.create_image(200,200, image=pomo_img)
canvas.grid(column=1, row=0)
interval_label = tk.Label(text="TIMER", bg=GREEN, fg=PURPLE, font=("Helvetica", 48, "bold"))
interval_label.grid(column=1,row=0)
timer_text = canvas.create_text(200,200, text="00:00", fill=YELLOW, font =("Helvetica", 48, "bold"))

# Button
start_button = tk.Button(text="START", command=start_timer)
start_button.grid(column=0,row=0)
restart_button = tk.Button(text="RESTART", command=restart_timer)
restart_button.grid(column=2,row=0)
pause_button = tk.Button(text="PAUSE", command=pause_timer)
pause_button.grid(column=1,row=1)

################################################################################


window.mainloop()
