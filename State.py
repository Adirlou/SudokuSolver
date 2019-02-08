import numpy as np

# Found on https://stackoverflow.com/questions/26648781/python-get-subarrays-of-3d-array
def blockshaped(arr, nrows, ncols):
    """
    Return an array of shape (n, nrows, ncols) where
    n * nrows * ncols = arr.size

    If arr is a 2D array, the returned array should look like n subblocks with
    each subblock preserving the "physical" layout of arr.
    """
    h, w = arr.shape
    return (arr.reshape(h//nrows, nrows, -1, ncols)
               .swapaxes(1,2)
               .reshape(-1, nrows, ncols))

class State:
    def __init__(self, state=None):
        if state is not None:
            self.state = state
        else:
            self.state = np.zeros((9, 9), dtype='int')

    def print_state(self):
        """
        Print the state, i.e. the board of the sudoku
        game
        """
        print("-"*37)
        for i, row in enumerate(self.state):
            print(("|" + " {}   {}   {} |"*3).format(*[x if x != 0 else " " for x in row]))
            if i == 8:
                print("-"*37)
            elif i % 3 == 2:
                print("|" + "---+"*8 + "---|")
            else:
                print("|" + "   +"*8 + "   |")


    def get_block(self, row, col):
        """
        Given a cell (row and column), returns the 3*3 block
        in which this cell is contained
        """
        # Compute the 3*3 blocks
        blocks = blockshaped(self.state, 3, 3)

        # Compute index of the corresponding block
        ind2d = (row // 3, col // 3)
        ind = ind2d[0] * 3 + ind2d[1]

        return blocks[ind]

    def possible_moves(self, row, col):
        """
        Given a cell (row and column), returns a list of the
        possible moves that can be done at this cell
        """
        poss = []

        # For each number, it is valid if it doesn't appear
        # on the same row, column, or 3*3 block
        for number in range(1, 10):
            if not (number in self.state[row, :] or number in self.state[:, col] or number in self.get_block(row, col)):
                poss.append(number)
        return poss

    def nextState(self, move):
        """
        Given a move (a cell and a number), compute the next state
        """
        row, col, number = move
        next_state = self.state.copy()
        next_state[row, col] = number

        return State(next_state)

    def is_final(self):
        """
        Returns true if the state of the game is final (i.e. the board is complete
        and correct)
        """
        # Sum of a line or row or 3*3 block for a correct board
        total = sum(range(1, 10))

        # Check that all rows sum up to the total
        for row in self.state:
            if row.sum() != total:
                return False

        # Check that all columns sum up to the total
        for col in self.state.T:
            if col.sum() != total:
                return False

        # Check that all 3*3 blocks sum up to the total
        for block in blockshaped(self.state, 3, 3):
            if block.sum() != total:
                return False

        return True

    def find_empty(self):
        """
        Returns the first cell which has no number assigned yet
        """
        return np.unravel_index(np.argmax(self.state == 0), self.state.shape)
