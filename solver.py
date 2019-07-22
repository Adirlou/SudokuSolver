from state import *
import os, time

def backtracking(state, animation=False):
    """
    Backtracking algorithm (DFS) to solve the Sudoku board
    """

    # If animation is on, print the current board, wait, and clear screen
    if animation:
        state.print_state()
        time.sleep(0.05)
        os.system('clear')

    # If state is final, we have a solution, print it
    if state.is_final():
        print('Solution:')
        state.print_state()
        return state

    # Find the next empty spot
    row_empty, col_empty = state.find_empty()

    # Compute the available moves at this spot
    available_moves = state.possible_moves(row_empty, col_empty)

    # For each available move
    for i in available_moves:

        # Compute the next state
        next_state = state.nextState((row_empty, col_empty, i))

        # Recurse, and if successful, return the next state computed
        if backtracking(next_state, animation):
            return next_state

    return None
