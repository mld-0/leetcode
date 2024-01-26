import time
import functools
from typing import List, Optional

class Solution:
    """Given an (m x n) grid, determine how many paths of length <= `maxMove` lead out of the grid, starting at (startRow,startColumn)"""

    #   runtime: beats 100%
    def findPaths_DP_TopDown(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        @functools.cache
        def solve(remainingMoves, row, col):
            if (row < 0 or row >= m) or (col < 0 or col >= n):
                return 1
            if remainingMoves == 0:
                return 0
            result = 0
            for delta in (-1,1):
                result += solve(remainingMoves-1, row+delta, col)
                result += solve(remainingMoves-1, row, col+delta)
            return result

        result = solve(maxMove, startRow, startColumn)
        return result % (10**9 + 7)


    #   runtime: beats 31%
    def findPaths_DP_BottomUp(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        #   table[row][col][remainingMoves]
        table = [ [ [ 0 for _ in range(n) ] for _ in range(m) ] for _ in range(maxMove+1) ]

        for remainingMoves in range(1, maxMove+1):
            for row in range(m):
                for col in range(n):
                    current = 0
                    for delta in (-1,1):
                        if row+delta < 0 or row+delta >= m:
                            current += 1
                        else:
                            current += table[remainingMoves-1][row+delta][col]
                        if col+delta < 0 or col+delta >= n:
                            current += 1
                        else:
                            current += table[remainingMoves-1][row][col+delta]

                    table[remainingMoves][row][col] = current

        return table[maxMove][startRow][startColumn] % (10**9 + 7)


    #   runtime: beats 60%
    def findPaths_ans_DP_BottomUp_SpaceOptimised(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        table = [ [ 0 for _ in range(n) ] for _ in range(m) ]

        table[startRow][startColumn] = 1
        result = 0

        for move in range(1, maxMove+1):
            next_table = [ [ 0 for _ in range(n) ] for _ in range(m) ]
            for i in range(m):
                for j in range(n):
                    if i == m-1:
                        result = result + table[i][j]
                    if j == n-1:
                        result = result + table[i][j]
                    if i == 0:
                        result = result + table[i][j]
                    if j == 0:
                        result = result + table[i][j]
                    next_table[i][j] = \
                        (table[i-1][j] if i > 0 else 0) + (table[i+1][j] if i < m - 1 else 0) + \
                        (table[i][j-1] if j > 0 else 0) + (table[i][j+1] if j < n - 1 else 0)
            table = next_table

        return result % (10**9 + 7)


s = Solution()
test_functions = [ s.findPaths_DP_TopDown, s.findPaths_DP_BottomUp, s.findPaths_ans_DP_BottomUp_SpaceOptimised, ]

inputs = [ (2,2,2,0,0), (1,3,3,0,1), (2,2,1,0,0), (8,50,23,5,26), ]
checks = [ 6, 12, 2, 914783380, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for (m, n, maxMove, startRow, startColumn), check in zip(inputs, checks):
        print(f"m=({m}), n=({n}), maxMove=({maxMove}), startRow=({startRow}), startColumn=({startColumn})")
        result = f(m, n, maxMove, startRow, startColumn)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

