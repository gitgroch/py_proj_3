# HangPy

![screenshot of the project from https://ui.dev/amiresponsive.](/assets/images/amiresponsive.jpg)

HangPy is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.

Users will be asked to guess letters in a game word before they run out of chances.

Here is the latest version of [HangPy](https://gr-hang-py.herokuapp.com/) 

## How to Play

HangPy follows the game structure of the classic game Hangman.

When the player loads the game, they can choose a difficulty setting:
    - Easy will give the player 8 guess
    - Medium will give the player  6 guesses
    - Hard will give the player  4 guesses

The player will then see the game board which will show the empty gallows along with a series of underscores (_) representing the hidden game word.

The player can guess a letter to see if it is in the game word.

If the player guesses correctly, the letter they guesses will appear in its correct place in the hidden game word.

If the player guesses incorrectly, a body part will be added to the gallows, indicating that they've used up one of their chances.

This loop continues as the user guesses more letters. If the user runs out of guesses, the player loses, the gallows will fill up and the game will end.

If the user guesses all the letters in the hidden game word, the player wins and the game will end.

## **Overview**

### User Stories:

- As a game player, I want to have clear instructions and a ruleset.
- As a player, I want the game flow to make sense so that I understand what I need to do.
- As a player, I want feedback so that I know what impact my actions are having on the game.
- As a player of casual games I want to be able to jump back into a game when the first one ends.

### Target Audience:

- Fans of word games.
- Fans of nostalgic command prompt games.
- People who want to play a quick game for enjoyment.

### The purpose of the program is to provide the above target users with:

- A quick and fun game with plenty of feedback. 
- A game loop that is fun and engaging and will make them want to play again. 

## **Planning** 

I began by quickly planning out what functions I thought the game would need and what they would need to do. I did this at a high level in a word document:

![screenshot of function planning.](/assets/images/function_planning.jpg)

### **Flow Chart** 

I took these elements and created a flow chart using [draw.io](https://www.draw.io) to better understand how the functions would work in the program:

![screenshot of flow chart.](/assets/images/hangpyflow.png)


### Features

#### Rules 

When the player loads the game they can choose to view the rules.

![screenshot of the rules .](/assets/images/rules.jpg)

#### Difficulty 

Next, the player can choose their difficulty setting:

![screenshot of the difficulty choice.](/assets/images/difficulty.jpg)

#### Game Board 

The player is presented with the game board. It is an empty gallows with blanks representing the hidden word.

![screenshot of the gameboard.](/assets/images/gameboard.jpg)

#### Guessing 

The player can then make a guess by entering a letter on their keyboard. 
- If they guess correctly the letter will display in its correct place in the game word:

![screenshot of a correct guess .](/assets/images/correct_guess.jpg)

- if the player guesses incorrectly, the gallows art will update with a body part. The letter that they guessed incorrectly will be added to the list of Missed Letters.

![screenshot of an incorrect guess.](/assets/images/missed.jpg)

#### Winning and Losing 

- If the player guesses all the letters correctly they win the game.
- The console will show the user how many missed and correct guesses they made in
 the game.

![screenshot of the win state.](/assets/images/win.jpg)

- If the player runs out of chances without guessing the word, they lose the game.
- The console will show the user how many missed and correct guesses they made in the game.
- The console will also show the hidden game word. 

![screenshot of the lose state.](/assets/images/lose.jpg)

#### Play Again 

Regardless of if the player won or lost the game, they can choose to play again or close the program.

#### Error Validation 

The player is notified and prompted to re-enter their choice if their input is invalid. This occurs wherever a choice is required. 

![screenshot of the lose state.](/assets/images/error_validation.jpg)

### Future Features

- Replace hangman imagery with something more original.
- Add the ability to choose different word categories and lengths.
- Add more nuance to the difficulty setting (e.g. Longer or harder words).


## Testing

I have manually tested the game by doing the following: 
- Passed the code through PEP8 linter and confirmed there are no errors.
- Tested error validation by entering invalid inputs.
- Tested on my local terminal and on the Code Institute Heroku Terminal

### Bugs

#### Solved Bugs

- In the difficulty_choice function The statement in the print function for my else condition ran regardless of what the input was. 
    - I had 2 If statements, changing one to elif solved this issue. 

- In the difficulty_choice function, when the else statement condition was met, it did not loop back to the start, rather it proceeded to the next part of the start_game function.
    - Added the continue python continue keyword. 


### Remaining Bugs 

- There are no bugs remaining
## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

- Steps for deployment:
    - Forked the repository
    - Create new Heroku App
    - Set the buildbacks to Python and NodeJS in that order
    - Link the Heroku to the GitHub repository
    - Click on Deploy

## Credits

- A large part of the initial structure for this game came from the book ["Invent your own computer games with Python, 4th Edition" By Al Sweigart](https://inventwithpython.com/)
- Word list courtesy of [Randomw Word Generator](https://randomwordgenerator.com/)
- ASCII Art courtesy of [Ascii Art Generator](https://www.ascii-art-generator.org/)
- Help with If/Else Statements [Problem Solving With Python ](https://problemsolvingwithpython.com/08-If-Else-Try-Except/08.04-If-Else-Statements)
- Help with opening a file and making it a list [admamsmith.haus](https://www.adamsmith.haus/python/answers/how-to-read-a-text-file-into-a-list-in-python)
