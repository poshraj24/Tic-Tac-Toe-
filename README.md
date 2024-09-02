# Tic-Tac-Toe Game with Minimax AI
## Initial Implementation: Python Implementation
## Final Implementation: Integration onto andorid app (Ongoing)
This is a Python implementation of the classic Tic-Tac-Toe game, featuring a human player vs. AI opponent. The AI uses the Minimax algorithm to determine the best possible move. The code is structured using Object-Oriented Programming (OOP) principles, encapsulating the game logic within a single class.

## How It Works

### Overview

The game is played on a 3x3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game. This implementation allows a human player to compete against an AI. The AI is powered by the Minimax algorithm, which ensures that it plays optimally.

## Class and Methods

### `TicTacToe` Class

The `TicTacToe` class contains all the necessary methods and attributes to manage the game, including the game board, player moves, and AI decision-making.

#### `__init__()`

- **Purpose**: Initializes a new game board, represented by a 3x3 list of lists filled with spaces (`' '`).
- **Usage**: Automatically called when a `TicTacToe` object is created.

#### `print_board()`

- **Purpose**: Displays the current state of the game board to the console.
- **Details**: Each row of the board is printed with vertical separators (`|`), and a line of dashes (`-----`) is printed between rows to visually separate them.

#### `check_winner(player)`

- **Purpose**: Checks if the specified player (`'X'` for human or `'O'` for AI) has won the game.
- **Details**: The method checks all possible winning combinations—rows, columns, and diagonals.
- **Returns**: `True` if the player has won, otherwise `False`.

#### `check_draw()`

- **Purpose**: Determines if the game has ended in a draw.
- **Details**: The method checks if there are no empty spaces left on the board and no winner has been determined.
- **Returns**: `True` if the game is a draw, otherwise `False`.

#### `minimax(depth, is_maximizing)`

- **Purpose**: Implements the Minimax algorithm to evaluate the best move for the AI.
- **Parameters**:
  - `depth`: Represents the depth of the recursive call, which corresponds to the number of moves made after the current position.
  - `is_maximizing`: A boolean indicating whether the current move is for the maximizing player (AI) or minimizing player (human).
- **Details**:
  - The algorithm recursively explores all possible game states.
  - It assigns a score to each terminal state (win, loss, draw) and propagates the scores back up the recursion tree to select the optimal move.
- **Returns**: The best score for the current player.

#### `find_best_move()`

- **Purpose**: Finds the best move for the AI by evaluating all possible moves using the `minimax` method.
- **Details**: Iterates over all empty spaces on the board, simulates each move, and uses the Minimax algorithm to determine the move's score.
- **Returns**: A tuple `(i, j)` representing the row and column of the best move.

#### `human_move()`

- **Purpose**: Allows the human player to make a move.
- **Details**: The method prompts the player to input the row and column where they want to place their mark (`'X'`), validates the input, and updates the board.

#### `play_game()`

- **Purpose**: Manages the flow of the game, alternating between the human player and the AI until the game is won or ends in a draw.
- **Details**:
  - Prints the board after each move.
  - Checks for a winner or draw after each move.
  - Declares the result (win/loss/draw) and ends the game.
