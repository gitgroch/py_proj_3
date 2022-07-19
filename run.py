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
    word_index = random.randint(0, len(word_list) -1)
    # store a random index for list in variable
    return word_list[word_index]
    # return the elementin list at the random index stored
    print(word_list)

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
    for letter in missed_letters:
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

def get_guess(already_guessed):
    # returns letter entered by player. Handles invalid input 
    while True :
        print("Guess a letter.")
        guess = input()
        guess = guess.lower()
        # ask player for letter, convert to lower case 
        if len(guess) != 1:
            print('Please enter a single letter')
        elif guess in already_guessed:
            print('Oops! You have already guessed that letter! Please try again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Oops! That does not seem to be a letter, please try again using a letter.!')
        else: 
            return guess

def play_again():
# asks player to play again, take input and validate if starts with 'y'
    print('Would you like to play again? (yes or no)')
    return input().lower().startswith('y')


# GAME LOOP 
print('H A N G M A N')
missed_letters = ''
correct_letters = ''
secret_word = get_random_word(words)
game_done = False

while True: 
    display_board(missed_letters, correct_letters, secret_word)
    # call display board function with defined variables 
    guess = get_guess(missed_letters + correct_letters)
    # call get guess function, concate missed letetr and correct letters for already_guessed 
    if guess in secret_word:
        # check if guess letter is in game word  
        correct_letters = correct_letters + guess
        # if tru concate correct_letters and guess 

        # Win Condition 
        found_all_letters = True 
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                found_all_letters = False
                break 
        if found_all_letters:
            print(f"Yes, the word is {secret_word} , You won! ")
            game_done = True 
    else:
        missed_letters = missed_letters + guess

        if len(missed_letters) == len(HANGMAN_PICS) -1:
            display_board(missed_letters, correct_letters, secret_word)
            print(f"You have run out of guesses!\n After {str(len(missed_letters))} missed guesses and {str(len(correct_letters))} correct guesses. The word was {secret_word}")
            game_done = True    

    if game_done:
        if play_again():
            missed_letters = ''
            correct_letters = ''
            game_done = False
            secret_word = get_random_word(words)
        else:
            break



