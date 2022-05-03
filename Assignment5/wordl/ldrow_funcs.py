# Christopher Hunt
# CS162
# LDROW FUNCTIONS

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
    answer = []

    word_alpha_count = alpha_count(word)
    guess_alpha_count = alpha_count(guess)
    
   # Check if guess letter matchs or is in word letter
    for index in range(5):
        letter_count = word.count(guess[index])
        if word[index] == guess[index]:
            check = [guess[index], 1]
        elif word[index] != guess[index] and letter_count > 0:
            check = [guess[index], 2]
        elif (letter_count == 0):
            check = [guess[index], 0]
        else:
            check = ["", 0]
            print("ERROR")
        answer.append(check)

    # Figure out how to deal with doubles and wrong positions
    # This whole section feels like a mess... Maybe someone can help clean it up?
    for i in range(0,len(word_alpha_count)):
        # Check for condition where the error occurs
        if guess_alpha_count[i][1] > 1 and word_alpha_count[i][1] > 0 and guess_alpha_count[i][1] != word_alpha_count[i][1]:
            # Find if the first instance is yellow, if yes, then is second yellow or green? if yellow discard if green discard the first
            diff = guess_alpha_count[i][1] - word_alpha_count[i][1]
            letter_to_fix = guess_alpha_count[i][0]
            index = 0
            while diff > 0 and index < 5:
                if word[index] == guess[index] and guess[index] == letter_to_fix and answer[index][1] == 1:
                    pass
                elif word[index] != guess[index] and guess[index] == letter_to_fix and answer[index][1] != 1:
                    answer[index][1] = 0
                    guess_alpha_count[i][1] -= 1
                diff = guess_alpha_count[i][1] - word_alpha_count[i][1]
                index += 1

    return answer

def alpha_count(word):
    # Alphabet Checklist
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    count = [0] * len(alpha)
    temp_alpha_count =list(zip(alpha,count)) 
    alpha_count = []
    for letter in temp_alpha_count:
        alpha_count.append(list(letter))

    for letter in alpha_count:
        for char in word:
            if letter[0] == char:
                letter[1] += 1
    return alpha_count

