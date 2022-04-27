# CHRISTOPHER HUNT
# CS 162
# WORDL

import random
import tkinter as tk
from ldrow_funcs import get_wordlist, match_word

MAX_GUESSES = 6
GUESS = 0

################################# COLORS ########################################
BLACK = "black"
WHITE = "white"
YELLOW = "#FFCA03"
GREEN = "#62B73E"
GREY = "#5B5B5B"
#################################################################################

############################## Create Window ####################################

window =tk.Tk()
window.title("ldrow")
window.config(padx=50, pady=50, bg=BLACK)

################################################################################

############################# LDROW FUNCTIONS ##################################

def reset_game():
    pass 

def make_guess():
    global GUESS 
    global MAX_GUESSES
    guessed_word = guess_entry.get()
    solution = match_word(word, guessed_word)
    if GUESS < MAX_GUESSES and len(guessed_word) == 5:
        for index, answer in enumerate(solution):
            if answer[1] == 0:
                guess_matrix[GUESS][index].config(text=answer[0], fg=WHITE, bg=GREY)
            elif answer[1] == 1:
                guess_matrix[GUESS][index].config(text=answer[0], fg=WHITE, bg=GREEN)
            elif answer[1] == 2:
                guess_matrix[GUESS][index].config(text=answer[0], fg=WHITE, bg=YELLOW)
        GUESS += 1
    elif GUESS == MAX_GUESSES:
        GUESS = 0
    else:
        pass

################################################################################

################################### TITLE #######################################

L_label = tk.Label(text="L", bg=BLACK, fg=WHITE, font=("Helvetica", 48, "bold"))
L_label.grid(column=1,row=0)

D_label = tk.Label(text="D", bg=BLACK, fg=WHITE, font=("Helvetica", 48, "bold"))
D_label.grid(column=2,row=0)

R_label = tk.Label(text="R", bg=BLACK, fg=WHITE, font=("Helvetica", 48, "bold"))
R_label.grid(column=3,row=0)

O_label = tk.Label(text="O", bg=BLACK, fg=WHITE, font=("Helvetica", 48, "bold"))
O_label.grid(column=4,row=0)

W_label = tk.Label(text="W", bg=BLACK, fg=WHITE, font=("Helvetica", 48, "bold"))
W_label.grid(column=5,row=0)
#################################################################################

################################### ENTRY ROW ###################################
reset_button = tk.Button(text="RESET", width=4, command=reset_game)
reset_button.grid(column=2, row=9)

exit_button = tk.Button(text="EXIT", command=window.quit)
exit_button.grid(column=4, row=9)

guess_entry = tk.Entry(window, width=5)
guess_entry.grid(column=4,row=1)

guess_button = tk.Button(text="GUESS", width=4, command=make_guess)
guess_button.grid(column=2,row=1)
#################################################################################

################################### ROW 1 #######################################
canvas = tk.Canvas(width=50, height=50, bg=GREY)
canvas.grid(column=1, row=3)
R3_C1_label = tk.Label(text="", bg=BLACK, fg=WHITE, font=("Helvetica", 48, "bold"))
R3_C1_label.grid(column=1,row=3)

canvas = tk.Canvas(width=50, height=50, bg=GREY)
canvas.grid(column=2, row=3)
R3_C2_label = tk.Label(text="", bg=BLACK, fg=WHITE, font=("Helvetica", 48, "bold"))
R3_C2_label.grid(column=2,row=3)

canvas = tk.Canvas(width=50, height=50, bg=GREY)
canvas.grid(column=3, row=3)
R3_C3_label = tk.Label(text="", bg=BLACK, fg=WHITE, font=("Helvetica", 48, "bold"))
R3_C3_label.grid(column=3,row=3)

canvas = tk.Canvas(width=50, height=50, bg=GREY)
canvas.grid(column=4, row=3)
R3_C4_label = tk.Label(text="", bg=BLACK, fg=WHITE, font=("Helvetica", 48, "bold"))
R3_C4_label.grid(column=4,row=3)

canvas = tk.Canvas(width=50, height=50, bg=GREY)
canvas.grid(column=5, row=3)
R3_C5_label = tk.Label(text="", bg=BLACK, fg=WHITE, font=("Helvetica", 48, "bold"))
R3_C5_label.grid(column=5,row=3)

row0 = [ R3_C1_label, R3_C2_label, R3_C3_label, R3_C4_label, R3_C5_label]
#################################################################################

################################### ROW 2 #######################################
canvas = tk.Canvas(width=50, height=50, bg=GREY)
canvas.grid(column=1, row=4)
R4_C1_label = tk.Label(text="", bg=BLACK, fg=WHITE, font=("Helvetica", 48, "bold"))
R4_C1_label.grid(column=1,row=4)

canvas = tk.Canvas(width=50, height=50, bg=GREY)
canvas.grid(column=2, row=4)
R4_C2_label = tk.Label(text="", bg=BLACK, fg=WHITE, font=("Helvetica", 48, "bold"))
R4_C2_label.grid(column=2,row=4)

canvas = tk.Canvas(width=50, height=50, bg=GREY)
canvas.grid(column=3, row=4)
R4_C3_label = tk.Label(text="", bg=BLACK, fg=WHITE, font=("Helvetica", 48, "bold"))
R4_C3_label.grid(column=3,row=4)

canvas = tk.Canvas(width=50, height=50, bg=GREY)
canvas.grid(column=4, row=4)
R4_C4_label = tk.Label(text="", bg=BLACK, fg=WHITE, font=("Helvetica", 48, "bold"))
R4_C4_label.grid(column=4,row=4)

canvas = tk.Canvas(width=50, height=50, bg=GREY)
canvas.grid(column=5, row=4)
R4_C5_label = tk.Label(text="", bg=BLACK, fg=WHITE, font=("Helvetica", 48, "bold"))
R4_C5_label.grid(column=5,row=4)

row1 = [R4_C1_label, R4_C2_label, R4_C3_label, R4_C4_label, R4_C5_label]
#################################################################################

################################## ROW 3 #######################################
canvas = tk.Canvas(width=50, height=50, bg=GREY)
canvas.grid(column=1, row=5)
R5_C1_label = tk.Label(text="", bg=BLACK, fg=WHITE, font=("Helvetica", 48, "bold"))
R5_C1_label.grid(column=1,row=5)

canvas = tk.Canvas(width=50, height=50, bg=GREY)
canvas.grid(column=2, row=5)
R5_C2_label = tk.Label(text="", bg=BLACK, fg=WHITE, font=("Helvetica", 48, "bold"))
R5_C2_label.grid(column=2,row=5)

canvas = tk.Canvas(width=50, height=50, bg=GREY)
canvas.grid(column=3, row=5)
R5_C3_label = tk.Label(text="", bg=BLACK, fg=WHITE, font=("Helvetica", 48, "bold"))
R5_C3_label.grid(column=3,row=5)

canvas = tk.Canvas(width=50, height=50, bg=GREY)
canvas.grid(column=4, row=5)
R5_C4_label = tk.Label(text="", bg=BLACK, fg=WHITE, font=("Helvetica", 48, "bold"))
R5_C4_label.grid(column=4,row=5)

canvas = tk.Canvas(width=50, height=50, bg=GREY)
canvas.grid(column=5, row=5)
R5_C5_label = tk.Label(text="", bg=BLACK, fg=WHITE, font=("Helvetica", 48, "bold"))
R5_C5_label.grid(column=5,row=5)

row2 = [R5_C1_label, R5_C2_label, R5_C3_label, R5_C4_label, R5_C5_label]
#################################################################################

################################### ROW 4 #######################################
canvas = tk.Canvas(width=50, height=50, bg=GREY)
canvas.grid(column=1, row=6)
R6_C1_label = tk.Label(text="", bg=BLACK, fg=WHITE, font=("Helvetica", 48, "bold"))
R6_C1_label.grid(column=1,row=6)

canvas = tk.Canvas(width=50, height=50, bg=GREY)
canvas.grid(column=2, row=6)
R6_C2_label = tk.Label(text="", bg=BLACK, fg=WHITE, font=("Helvetica", 48, "bold"))
R6_C2_label.grid(column=2,row=6)

canvas = tk.Canvas(width=50, height=50, bg=GREY)
canvas.grid(column=3, row=6)
R6_C3_label = tk.Label(text="", bg=BLACK, fg=WHITE, font=("Helvetica", 48, "bold"))
R6_C3_label.grid(column=3,row=6)

canvas = tk.Canvas(width=50, height=50, bg=GREY)
canvas.grid(column=4, row=6)
R6_C4_label = tk.Label(text="", bg=BLACK, fg=WHITE, font=("Helvetica", 48, "bold"))
R6_C4_label.grid(column=4,row=6)

canvas = tk.Canvas(width=50, height=50, bg=GREY)
canvas.grid(column=5, row=6)
R6_C5_label = tk.Label(text="", bg=BLACK, fg=WHITE, font=("Helvetica", 48, "bold"))
R6_C5_label.grid(column=5,row=6)

row3 = [R6_C1_label, R6_C2_label, R6_C3_label, R6_C4_label, R6_C5_label]
#################################################################################

################################### ROW 5 #######################################
canvas = tk.Canvas(width=50, height=50, bg=GREY)
canvas.grid(column=1, row=7)
R7_C1_label = tk.Label(text="", bg=BLACK, fg=WHITE, font=("Helvetica", 48, "bold"))
R7_C1_label.grid(column=1,row=7)

canvas = tk.Canvas(width=50, height=50, bg=GREY)
canvas.grid(column=2, row=7)
R7_C2_label = tk.Label(text="", bg=BLACK, fg=WHITE, font=("Helvetica", 48, "bold"))
R7_C2_label.grid(column=2,row=7)

canvas = tk.Canvas(width=50, height=50, bg=GREY)
canvas.grid(column=3, row=7)
R7_C3_label = tk.Label(text="", bg=BLACK, fg=WHITE, font=("Helvetica", 48, "bold"))
R7_C3_label.grid(column=3,row=7)

canvas = tk.Canvas(width=50, height=50, bg=GREY)
canvas.grid(column=4, row=7)
R7_C4_label = tk.Label(text="", bg=BLACK, fg=WHITE, font=("Helvetica", 48, "bold"))
R7_C4_label.grid(column=4,row=7)

canvas = tk.Canvas(width=50, height=50, bg=GREY)
canvas.grid(column=5, row=7)
R7_C5_label = tk.Label(text="", bg=BLACK, fg=WHITE, font=("Helvetica", 48, "bold"))
R7_C5_label.grid(column=5,row=7)

row4 = [R7_C1_label, R7_C2_label, R7_C3_label, R7_C4_label, R7_C5_label]
#################################################################################

################################### ROW 6 #######################################
canvas = tk.Canvas(width=50, height=50, bg=GREY)
canvas.grid(column=1, row=8)
R8_C1_label = tk.Label(text="", bg=BLACK, fg=WHITE, font=("Helvetica", 48, "bold"))
R8_C1_label.grid(column=1,row=8)

canvas = tk.Canvas(width=50, height=50, bg=GREY)
canvas.grid(column=2, row=8)
R8_C2_label = tk.Label(text="", bg=BLACK, fg=WHITE, font=("Helvetica", 48, "bold"))
R8_C2_label.grid(column=2,row=8)

canvas = tk.Canvas(width=50, height=50, bg=GREY)
canvas.grid(column=3, row=8)
R8_C3_label = tk.Label(text="", bg=BLACK, fg=WHITE, font=("Helvetica", 48, "bold"))
R8_C3_label.grid(column=3,row=8)

canvas = tk.Canvas(width=50, height=50, bg=GREY)
canvas.grid(column=4, row=8)
R8_C4_label = tk.Label(text="", bg=BLACK, fg=WHITE, font=("Helvetica", 48, "bold"))
R8_C4_label.grid(column=4,row=8)

canvas = tk.Canvas(width=50, height=50, bg=GREY)
canvas.grid(column=5, row=8)
R8_C5_label = tk.Label(text="", bg=BLACK, fg=WHITE, font=("Helvetica", 48, "bold"))
R8_C5_label.grid(column=5,row=8)

row5 = [R8_C1_label, R8_C2_label, R8_C3_label, R8_C4_label, R8_C5_label]
#################################################################################
path_to_wordlist = "./wordlist.txt"
wordlist = get_wordlist(path_to_wordlist)
word = random.choice(wordlist)
print(word)

# Guess Matrix. Used to easily access each guess square.
guess_matrix = [row0, row1, row2, row3, row4, row5]


window.mainloop()
