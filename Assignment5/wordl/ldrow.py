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

############################## WINDOW CLASS ####################################
class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.window =tk.Tk()
        self.window.title("ldrow")
        self.window.config(padx=50, pady=50, bg=BLACK)

################################################################################

############################# LDROW FUNCTIONS ##################################

def reset_game():
    global GUESS
    global word
    for guess in range(0,6):
        for index in range(0,5):
            guess_matrix[guess][index].config(text="", bg=BLACK)
    word = random.choice(wordlist)
    GUESS = 0
    print(word)

def make_guess():
    global GUESS 
    global MAX_GUESSES
    guessed_word = guess_entry.get()
    if GUESS < MAX_GUESSES and len(guessed_word) == 5 and wordlist.count(guessed_word) > 0:
        solution = match_word(word, guessed_word)
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

################################### TITLE CLASS #######################################
class Title(tk.Label):
    def __init__(self):
        super().__init__()

        self.L_label = tk.Label(text="L", bg=BLACK, fg=WHITE, font=("Helvetica", 48, "bold"))
        self.L_label.grid(column=1,row=0)

        self.D_label = tk.Label(text="D", bg=BLACK, fg=WHITE, font=("Helvetica", 48, "bold"))
        self.D_label.grid(column=2,row=0)

        self.R_label = tk.Label(text="R", bg=BLACK, fg=WHITE, font=("Helvetica", 48, "bold"))
        self.R_label.grid(column=3,row=0)

        self.O_label = tk.Label(text="O", bg=BLACK, fg=WHITE, font=("Helvetica", 48, "bold"))
        self.O_label.grid(column=4,row=0)

        self.W_label = tk.Label(text="W", bg=BLACK, fg=WHITE, font=("Helvetica", 48, "bold"))
        self.W_label.grid(column=5,row=0)
#################################################################################

################################ GUESS ROW CLASS ####################################
class GuessRow(tk.Canvas, tk.Label):
    def __init__(self):
        super().__init__()
        self.canvas = tk.Canvas(width=50, height=50, bg=GREY)
        self.canvas.grid(column=1, row=3)
        self.C1_label = tk.Label(text="", bg=BLACK, fg=WHITE, font=("Helvetica", 48, "bold"))
        self.C1_label.grid(column=1,row=3)

        self.canvas = tk.Canvas(width=50, height=50, bg=GREY)
        self.canvas.grid(column=2, row=3)
        self.C2_label = tk.Label(text="", bg=BLACK, fg=WHITE, font=("Helvetica", 48, "bold"))
        self.C2_label.grid(column=2,row=3)

        self.canvas = tk.Canvas(width=50, height=50, bg=GREY)
        self.canvas.grid(column=3, row=3)
        self.C3_label = tk.Label(text="", bg=BLACK, fg=WHITE, font=("Helvetica", 48, "bold"))
        self.C3_label.grid(column=3,row=3)

        self.canvas = tk.Canvas(width=50, height=50, bg=GREY)
        self.canvas.grid(column=4, row=3)
        self.C4_label = tk.Label(text="", bg=BLACK, fg=WHITE, font=("Helvetica", 48, "bold"))
        self.C4_label.grid(column=4,row=3)

        self.canvas = tk.Canvas(width=50, height=50, bg=GREY)
        self.canvas.grid(column=5, row=3)
        self.C5_label = tk.Label(text="", bg=BLACK, fg=WHITE, font=("Helvetica", 48, "bold"))
        self.C5_label.grid(column=5,row=3)

        self.row = [self.C1_label, self.C2_label, self.C3_label, self.C4_label, self.C5_label]
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

#################################################################################
path_to_wordlist = "./wordlist.txt"
wordlist = get_wordlist(path_to_wordlist)
word = random.choice(wordlist)
print(word)


window.mainloop()
