# Word Unscramble Game

## Project Description

The Word Unscramble Game is an interactive word puzzle game where players rearrange shuffled letters to form meaningful words. The game tracks the player's score and provides feedback on their guesses. Players have the option to continue playing after reaching a certain number of incorrect guesses.

## Features

1. **Word Selection and Shuffling**
   - Randomly selects a word from a predefined list.
   - Shuffles the letters of the selected word and presents them to the player.

2. **User Input and Validation**
   - Allows the player to input their guess for the original word.
   - Validates the player's guess against the correct word.

3. **Scoring System**
   - Awards points for correct guesses.
   - Tracks the number of incorrect guesses.

4. **Game Over and Restart**
   - Ends the game after a set number of incorrect guesses.
   - Asks the player if they want to continue or exit when the game is over.
   - Resets the score and incorrect guess counter if the player chooses to continue.

5. **Graphical Interface (Optional)**
   - Uses Pygame to create a graphical interface for the game.
   - Displays shuffled letters, player input, score, and game status on the screen.
   - Provides an interactive prompt for restarting the game.

## Installation

### Prerequisites

- Python 3.x
- (Optional) Pygame library

### Steps

1. Clone the repository:
   ```sh
   git clone https://github.com/word-unscramble-game.git
   cd word-unscramble-game
