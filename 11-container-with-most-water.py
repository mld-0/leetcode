#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
#   {{{2
from typing import List

class Solution:

    def maxArea(self, height: List[int]) -> int:
        return self.maxArea_TwoPointers(height)

    
    #   runtime: beats 99%
    def maxArea_TwoPointers(self, height: List[int]) -> int:
        V = 0
        endpoints = [None, None]

        l = 0
        r = len(height) - 1

        while l < r:
            #   evaluate trial height/volume 
            trial_H = min(height[l], height[r])
            trial_V = trial_H * (r - l)
            if trial_V > V:
                V = trial_V
                endpoints = [l, r]

            #   Increment 'l' until height[l] > trial_H (or out of bounds)
            while (trial_H >= height[l] and l < r):
                l += 1

            #   Decrement 'r' until height[r] > trial_H (or out of bounds)
            while (trial_H >= height[r] and l < r):
                r -= 1

        return V
        

    #   runtime: TLE
    def maxArea_BruteForce(self, height: List[int]) -> int:
        V = 0
        endpoints = [0, len(height)-1]

        for i in range(0, len(height)-1):
            for j in range(1, len(height)):
                h = min(height[i], height[j])
                trial_V = h * (j - i)
                if trial_V > V:
                    V = trial_V
                    endpoints = [i, j]

        return V


s = Solution()

input_items = [ [1,8,6,2,5,4,8,3,7], [1,1], [4,3,2,1,4], [1,2,1], [1,2,4,3] ]
check_items = [ 49, 1, 16, 2, 4 ]

for heights, check in zip(input_items, check_items):
    print("heights=(%s)" % str(heights))
    result = s.maxArea(heights)
    print("result=(%s)" % result)
    assert result == check, "Check failed"
    print()

