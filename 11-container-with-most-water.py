#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   {{{2
import math
import time
from typing import List

class Solution:
    """Determine the maximum area that can be found between two heights in array `height`, where area is given by the distance between the elements * the min height of the two elements"""
 
    def maxArea_TwoPointers_i(self, height: List[int]) -> int:

        def get_area(l, r):
            return (r-l) * min(height[l], height[r])

        V = -math.inf
        l = 0
        r = len(height) - 1
        while l < r:
            V = max(V, get_area(l, r))
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1

        return V


    #   runtime: beats 99%
    def maxArea_TwoPointers_ii(self, height: List[int]) -> int:

        def get_area(l, r):
            return (r-l) * get_height(l, r)
        def get_height(l, r):
            return min(height[l], height[r])

        V = -math.inf
        l = 0
        r = len(height) - 1
        while l < r:
            V = max(V, get_area(l, r))
            h = get_height(l, r)
            while height[l] <= h and l < r:
                l += 1
            while height[r] <= h and l < r:
                r -= 1

        return V


    #   runtime: TLE
    def maxArea_BruteForce(self, height: List[int]) -> int:
        V = 0
        endpoints = [None, None]

        for i in range(0, len(height)-1):
            for j in range(1, len(height)):
                trial_H = min(height[i], height[j])
                trial_V = trial_H * (j - i)
                if trial_V > V:
                    V = trial_V
                    endpoints = [i, j]

        return V


s = Solution()
test_functions = [ s.maxArea_TwoPointers_i, s.maxArea_TwoPointers_ii, s.maxArea_BruteForce, ]

inputs = [ [1,8,6,2,5,4,8,3,7], [1,1], [4,3,2,1,4], [1,2,1], [1,2,4,3] ]
checks = [ 49, 1, 16, 2, 4 ]

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for heights, check in zip(inputs, checks):
        print("heights=(%s)" % str(heights))
        result = f(heights)
        print("result=(%s)" % result)
        assert result == check, "Check failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

