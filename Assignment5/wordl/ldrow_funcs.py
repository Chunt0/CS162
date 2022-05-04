# Christopher Hunt
# CS162
# LDROW FUNCTIONS

import string

def get_wordlist(path_to_wordlist):

    with open(path_to_wordlist) as wlist:
        wordlist_temp = wlist.readlines()

    wordlist = []
    for word in wordlist_temp:
        word = word.replace('\n','')
        wordlist.append(word)

    return wordlist

def match_word(word, guess):
    # Format guess and word, make answer list
    guess = guess.upper()
    word = word.upper()

    freq = [0] * 26
    alphabet = string.ascii_uppercase
    output = [['',0],['',0],['',0],['',0],['',0],]

    for index1 in range(0, 5):
      for index2 in range(0, len(alphabet)):
        if word[index1] == alphabet[index2]:
          freq[index2]+=1
                
    guess = [char for char in guess] #splitting the guess into a list of chars for manipulation purposes

        #check not a match or exact match
    for index in range(0, len(word)):
          
        if guess[index] not in word:
            output[index] = [guess[index], 0]
        
        elif word[index] == guess[index]:
            output[index] = [guess[index], 1]
            freq[alphabet.index(guess[index])] -=1 #decrement our list of freqs
            guess[index] = 0 #set this letter to 0


    #now we'll do a seperate loop to deal with multiple/misplaced letters
    for index in range(0, len(word)):
        if guess[index] != 0:
            if freq[alphabet.index(guess[index])] > 0:
                output[index] = [guess[index], 2]
                freq[alphabet.index(guess[index])] -=1
            else:
                output[index]=[guess[index],0]
                 
    return output
