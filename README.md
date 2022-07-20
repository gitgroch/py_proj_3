# HangPy

![screenshot of site from https://ui.dev/amiresponsive.](/assets/images/amiresponsive.jpg)

HangPy is a Python terminal game, which runs in the the Code Institute mock terminal on Heroku.

Users will be asked to guess letters in a game word before they run out of chances.

Here is the latest version of [HangPy](https://gr-hang-py.herokuapp.com/) 

## How to Play

HangPy follows the game structure of the classic game Hangman.

When the player loads the game, they can choose a difficulty setting:
    - Easy will give the player 8 guess
    - Medium will give the player  6 guesses
    - Hard will give the player  4 guesses

The player will then see the game board which will show them an empty gallows along with a series of underscores (_) representing the hidden game word.

The player can guess a letter to see if it is in the game word.

If the player guesses correctly, the letter they guesses will appear in it's correct place in the hidden game word.

If the player guesses incorrectly, a body part will be added to the gallows, indicating that they've used up one of their chances.

This loop continues as the user guesses more letters. If the user runs our of guesses, the player loses, the gallows will fill up and the game will end.

If the user guesses all the letters in the hidden game word, the player wins and the game will end.

## **Overview**

### User Stories:

- As a game player I want to have clear instructions and ruleset.
- As a player I want the game flow to make sense so that I understand what I need to do.
- As a player I want feedback so that I know what impact my actions are having on the game.
- As a player of casual games I want to be able to jump back into a game when the first one ends.

### Target Audience:

- Fans of word games.
- Fans of nostolgic command prompt games.
- People who want to play a quick game for enjoyment.

### The purpose of the program is to provide the above target users with:

- A quick and fun game with plenty of feedback. 
- A game loop that is fun and engaing and will make them want to play again. 

## **Planning** 

I began by quickly planning out what functions I thought the game would need and what they would need to do. I did this at a highlevel in a word document:

![screenshot of function planning.](/assets/images/function_planning.jpg)

### **Flow Chart** 

I took these elements and created a flow chart using [draw.io](https://www.draw.io) to better understand how the functions would work in the program:

![screenshot of flow chart.](/assets/images/hangpyflow.png)


### Features



### Future Features

## Data Model

## Testing
### Bugs

### Validator Testing

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

- Steps for deployment:
    - Forked the repository
    - Create new Heroku App
    - Set the buildbacks to Python and NodeJS in that order
    - Link the Heroku to the GitHub repository
    - Click on Deploy

## Credits

