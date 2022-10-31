from typing import List
from collections import defaultdict

#   A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements

class Solution:

    #   runtime: beats 96%
    def isToeplitzMatrix_i(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        assert all( [ cols == len(row) for row in matrix ] )

        for row in range(rows-1, -1, -1):
            col = 0
            values = set()
            for delta in range(0, cols):
                if row < 0 or row >= rows or col >= cols or col < 0:
                    break
                values.add(matrix[row][col])
                row += 1
                col += 1
            if len(values) > 1:
                return False

        for col in range(0, cols):
            row = 0
            values = set()
            for delta in range(0, cols):
                if row < 0 or row >= rows or col >= cols or col < 0:
                    break
                values.add(matrix[row][col])
                row += 1
                col += 1
            if len(values) > 1:
                return False

        return True

        
    #   runtime: beats 70%
    def isToeplitzMatrix_Ans_Coordinates(self, matrix: List[List[int]]) -> bool:
        #   Recognise that (r1,c1) is on diagonal number 'r1 - c1'
        #   or, (r1,c1)/(r2,c2) are on the same diagonal if 'r1 - c1' == 'r2 - c2'
        rows = len(matrix)
        cols = len(matrix[0])
        assert all( [ cols == len(row) for row in matrix ] )
        diagonals = defaultdict(set)
        for row in range(0, rows):
            for col in range(0, cols):
                diagonals[row-col].add(matrix[row][col])
        for k,v in diagonals.items():
            if len(v) > 1:
                return False
        return True


    #   runtime: beats 87%
    def isToeplitzMatrix_Ans_TopLeftNeighbour(self, matrix: List[List[int]]) -> bool:
        #   Compare each element with it's immediate top-left neighbour
        rows = len(matrix)
        cols = len(matrix[0])
        assert all( [ cols == len(row) for row in matrix ] )
        for row in range(0, rows):
            for col in range(0, cols):
                if row > 0 and col > 0 and matrix[row-1][col-1] != matrix[row][col]:
                    return False
        return True


s = Solution()
test_functions = [ s.isToeplitzMatrix_i, s.isToeplitzMatrix_Ans_Coordinates, s.isToeplitzMatrix_Ans_TopLeftNeighbour, ]

inputs = [ [[1,2,3,4],[5,1,2,3],[9,5,1,2]], [[1,2],[2,2]], ]
checks = [ True, False, ]
assert len(inputs) == len(checks)

for f in test_functions:
    print(f.__name__)
    for matrix, check in zip(inputs,checks):
        print(f"matrix=({matrix})")
        result = f(matrix)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print()

