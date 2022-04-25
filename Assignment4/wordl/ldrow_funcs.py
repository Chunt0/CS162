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
    answer=[]
    for index in range(5):
        if word[index] == guess[index]:
            check = (guess[index], 1)
        elif (word[index] != guess[index] and word.count(guess[index]) > 0):
            check = (guess[index], 2)
        elif (word.count(guess[index]) == 0):
            check = (guess[index], 0)
        else:
            check = "ERROR"
        answer.append(check)
        
    return answer

# wordlist_path = "/home/chunt/Code/CS162/Assignment4/wordl/wordlist.txt"
# wordlist = get_wordlist(wordlist_path)

# print(wordlist[145])
# guess = input("Guess: ")
# solution = match_word(wordlist[145], guess)
# print(solution)