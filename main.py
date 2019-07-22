from state import *
from solver import *

# Taken from https://www.youtube.com/watch?v=LzxKkoeXLRo
initial_board = np.array([
[0, 8, 0, 0, 0, 6, 0, 0, 3],
[0, 6, 0, 0, 7, 0, 2, 0, 0],
[0, 0, 4, 0, 1, 0, 0, 9, 0],
[0, 5, 0, 0, 0, 0, 8, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 3, 0, 0, 0, 0, 6, 0],
[0, 0, 5, 0, 0, 9, 0, 0, 8],
[0, 0, 0, 0, 2, 0, 0, 0, 0],
[0, 0, 6, 7, 0, 0, 3, 0, 2]
])

print('Initial Sudoku:')
initial_state = State(initial_board)
initial_state.print_state()

# Solve using backtracking
backtracking(initial_state)
