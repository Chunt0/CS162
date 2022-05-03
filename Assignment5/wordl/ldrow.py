# CHRISTOPHER HUNT
# CS 162
# WORDL

import random
import tkinter as tk
from ldrow_funcs import get_wordlist, match_word


############################## WINDOW CLASS ####################################
class Ldrow(tk.Tk):
    """Root window that UI exists in."""
    def __init__(self):
        super().__init__()
        self.window = tk.Tk()
        self.window.title("ldrow")
        self.window.config(padx=50, pady=50, bg="black")
        self.row1 = GuessRow(1)
        self.row2 = GuessRow(2)
        self.row3 = GuessRow(3)
        self.row4 = GuessRow(4)
        self.row5 = GuessRow(5)
        self.row6 = GuessRow(6)
        self.title_row = Title()

        # Rows are updated each round a player guesses
        self.guess_matrix = [
                self.row1.row,
                self.row2.row,
                self.row3.row,
                self.row4.row,
                self.row5.row,
                self.row6.row
                ]

        # Untouchables
        self._wordlist = get_wordlist("./wordlist.txt")
        self._word = random.choice(self._wordlist)
        self._GUESS = 0
        self._MAX_GUESS = 6
        self._YELLOW = "#FFCA03"
        self._GREEN = "#62B73E"
        self._GREY = "#5B5B5B"

        self.reset_button = tk.Button(text="RESET", width=4)
        self.reset_button.grid(column=2, row=9)

        self.exit_button = tk.Button(text="EXIT", command=self.window.quit)
        self.exit_button.grid(column=4, row=9)

        self.guess_entry = tk.Entry(self.window, width=5)
        self.guess_entry.grid(column=4,row=1)

        self.guess_button = tk.Button(text="GUESS", width=4, command=self.reset_game)
        self.guess_button.grid(column=2,row=1)

    def reset_game(self):
        for guess in range(0,6):
            for index in range(0,5):
                self.guess_matrix[guess][index].config(text="", bg="black")
        self._word = random.choice(self._wordlist)
        self._GUESS = 0
        print(self._word)

    def make_guess(self):
        guessed_word = self.guess_entry.get()
        if self._GUESS < self._MAX_GUESS and len(guessed_word) == 5 and self._wordlist.count(guessed_word) > 0:
            solution = match_word(self._word, guessed_word)
            for index, answer in enumerate(solution):
                if answer[1] == 0:
                    self.guess_matrix[self._GUESS][index].config(text=answer[0], fg="white", bg=self._GREY)
                elif answer[1] == 1:
                    self.guess_matrix[self._GUESS][index].config(text=answer[0], fg="white", bg=self._GREEN)
                elif answer[1] == 2:
                    self.guess_matrix[self._GUESS][index].config(text=answer[0], fg="white", bg=self._YELLOW)
            self._GUESS += 1
        elif self._GUESS == self._MAX_GUESS:
            self._GUESS = 0
        else:
            pass

################################################################################

################################### TITLE CLASS #######################################
class Title(tk.Label):
    """Creates the title label"""
    def __init__(self):
        super().__init__()

        self.L_label = tk.Label(text="L", bg="black", fg="white", font=("Helvetica", 48, "bold"))
        self.L_label.grid(column=1,row=0)

        self.D_label = tk.Label(text="D", bg="black", fg="white", font=("Helvetica", 48, "bold"))
        self.D_label.grid(column=2,row=0)

        self.R_label = tk.Label(text="R", bg="black", fg="white", font=("Helvetica", 48, "bold"))
        self.R_label.grid(column=3,row=0)

        self.O_label = tk.Label(text="O", bg="black", fg="white", font=("Helvetica", 48, "bold"))
        self.O_label.grid(column=4,row=0)

        self.W_label = tk.Label(text="W", bg="black", fg="white", font=("Helvetica", 48, "bold"))
        self.W_label.grid(column=5,row=0)
#################################################################################

################################ GUESS ROW CLASS ####################################
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
#################################################################################


ldrow = Ldrow()

ldrow.mainloop()
