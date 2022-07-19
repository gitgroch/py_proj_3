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


def get_random_word(word_list):
    '''
    Returns a random word (string) from a word list
    '''
    word_index = random.randint(0, len(wordList) -1)
    # store a random index for list in variable 
    return word_list[word_index]
    # return the elementin list at the random index stored 
    print(wordList)

def display_board(missed_letters, correct_letters, secret_word):
    '''
    Display game interface, 
    show correct guesses, letters guessed incorrectly and hangman progress
    '''
    print(HANGMAN_PICS[len(missed_letters)])
    # display hangman progress based on the lenght of missed letters 
    print()

    print("Missed letters:", end=' ')
    # prints message with a space at the end rather than moving to new line 
    for letters in missed_letters:
        # iterate through each letter in missedLetters and print
        print(letter, end=' ')
    print()

    blanks = '_' * len(secret_word)
    # create blanks for secret word based on lenght of secretWord variable 

    for i in range(len(secret_word)):
    # iterate through secretWord, replace blanks with letters at their index if in correct letters
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]
    
    for letter in blanks:
    # show game word with spaces between each letter 
        print(letter, end=' ')
    print()



