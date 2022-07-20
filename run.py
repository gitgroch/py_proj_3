import random

# constant variable for hangman progress art as a list
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
    +---+
    O   |
    |   |
        |
        ===''', '''
    +---+
    O   |
   /|   |
        |
        ===''', '''
    +---+
    O   |
   /|\  |
        |
        ===''', '''
    +---+
    O   |
   /|\  |
   /    |
        ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
        ===''', '''
    +---+
    O   |
   /|\  |
  _/ \_ |
        ===''', '''
    +---+
    O   |
  _/|\_ |
  _/ \_ |
        ===''']

# Open word list file, read it, make it a list
word_file = open("word_list.txt", "r")
word_content = word_file.read()
words = word_content.split()


def get_random_word(word_list):
    '''
    Returns a random word (string) from a word list
    ''' 
    word_index = random.randint(0, len(word_list) - 1)
    # store a random index for list in variable
    return word_list[word_index]
    # return the elementin list at the random index stored


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
        # iterate through secretWord, replace blanks with 
        # letters at their index if in correct letters
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]
  
    for letter in blanks:
        # show game word with spaces between each letter
        print(letter, end=' ')
    print()


def get_guess(already_guessed):
    # returns letter entered by player. Handles invalid input 
    while True:
        print("Guess a letter.")
        guess = input()
        guess = guess.lower()
        # ask player for letter, convert to lower case 
        if len(guess) != 1:
            print('Please enter a single letter')
        elif guess in already_guessed:
            print('Oops! You have already guessed\
 that letter! Please try again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Oops! That does not seem to be a letter,\
 please try again using a letter!')
        else: 
            return guess


def play_again():
    '''
    Asks player to play again, take input and validate if starts with 'y'
    '''
    print('Would you like to play again? (yes or no)')
    return input().lower().startswith('y')


def start_game():
    '''
    Function for main game loop.
    Calls rules and difficulty choice fnctions, 
    begins game and runs until end conditions are met.
    '''
    # GAME LOOP 
    print('''                          
    |_|  /\  |\ | /__ |\/|  /\  |\ | 
    | | /--\ | \| \_| |  | /--\ | \| 
    ''')

    # Call rules and difficulty functions before starting game loop
    rules()
    difficulty_choice()
    # define variables for game loop
    missed_letters = ''
    correct_letters = ''
    secret_word = get_random_word(words)
    GAME_DONE = False
   
    while True: 
        display_board(missed_letters, correct_letters, secret_word)
        # call display board function with defined variables 
        guess = get_guess(missed_letters + correct_letters)
        # call get guess function, concate missed letter
        # and correct letters for already_guessed 
        if guess in secret_word:
            # check if guess letter is in game word  
            correct_letters = correct_letters + guess
            # if true concate correct_letters and guess 
            # Win Condition 
            found_all_letters = True 
            for i in range(len(secret_word)):
                # sets found_all_letters to false if all 
                # correct letters not present
                if secret_word[i] not in correct_letters:
                    found_all_letters = False
                    break 
            if found_all_letters:
                # win state
                print(f"\nYes, the word is {secret_word} , You won!\n\
You had {str(len(missed_letters))} missed guesses,\
 and {str(len(correct_letters))} correct guesses.\n")
                GAME_DONE = True 
        else:
            # lose state
            missed_letters = missed_letters + guess
            if len(missed_letters) == len(HANGMAN_PICS) - 1:
                display_board(missed_letters, correct_letters, secret_word)
                print(f"You have run out of guesses!\n\
You had {str(len(missed_letters))} missed guesses,\
 and {str(len(correct_letters))} correct guesses.\n \
The word was {secret_word}.\n")
                GAME_DONE = True    

        if GAME_DONE:
            if play_again():
                # resets game state
                missed_letters = ''
                correct_letters = ''
                GAME_DONE = False
                secret_word = get_random_word(words)
            else:
                break


def difficulty_choice():
    '''
    Allows player to choose difficulty. 
    M will remove 2 list elements from HANGMAN_PICS.
    H will remove 4 elements
    Handles error for invalid input
    '''
    difficulty = ' '
    while difficulty not in 'EMH':
        print('Choose your difficulty: E - Easy, M - Medium, H - Hard')
        difficulty = input().upper()
        if difficulty == 'M':
            del HANGMAN_PICS[8]
            del HANGMAN_PICS[7]
            print("Medium it is!")
        elif difficulty == 'H':
            del HANGMAN_PICS[8]
            del HANGMAN_PICS[7]
            del HANGMAN_PICS[5]
            del HANGMAN_PICS[3]
            print("Hard it is!")
        else:
            print("Please choose a difficulty")
            continue


def rules():
    '''
    Asks player if they wish to see rules. 
    If Y, shows rules 
    '''
    print('Would you like to see the rules? (Y or N)')
    choice = input().upper()
    if choice == 'Y':
        show_rules()
    elif choice == 'N':
        print()
    else:
        print('Please type either Y or N')
        rules()


def show_rules():
    '''
    Function to hold the rules of the game.
    '''
    print('Hangman is a simple word guessing game.\n\
First choose your difficulty:\n\
\
    - Easy will give you 8 guess\n\
    - Medium will give you 6 guesses\n\
    - Hard will give you 4 guesses\n\
\
Next you will see the game board\
and a set of blanks representing the hidden word.\n\
Make a guess by entering a letter with\
your keyboard and hit enter.\n\
If you guess a letter in the game word,\n\
it will appear on the game board and you can guess again.\n\
If you make an incorrect guess,\n\
a body part will be added\
to the gameboard gallows.\n\
If you run out of guesses, the gameboard\n\
fills out all the body parts and you lose the game.\n\
If you guess all the letters correctly, you win!\n')


start_game()