# TicTacToe Game with OpenCV

This project is a graphical implementation of the classic Tic-Tac-Toe game using OpenCV in Python. The game features a simple user interface where players can place their moves by clicking on the grid. It also includes buttons for starting a new game, undoing the last move, and quitting the game.

## Features
- **Tic-Tac-Toe Board**: A 3x3 grid for two players to place 'X' and 'O' alternately.
- **Win Condition**: Detects winning patterns (rows, columns, and diagonals) and displays a line through the winning sequence.
- **Buttons**: 
  - `New`: Start a new game.
  - `Back`: Undo the last move.
  - `Quit`: Exit the game.
- **Mouse Interaction**: Players can click inside the game board to place their mark.

## Requirements
To run this project, you will need:
- Python 3.x
- OpenCV (`cv2`)
- NumPy (`numpy`)

You can install the dependencies with:
```
pip install opencv-python numpy
```

## How to Run
1. Clone the repository and navigate to the project directory.
2. Run the script:
   ```bash
   python tic_tac.py
   ```
3. The game window will open:
   - Press `ENTER` to start a new game.
   - Press `Q` to quit.
   - Use the on-screen buttons or click on the grid to play.

## Code Overview

### `is_inside(bbox, point)`
Checks if a point is within a bounding box.

### `TicTacGame` Class
This class handles the game logic, board rendering, and user interaction:
- **Attributes**:
  - `img`: The image (background or blank canvas) on which the game is drawn.
  - `history`: A 3x3 NumPy array storing the game state (`1` for 'O', `-1` for 'X', `0` for empty).
  - `buttons`: Stores the positions and sizes of interactive buttons.
  - `has_win`: Boolean flag to indicate if the game has been won.
  - `quit`: Boolean flag to exit the game loop.
  
- **Methods**:
  - `check_win()`: Checks if there is a winner.
  - `make_table()`: Draws the Tic-Tac-Toe grid.
  - `make_buttons()`: Creates the control buttons.
  - `draw_button()`: Draws individual buttons with their state (clicked or not).
  - `finish_line(case)`: Draws a line over the winning sequence.
  - `update(sign, i, j)`: Updates the game board with a move and checks for a win.
  - `draw_O()`: Draws 'O' on the board.
  - `draw_X()`: Draws 'X' on the board.
  - `get_paste_coord()`: Calculates the coordinates to place the mark.
  - `go_back()`: Reverts the last move.
  - `act(event, x, y, flags, param)`: Handles mouse events (placing marks, clicking buttons).
  - `init_game()`: Initializes the game state and draws the board.
  - `start_game()`: Starts the game loop and listens for inputs.

## Customization
- You can change the background image by replacing the `back_ground.png` file or by loading another image into the `TicTacGame` class.
- Modify the dimensions of the grid or buttons by adjusting the constants in the code.

## Example Usage
```python
if __name__ == "__main__":
    backgr_img = cv.imread('back_ground.png')
    game = TicTacGame(backgr_img)
    game.start_game()
```

## License
This project is licensed under the MIT License.

---

Feel free to fork the repository and contribute any improvements or features!
