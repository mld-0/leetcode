import functools
from typing import List

class Solution:

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """Find minimum path sum from top-to-bottom, traveling from i on a given row to either i or i+1 on the next row"""
        return self.minimumTotal_Recursive(triangle)

    #   runtime: beats 15%
    def minimumTotal_Recursive(self, triangle: List[List[int]]) -> int:
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

    #   runtime: beats 5%
    def minimumTotal_WithPath_Recursive(self, triangle: List[List[int]]) -> int:
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


    #   TODO: 2021-09-30T20:17:16AEST _leetcode, 120-triangle, Dynamic Programming, BottomUp and TopDown
    def minimumTotal_DP_BottomUp(self, triangle: List[List[int]]) -> int:
        raise NotImplementedError()


    def minimumTotal_DP_TopDown(self, triangle: List[List[int]]) -> int:
        raise NotImplementedError()


s = Solution()

input_values = [ [[2],[3,4],[6,5,7],[4,1,8,3]], [[-10]], ]
input_checks = [ 11, -10, ]

for triangle, check in zip(input_values, input_checks):
    result = s.minimumTotal(triangle)
    print("result=(%s)" % str(result))
    assert check == result, "Check failed"
    print()

