#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
import math
from typing import List, Optional

class Solution:
    """We have an m x n grid of positive integers. Starting at any cell in the first column, at each step, we can move: 
        -   right               (row, col+1)
        -   right-and-down      (row+1, col+1)
        -   right-and-up        (row-1, col+1)
    if that square is larger than the current. Determine the maximum number of moves possible"""

    #   runtime: beats 12%
    #    memory: beats 90%
    def maxMoves_DP_BottomUp(self, grid: List[List[int]]) -> int:

        #   table[i][j]: maximum number of moves from (i,j) possible
        table = [ [ 0 for _ in range(len(grid[0])) ] for _ in range(len(grid)) ]

        #   fill table:
        for col in range(len(grid[0])-2, -1, -1):
            for row in range(len(grid)):
                table_current = table[row][col]
                trial_row = row - 1
                if trial_row >= 0 and trial_row < len(grid):
                    if grid[row][col] < grid[trial_row][col+1]:
                        table_current = max(table_current, 1 + table[trial_row][col+1])
                trial_row = row 
                if trial_row >= 0 and trial_row < len(grid):
                    if grid[row][col] < grid[trial_row][col+1]:
                        table_current = max(table_current, 1 + table[trial_row][col+1])
                trial_row = row + 1
                if trial_row >= 0 and trial_row < len(grid):
                    if grid[row][col] < grid[trial_row][col+1]:
                        table_current = max(table_current, 1 + table[trial_row][col+1])
                table[row][col] = table_current

        result = 0
        for row in range(len(grid)):
            result = max(result, table[row][0])
        return result


    #   runtime: beats 55%
    #    memory: beats 5%
    def maxMoves_DP_TopDown(self, grid: List[List[int]]) -> int:

        def solve(row, col):
            if col >= len(grid[0]) - 1:
                return 0
            if (row, col) in memo:
                return memo[(row,col)]
            temp = 0
            trial_row = row - 1
            if trial_row >= 0 and trial_row < len(grid):
                if grid[row][col] < grid[trial_row][col+1]:
                    temp = max(temp, 1 + solve(trial_row, col+1))
            trial_row = row
            if trial_row >= 0 and trial_row < len(grid):
                if grid[row][col] < grid[trial_row][col+1]:
                    temp = max(temp, 1 + solve(trial_row, col+1))
            trial_row = row + 1
            if trial_row >= 0 and trial_row < len(grid):
                if grid[row][col] < grid[trial_row][col+1]:
                    temp = max(temp, 1 + solve(trial_row, col+1))
            memo[(row,col)] = temp
            return temp

        memo = dict()
        result = 0
        for row in range(len(grid)):
            temp = solve(row, 0)
            result = max(result, temp)
        return result


    def maxMoves_ans_BFS(self, grid: List[List[int]]) -> int:
        raise NotImplementedError("Review BFS answer")


s = Solution()
test_functions = [ s.maxMoves_DP_BottomUp, s.maxMoves_DP_TopDown, s.maxMoves_ans_BFS, ]

inputs = [ [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]], [[3,2,4],[2,1,9],[1,1,7]], [[187,167,209,251,152,236,263,128,135],[267,249,251,285,73,204,70,207,74],[189,159,235,66,84,89,153,111,189],[120,81,210,7,2,231,92,128,218],[193,131,244,293,284,175,226,205,245]], ]
checks = [ 3, 0, 3, ]
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

