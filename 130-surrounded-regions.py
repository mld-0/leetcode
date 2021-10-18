#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
import pprint
from collections import deque
from typing import List
#   {{{2
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #return self.solve_DFS(board)
        return self.solve_BFS(board)


    #   runtime: beats 98%
    def solve_DFS(self, board: List[List[str]]) -> None:
        """Flip any 'O' that is not on the border, or 4-connected to an 'O' on the border"""

        def DFS(row, col):
            """If square at (row,col) is 'O', set to 'E' and recurse for valid 4-connected adjacent cells"""
            if board[row][col] != 'O':
                return
            board[row][col] = 'E'
            directions = [ (-1,0), (1,0), (0,-1), (0,1), ]
            for delta_row, delta_col in directions:
                if row+delta_row < 0 or row+delta_row >= len(board):
                    continue
                if col+delta_col < 0 or col+delta_col >= len(board[0]):
                    continue
                if board[row+delta_row][col+delta_col] != 'O':
                    continue
                DFS(row+delta_row, col+delta_col)

        #   Perform DFS search on 'O' squares (for each 4-connected 'O' square) on the border, marking squares as 'E'
        for row in range(len(board)):
            DFS(row, 0)
            DFS(row, len(board[0])-1)
            
        for col in range(len(board[0])):
            DFS(0, col)
            DFS(len(board)-1, col)

        #   Flip any remaining 'O' squares to 'X', and any 'E' squares to 'O'
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                if board[row][col] == 'E':
                    board[row][col] = 'O'



    #   runtime: beats 98%
    def solve_BFS(self, board: List[List[str]]) -> None:
        """Flip any 'O' that is not on the border, or 4-connected to an 'O' on the border"""

        def BFS(row, col):
            if board[row][col] != 'O':
                return
            directions = [ (-1,0), (1,0), (0,-1), (0,1), ]
            queue = deque( [ (row,col) ] )
            while len(queue) > 0:
                row, col = queue.popleft()
                if board[row][col] != 'O':
                    continue
                board[row][col] = 'E'
                for delta_row, delta_col in directions:
                    if row+delta_row < 0 or row+delta_row >= len(board):
                        continue
                    if col+delta_col < 0 or col+delta_col >= len(board[0]):
                        continue
                    if board[row+delta_row][col+delta_col] != 'O':
                        continue
                    queue.append( (row+delta_row, col+delta_col) )

        #   Perform DFS search on 'O' squares (for each 4-connected 'O' square) on the border, marking squares as 'E'
        for row in range(len(board)):
            BFS(row, 0)
            BFS(row, len(board[0])-1)
            
        for col in range(len(board[0])):
            BFS(0, col)
            BFS(len(board)-1, col)

        #   Flip any remaining 'O' squares to 'X', and any 'E' squares to 'O'
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                if board[row][col] == 'E':
                    board[row][col] = 'O'


s = Solution()

input_values = [ [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]], [["X"]], [["X","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"],["O","X","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","O","X","X"],["O","O","O","O","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","X"],["O","O","X","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","X","O"],["O","O","O","O","O","X","O","O","O","O","X","O","O","O","O","O","X","O","O","X"],["X","O","O","O","X","O","O","O","O","O","X","O","X","O","X","O","X","O","X","O"],["O","O","O","O","X","O","O","X","O","O","O","O","O","X","O","O","X","O","O","O"],["X","O","O","O","X","X","X","O","X","O","O","O","O","X","X","O","X","O","O","O"],["O","O","O","O","O","X","X","X","X","O","O","O","O","X","O","O","X","O","O","O"],["X","O","O","O","O","X","O","O","O","O","O","O","X","X","O","O","X","O","O","X"],["O","O","O","O","O","O","O","O","O","O","X","O","O","X","O","O","O","X","O","X"],["O","O","O","O","X","O","X","O","O","X","X","O","O","O","O","O","X","O","O","O"],["X","X","O","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","O","O"],["O","X","O","X","O","O","O","X","O","X","O","O","O","X","O","X","O","X","O","O"],["O","O","X","O","O","O","O","O","O","O","X","O","O","O","O","O","X","O","X","O"],["X","X","O","O","O","O","O","O","O","O","X","O","X","X","O","O","O","X","O","O"],["O","O","X","O","O","O","O","O","O","O","X","O","O","X","O","X","O","X","O","O"],["O","O","O","X","O","O","O","O","O","X","X","X","O","O","X","O","O","O","X","O"],["O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"],["X","O","O","O","O","X","O","O","O","X","X","O","O","X","O","X","O","X","O","O"]], ]
input_checks = [ [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]], [["X"]], [["X","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"], ["O","X","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","O","X","X"], ["O","O","O","O","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","X"], ["O","O","X","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","X","O"], ["O","O","O","O","O","X","O","O","O","O","X","O","O","O","O","O","X","O","O","X"], ["X","O","O","O","X","O","O","O","O","O","X","O","X","O","X","O","X","O","X","O"], ["O","O","O","O","X","O","O","X","O","O","O","O","O","X","O","O","X","O","O","O"], ["X","O","O","O","X","X","X","X","X","O","O","O","O","X","X","O","X","O","O","O"], ["O","O","O","O","O","X","X","X","X","O","O","O","O","X","O","O","X","O","O","O"], ["X","O","O","O","O","X","O","O","O","O","O","O","X","X","O","O","X","O","O","X"], ["O","O","O","O","O","O","O","O","O","O","X","O","O","X","O","O","O","X","O","X"], ["O","O","O","O","X","O","X","O","O","X","X","O","O","O","O","O","X","O","O","O"], ["X","X","O","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","O","O"], ["O","X","O","X","O","O","O","X","O","X","O","O","O","X","O","X","O","X","O","O"], ["O","O","X","O","O","O","O","O","O","O","X","O","O","O","O","O","X","X","X","O"], ["X","X","O","O","O","O","O","O","O","O","X","O","X","X","O","O","O","X","O","O"], ["O","O","X","O","O","O","O","O","O","O","X","O","O","X","O","X","O","X","O","O"], ["O","O","O","X","O","O","O","O","O","X","X","X","O","O","X","O","O","O","X","O"], ["O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"], ["X","O","O","O","O","X","O","O","O","X","X","O","O","X","O","X","O","X","O","O"]], ]

for board, check in zip(input_values, input_checks):
    print("board=(%s)" % board)
    s.solve(board)
    print("result=(%s)" % board)
    assert board == check, "Check failed"
    print()

