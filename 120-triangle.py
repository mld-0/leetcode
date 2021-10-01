#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
import functools
import math
from typing import List
#   {{{2

class Solution:

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """Find minimum path sum from top-to-bottom, traveling from i on a given row to either i or i+1 on the next row"""
        return self.minimumTotal_TopDown(triangle)
        #return self.minimumTotal_BottomUp(triangle)

    #   runtime: beats 5%
    def minimumTotal_TopDown(self, triangle: List[List[int]]) -> int:
        self.memo = {}

        def min_path(row, col):
            if (row,col) in self.memo:
                return self.memo[(row,col)]

            #   last row, no recursive calls to make
            if row == len(triangle) - 1:
                self.memo[(row,col)] = triangle[row][col]
                return triangle[row][col]

            #   cost for (row, col) is given by min of two cells below it
            trials = [ min_path(row+1, col), min_path(row+1, col+1) ]
            path = triangle[row][col] + min(trials)

            self.memo[(row,col)] = path
            return path

        result = min_path(0,0)
        return result


    #   runtime: beats 33%
    def minimumTotal_BottomUp(self, triangle: List[List[int]]) -> int:
        grid = triangle[:]

        for row in range(1, len(grid)):
            for col in range(len(grid[row])):

                trials = [ math.inf ] * 2
                if col-1 >= 0:
                    trials[0] = grid[row-1][col-1]
                if col < len(grid[row-1]):
                    trials[1] = grid[row-1][col]

                grid[row][col] += min(trials)

        print(grid)
        return min(grid[-1])


    #   runtime: beats 15%
    def minimumTotal_Recursive(self, triangle: List[List[int]]) -> int:
        #   {{{
        @functools.lru_cache()
        def min_path(row, col):
            path = triangle[row][col]
            if row < len(triangle) - 1:
                trial_A = min_path(row+1, col)
                trial_B = min_path(row+1, col+1)
                
                if trial_A < trial_B:
                    path += trial_A
                else:
                    path += trial_B
            return path
        result = min_path(0,0)
        return result
        #   }}}

    #   runtime: beats 5%
    def minimumTotal_WithPath_Recursive(self, triangle: List[List[int]]) -> int:
        #   {{{
        @functools.lru_cache()
        def min_path(row, col):
            steps = []
            path = triangle[row][col]
            if row < len(triangle) - 1:
                trial_A, steps_A = min_path(row+1, col)
                trial_B, steps_B = min_path(row+1, col+1)
                if trial_A < trial_B:
                    path += trial_A
                    steps = steps + steps_A + [(row+1, col)]
                else:
                    path += trial_B
                    steps = steps + steps_B + [(row+1, col+1)]
            return path, steps
        result, steps = min_path(0,0)
        steps = steps + [(0,0)] 
        print(steps)
        return result
        #   }}}



s = Solution()

input_values = [ [[2],[3,4],[6,5,7],[4,1,8,3]], [[-10]], [[-1],[3,2],[-3,1,-1]], ]
input_checks = [ 11, -10, -1, ]

for triangle, check in zip(input_values, input_checks):
    result = s.minimumTotal(triangle)
    print("result=(%s)" % str(result))
    assert check == result, "Check failed"
    print()

