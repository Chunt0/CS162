# CHRISTOPHER HUNT
# CS 162
# WORDL

import random, string
import tkinter as tk
from ldrow_funcs import get_wordlist, match_word
from title import Title
from guessrow import GuessRow
from keyboard import Keyboard

class Ldrow(tk.Tk):
    """Root window that UI exists in."""
    def __init__(self):
        super().__init__()
        row1 = GuessRow(2)
        row2 = GuessRow(3)
        row3 = GuessRow(4)
        row4 = GuessRow(5)
        row5 = GuessRow(6)
        row6 = GuessRow(7)
        self.title_row = Title()
        self.keyboard = Keyboard(6,3)
        # Rows are updated each round a player guesses
        self.guess_matrix = [
                row1.row,
                row2.row,
                row3.row,
                row4.row,
                row5.row,
                row6.row
                ]

        # Untouchables
        self._wordlist = get_wordlist("./wordlist.txt")
        self._word = random.choice(self._wordlist)
        self._GUESS = 0
        self._MAX_GUESS = 6
        self._YELLOW = "#FFCA03"
        self._GREEN = "#62B73E"
        self._GREY = "#5B5B5B"

        self.reset_button = tk.Button(text="RESET", width=4, command=self.reset_game)
        self.reset_button.grid(column=4, row=1)

        self.guess_entry = tk.Entry(width=5)
        self.guess_entry.grid(column=3,row=1)

        self.guess_button = tk.Button(text="GUESS", width=4, command=self.make_guess)
        self.guess_button.grid(column=2,row=1)

        print(self._word)

    def reset_game(self):
        for guess in range(0,6):
            for index in range(0,5):
                self.guess_matrix[guess][index].config(text="", bg="black")
        for letter in string.ascii_uppercase:
            self.keyboard.key_matrix.get(letter).config(text=letter, bg = "black", fg = "white")
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
                    if self.keyboard.key_matrix.get(answer[0]).cget("bg") == "black":
                        self.keyboard.key_matrix.get(answer[0]).config(text='')
                elif answer[1] == 1:
                    self.guess_matrix[self._GUESS][index].config(text=answer[0], fg="white", bg=self._GREEN)
                    self.keyboard.key_matrix.get(answer[0]).config(bg=self._GREEN)
                elif answer[1] == 2:
                    self.guess_matrix[self._GUESS][index].config(text=answer[0], fg="white", bg=self._YELLOW)
                    if self.keyboard.key_matrix.get(answer[0]).cget("bg") != self._GREEN:
                        self.keyboard.key_matrix.get(answer[0]).config(bg=self._YELLOW)
            self._GUESS += 1
        elif self._GUESS == self._MAX_GUESS:
            self._GUESS = 0
            self.reset_game()
        else:
            pass
