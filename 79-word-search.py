#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
from typing import List
#   {{{2
class Solution:

    #   runtime: beats 65%
    def exist_Backtrack(self, board: List[List[str]], word: str) -> bool:
        """Determine if 'word' exists in 'board'"""
        self.result = False

        #   insight: pass remainder of word to be searched for as 'suffix', replace visited squares on board with '*'
        def backtrack(row, col, suffix):
            #   suffix is empty -> we have arrived on final square of word
            if len(suffix) == 0:
                self.result = True
                return
            if self.result:
                return
            #   visit each valid adjacent square
            directions = [ (-1,0), (1,0), (0,-1), (0,1), ]
            for delta_row, delta_col in directions:
                if delta_row+row < 0 or delta_row+row >= len(board):
                    continue
                if delta_col+col < 0 or delta_col+col >= len(board[row]):
                    continue
                #   only continue if square matches first character of 'suffix'
                if board[row+delta_row][col+delta_col] != suffix[0]:
                    continue
                #   Denote the current square as visited, and continue backtracking from next square, with first char of 'suffix' removed
                temp = board[row][col]
                board[row][col] = '*'
                backtrack(row+delta_row, col+delta_col, suffix[1:])
                board[row][col] = temp

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == word[0]:
                    backtrack(row, col, word[1:])
                if self.result == True:
                    return True

        return self.result


s = Solution()
test_functions = [ s.exist_Backtrack, ]

input_values = [ ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"), ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"), ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"), ([["a"]], "a"), ]
input_checks = [ True, True, False, True, ]

for test_func in test_functions:
    print(test_func.__name__)
    for (board, word), check in zip(input_values, input_checks):
        print("word=(%s), board=(%s)" % (word, board))
        result = test_func(board, word)
        print("result=(%s)" % result)
        assert result == check, "Check failed"
    print()

