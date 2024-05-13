#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
import pprint
import math
from typing import List, Optional

class Solution:
    """Given an m x n binary matrix, determine the highest possible score after making any number of moves, a move consists of flipping the bits in a given row or column, and the score is the sum of each row when expressed as a binary number"""

    #   runtime: beats 5%
    #    memory: beats 93%
    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def score_grid() -> int:
            result = 0
            for row in range(m):
                row_value = 0
                for bit in grid[row]:
                    row_value = (row_value << 1) | bit
                result += row_value
            return result

        def score_if_row_flipped(row: int) -> int:
            flip_row(row)
            result = score_grid()
            flip_row(row)
            return result

        def score_if_col_flipped(col: int) -> int:
            flip_col(col)
            result = score_grid()
            flip_col(col)
            return result

        def flip_row(row: int):
            for col in range(n):
                grid[row][col] = 1 - grid[row][col]

        def flip_col(col: int):
            for row in range(m):
                grid[row][col] = 1 - grid[row][col]

        while True:
            current_score = score_grid()
            choice_direction = None
            choice_index = None
            choice_value = current_score
            for row in range(m):
                score = score_if_row_flipped(row)
                if score > choice_value:
                    choice_value = score
                    choice_index = row
                    choice_direction = "row"
            for col in range(n):
                score = score_if_col_flipped(col)
                if score > choice_value:
                    choice_value = score
                    choice_index = col
                    choice_direction = "col"
            if choice_direction == "row":
                flip_row(choice_index)
            elif choice_direction == "col":
                flip_col(choice_index)
            else:
                break

        return current_score


    #   runtime: beats 97%
    #    memory: beats 93%
    def matrixScore_ans_i(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # Set first column
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] = 1 - grid[i][j]  
        # Optimize columns except first column
        for j in range(1, n):
            count_zero = 0
            for i in range(m):
                if grid[i][j] == 0:
                    count_zero += 1
            # Flip the column if more zeros for better score
            if count_zero > m - count_zero:
                for i in range(m):
                    grid[i][j] ^= 1  
        # Calculate the final score considering bit positions
        score = 0
        for i in range(m):
            for j in range(n):
                columnScore = grid[i][j] << (n - j - 1)
                score += columnScore
        return score


    #   runtime: beats 96%
    #    memory: beats 93%
    def matrixScore_ans_ii(self, grid):
        M, N = len(grid), len(grid[0])
        res = (1 << N - 1) * M
        for j in range(1, N):
            cur = sum(grid[i][j] == grid[i][0] for i in range(M))
            res += max(cur, M - cur) * (1 << N - 1 - j)
        return res


s = Solution()
test_functions = [ s.matrixScore, s.matrixScore_ans_i, s.matrixScore_ans_ii, ]

inputs = [ [[0,0,1,1],[1,0,1,0],[1,1,0,0]], [[0]], ]
checks = [ 39, 1, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for grid, check in zip(inputs, checks):
        print(f"grid=({grid})")
        result = f(grid)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

