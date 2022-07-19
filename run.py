import random

# constant variable for hangman progress art ast a list
HANGMAN_PICS = ['''
    +---+
        |
        |
        |
        ===''', '''
    +---+
    O   |
        |
        |
        ===''', '''
    O   |
    |   |
        |
        ===''', '''
    O   |
   /|   |
        |
        ===''', '''
    O   |
   /|\  |
        |
        ===''', '''
    O   |
   /|\  |
   /    |
        ===''', '''
    O   |
   /|\  |
   / \  |
        ===''']
    
words = 'aluminium key giant location drawing ignorance cancer establish prosper learn print gravity joint architect charge exaggerate state dorm piano'.split()


def getRandomWord(wordList):
    '''
    Returns a random word (string) from a word list
    '''
    wordIndex = random.randint(0, len(wordList) -1)
    # store a random index for list in variable 
    return wordList[wordIndex]
    # return the elementin list at the random index stored 
    print(wordList)

print(getRandomWord(words))


