# CHRISTOPHER HUNT
# CS 162
# WORDL

import random, string
import tkinter as tk
from title import Title
from guessrow import GuessRow
from keyboard import Keyboard

class Ldrow(tk.Tk):
    """Initializes title bar, guess matrix, guess and reset buttons, guess entry and keyboard."""
    def __init__(self):
        super().__init__()
        self.title_row = Title()
        
        self.keyboard = Keyboard(6,3) # (6,3) relate to column and row position of keyboard
        
        row1 = GuessRow(2)
        row2 = GuessRow(3)
        row3 = GuessRow(4)
        row4 = GuessRow(5)
        row5 = GuessRow(6)
        row6 = GuessRow(7)
        self.guess_matrix = [
                row1.row,
                row2.row,
                row3.row,
                row4.row,
                row5.row,
                row6.row
                ]

        # Untouchables
        self._wordlist = self.get_wordlist("./wordlist.txt")
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
        """
        Loops through self.game_matrix and sets all values back to empty, then
        loops through the alphabet and resets self.keyboard.key_matrix. A new
        word is selected, guesses set to zero and the new word is printed to
        the terminal.
        """
        for guess in range(0,6):
            for index in range(0,5):
                self.guess_matrix[guess][index].config(text="", bg="black")
        for letter in string.ascii_uppercase:
            self.keyboard.key_matrix.get(letter).config(text=letter, bg = "black", fg = "white")
        self._word = random.choice(self._wordlist)
        self._GUESS = 0
        print(self._word)

    def make_guess(self):
        """
        Triggered when the guess_button is triggered. Takes input from guess_entry
        and inputs it to match_word(word, guess). The solution is then enumerated
        in a for loop and the self.guess_matrix is updated with that rounds guess
        solution.
        """
        guessed_word = self.guess_entry.get()

        # Makes sure the player doesn't exceed guess limit or inputs a word incorrectly
        if self._GUESS < self._MAX_GUESS and len(guessed_word) == 5 and self._wordlist.count(guessed_word) > 0:
            try:
                solution = self.match_word(self._word, guessed_word)
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
            except:
                pass
        elif self._GUESS == self._MAX_GUESS:
            self._GUESS = 0
            self.reset_game()
        else:
            pass


    def get_wordlist(self, path_to_wordlist):
        """Takes path to a wordlist and outputs a list object of the wordlist."""
        with open(path_to_wordlist, encoding="utf-8") as wlist:
            wordlist_temp = wlist.readlines()

        wordlist = []
        for word in wordlist_temp:
            word = word.replace('\n','')
            wordlist.append(word)

        return wordlist

    def match_word(self, word, guess):
        """
        Compares values between the guessed word and the word to be guessed.
        Uses frequency lists to help make decision about if the character doesn't
        match, matches and is in the wrong spot, or matches and is in the right
        spot.
        """

        # Format guess and word, make answer list
        guess = guess.upper()
        word = word.upper()

        freq = [0] * 26
        alphabet = string.ascii_uppercase
        output = [['',0],['',0],['',0],['',0],['',0],]

        for index1, _ in enumerate(word):
            for index2, _ in enumerate(alphabet):
                if word[index1] == alphabet[index2]:
                    freq[index2] += 1
        guess = [char for char in guess] # Splitting the guess into a list of chars for manipulation purposes

        # Check not a match or exact match
        for index, _ in enumerate(word):
            if guess[index] not in word:
                output[index] = [guess[index], 0]
            elif word[index] == guess[index]:
                output[index] = [guess[index], 1]
                freq[alphabet.index(guess[index])] -= 1 # Decrement our list of freqs
                guess[index] = 0 # Set this letter to 0 in order to weed out the correct matches


        # Now we'll do a seperate loop to deal with multiple/misplaced letters
        for index,_ in enumerate(word):
            if guess[index] != 0:
                if freq[alphabet.index(guess[index])] > 0:
                    output[index] = [guess[index], 2]
                    freq[alphabet.index(guess[index])] -= 1
                else:
                    output[index]=[guess[index],0]
        return output
