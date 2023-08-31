#   vim-modelines:  {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
import math
import pprint

class Solution:

    #   runtime: beats 93%
    def solveSudoku(self, board):
        self.setBoard(board)
        self.solve_backtracking()
        return self.board

    def setBoard(self, board):
        self.board = board

    def solve_backtracking(self):
        """Backtracking solution, fill next empty square with each possible option and recurse"""
        #   for next unassigned square
        row, col = self.findUnassigned()
        if row == -1 and col == -1:
            return True
        #   try to fill that square for each possible value
        options = self.options(row, col)
        for i in options:
            #   attempt to place each possible value, backtracking if unsucessful
            self.board[row][col] = i
            result = self.solve_backtracking()
            if result == True:
                return True
            self.board[row][col] = '.'
        #   If we failed to place a value, problem must be unsolveable for current board
        return False

    def findUnassigned(self):
        """Find coordinates of the empty square with the least possible options"""
        best = (-1, -1)
        best_options_len = math.inf
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == '.':
                    options = self.options(row, col)
                    if len(options) == 1:
                        return (row, col)
                    elif len(options) < best_options_len:
                        best_options_len = len(options)
                        best = (row, col)
        return best

    def options(self, row, col):
        """Get available values for a given (empty) square"""
        options_row = self.options_checkrow(row)
        options_col = self.options_checkcol(col)
        options_sector = self.options_checksector(row, col)
        return options_row & options_col & options_sector

    def options_checkrow(self, row):
        """Get available values for a given row"""
        options = set( [str(i) for i in range(1, 10) ] )
        for loop_col in range(9):
            val = self.board[row][loop_col]
            if val != '.':
                options.remove(val)
        return options

    def options_checkcol(self, col):
        """Get available values for a given col"""
        options = set( [str(i) for i in range(1, 10) ] )
        for loop_row in range(9):
            val = self.board[loop_row][col]
            if val != '.':
                options.remove(val)
        return options

    def options_checksector(self, row, col):
        """Get available values for a given (3x3) sector"""
        sector_row = row - row % 3
        sector_col = col - col % 3 
        options = set( [str(i) for i in range(1, 10) ] )
        for loop_row in range(sector_row, sector_row+3):
            for loop_col in range(sector_col, sector_col+3):
                val = self.board[loop_row][loop_col]
                if val != '.':
                    options.remove(val)
        return options


s = Solution()
test_functions = [ s.solveSudoku, ]

inputs = [
    [ ['.','.','9','7','4','8','.','.','.'], ['7','.','.','.','.','.','.','.','.'], ['.','2','.','1','.','9','.','.','.'], ['.','.','7','.','.','.','2','4','.'], ['.','6','4','.','1','.','5','9','.'], ['.','9','8','.','.','.','3','.','.'], ['.','.','.','8','.','3','.','2','.'], ['.','.','.','.','.','.','.','.','6'], ['.','.','.','2','7','5','9','.','.'], ],
    [ ['.','6','.','8','.','.','5','.','.'], ['.','.','5','.','.','.','3','6','7'], ['3','7','.','.','6','5','8','.','9'], ['6','.','9','.','.','2','1','.','.'], ['.','.','1','4','8','9','2','.','.'], ['.','.','.','3','.','6','9','.','.'], ['.','5','.','.','.','.','4','.','.'], ['.','1','.','5','4','7','.','.','3'], ['.','9','6','.','3','8','.','5','1'], ],
]
checks = [ 
    [ ['5', '1', '9', '7', '4', '8', '6', '3', '2'], ['7', '8', '3', '6', '5', '2', '4', '1', '9'], ['4', '2', '6', '1', '3', '9', '8', '7', '5'], ['3', '5', '7', '9', '8', '6', '2', '4', '1'], ['2', '6', '4', '3', '1', '7', '5', '9', '8'], ['1', '9', '8', '5', '2', '4', '3', '6', '7'], ['9', '7', '5', '8', '6', '3', '1', '2', '4'], ['8', '3', '2', '4', '9', '1', '7', '5', '6'], ['6', '4', '1', '2', '7', '5', '9', '8', '3'] ],
   [ ['9', '6', '2', '8', '7', '3', '5', '1', '4'], ['1', '8', '5', '9', '2', '4', '3', '6', '7'], ['3', '7', '4', '1', '6', '5', '8', '2', '9'], ['6', '4', '9', '7', '5', '2', '1', '3', '8'], ['5', '3', '1', '4', '8', '9', '2', '7', '6'], ['8', '2', '7', '3', '1', '6', '9', '4', '5'], ['7', '5', '3', '6', '9', '1', '4', '8', '2'], ['2', '1', '8', '5', '4', '7', '6', '9', '3'], ['4', '9', '6', '2', '3', '8', '7', '5', '1'] ],
]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    for board, check in zip(inputs, checks):
        print("board:")
        pprint.pprint(board)
        start_time = time.time()
        result = f(board)
        end_time = time.time()
        print("result:")
        pprint.pprint(result)
        assert result == check, "Check comparison failed"
        print("elapsed_us=(%0.2f)" % ((end_time - start_time) * 1_000_000))
    print()

