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
    guess = guess.upper()
    word = word.upper()
    answer = []
    for index in range(5):
        letter_count = word.count(guess[index])
        if word[index] == guess[index]:
            check = (guess[index], 1)
        elif word[index] != guess[index] and letter_count > 0:
            check = (guess[index], 2)
        elif (letter_count == 0):
            check = (guess[index], 0)
        else:
            check = ("", 0)
            print("ERROR")
        answer.append(check)
    return answer
