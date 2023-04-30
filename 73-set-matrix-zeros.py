import copy
import math
import time
import pprint
from typing import List

class Solution:

    #   runtime: beats 90%
    def setZeros_set(self, matrix: List[List[int]]) -> None:
        mark_rows = set()
        mark_cols = set()
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    mark_rows.add(row)
                    mark_cols.add(col)
        for row in mark_rows:
            for col in range(len(matrix[0])):
                matrix[row][col] = 0
        for col in mark_cols:
            for row in range(len(matrix)):
                matrix[row][col] = 0


    #   runtime: beats 90%
    def setZeros_markedNone(self, matrix: List[List[int]]) -> None:
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[row][col] = None
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] is None:
                    for i in range(len(matrix)):
                        if not matrix[i][col] is None:
                            matrix[i][col] = 0
                    for j in range(len(matrix[0])):
                        if not matrix[row][j] is None:
                            matrix[row][j] = 0
                    matrix[row][col] = 0


    #   runtime: beats 67%
    def setZeros_findPlaceholder(self, matrix: List[List[int]]) -> None:

        def find_placeholder(matrix: List[List[int]]) -> int:
            min_unused = -math.inf
            for row in range(len(matrix)):
                for col in range(len(matrix[0])):
                    min_unused = max(min_unused, matrix[row][col])
            return min_unused + 1

        placeholder = find_placeholder(matrix)
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[row][col] = placeholder
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == placeholder:
                    for i in range(len(matrix)):
                        if not matrix[i][col] == placeholder:
                            matrix[i][col] = 0
                    for j in range(len(matrix[0])):
                        if not matrix[row][j] == placeholder:
                            matrix[row][j] = 0
                    matrix[row][col] = 0


    #   runtime: beats 87%
    def setZeros_ans(self, matrix: List[List[int]]) -> None:
        #   Need to use flags for first row/col since it is a single cell which cannot be used for both
        zero_first_row = False
        for col in range(len(matrix[0])):
            if matrix[0][col] == 0:
                zero_first_row = True
                break
        zero_first_col = False
        for row in range(len(matrix)):
            if matrix[row][0] == 0:
                zero_first_col = True
                break

        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0
        for row in range(1, len(matrix)):
            if matrix[row][0] == 0:
                for col in range(1, len(matrix[0])):
                    matrix[row][col] = 0
        for col in range(1, len(matrix[0])):
            if matrix[0][col] == 0:
                for row in range(1, len(matrix)):
                    matrix[row][col] = 0

        if zero_first_row:
            for col in range(len(matrix[0])):
                matrix[0][col] = 0
        if zero_first_col:
            for row in range(len(matrix)):
                matrix[row][0] = 0


s = Solution()
test_functions = [ s.setZeros_markedNone, s.setZeros_set, s.setZeros_findPlaceholder, s.setZeros_ans, ]

inputs = [ [[1,1,1],[1,0,1],[1,1,1]], [[0,1,2,0],[3,4,5,2],[1,3,1,5]], ]
checks = [ [[1,0,1],[0,0,0],[1,0,1]], [[0,0,0,0],[0,4,5,0],[0,3,1,0]], ]
assert len(inputs) == len(checks)

for f in test_functions:
    inputs_copy = copy.deepcopy(inputs)
    print(f.__name__)
    startTime = time.time()
    for matrix, check in zip(inputs_copy, checks):
        print(f"matrix=({matrix})")
        f(matrix)
        print(f"result=({matrix})")
        assert matrix == check, "Comparison failed, check=({check})"
    print("elapsed_ms=(%0.2f)" % ((time.time() - startTime) * 1000000))
    print()

