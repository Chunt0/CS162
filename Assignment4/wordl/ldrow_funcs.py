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

def matches(word, guess):
    pass


wordlist_path = "/home/chunt/Code/CS162/Assignment4/wordl/wordlist.txt"
wordlist = get_wordlist(wordlist_path)
print(wordlist)