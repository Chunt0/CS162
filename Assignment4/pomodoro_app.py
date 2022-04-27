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
POMO_PNG_PATH = "./PomodoroPics/pomo2.png" # You may need to change this.
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
    canvas.itemconfig(interval_text, text=f"INTERVAL: {INTERVAL}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
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
    elif INTERVAL == 8:
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

def next_interval():
    """Changes to the next time interval"""
    global INTERVAL
    if INTERVAL < 8:
        INTERVAL += 1
    else:
        INTERVAL = 1

def change_study_time():
    """Changes study time. User must enter an int else, nothing happens."""
    global STUDY
    try:
        STUDY = int(study_input.get())
    except:
        pass

def change_short_time():
    """Changes short break time. User must enter an int else, nothing happens."""
    global SHORT
    try:
        SHORT = int(short_break_input.get())
    except:
        pass

def change_long_time():
    """Changes long break time. User must enter an int else, nothing happens."""
    global LONG
    try:
        LONG = int(long_break_input.get())
    except:
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
timer_text = canvas.create_text(200,200, text="00:00", fill=YELLOW, font=("Helvetica", 48, "bold"))
interval_text = canvas.create_text(200,350, text=f"INTERVAL: {INTERVAL}", fill=YELLOW, font=("Helvetica", 48, "bold"))


# Button
start_button = tk.Button(text="START", command=start_timer)
start_button.grid(column=0,row=1)

restart_button = tk.Button(text="RESTART", command=restart_timer)
restart_button.grid(column=2,row=1)

pause_button = tk.Button(text="PAUSE", command=pause_timer)
pause_button.grid(column=1,row=1)

exit_button = tk.Button(text="EXIT", command=window.quit)
exit_button.grid(column=2,row=4)

next_button = tk.Button(text="NEXT", command=next_interval)
next_button.grid(column=0, row=4)

# Change Times:
study_button = tk.Button(text="STUDY TIME", command=change_study_time)
study_button.grid(column=0, row=2)
study_input = tk.Entry(window)
study_input.grid(column=0, row=3)

short_button = tk.Button(text="SHORT TIME", command=change_short_time)
short_button.grid(column=1, row=2)
short_break_input = tk.Entry(window)
short_break_input.grid(column=1, row=3)

long_button = tk.Button(text="LONG TIME", command=change_long_time)
long_button.grid(column=2, row=2)
long_break_input = tk.Entry(window)
long_break_input.grid(column=2, row=3)


################################################################################


window.mainloop()








