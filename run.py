
words = 'aluminium key giant location drawing ignorance cancer establish deficiency prosper learn print gravity joint architect charge exaggerate state dorm piano '

def getRandomWord():
    '''
    Returns a random word (string) from a word list
    '''
    wordIndex = random.randint(0, len(wordList) -1)
    return wordList[wordIndex]

