#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
from typing import List
import math
#   Problem: Given an array of non-negative integers nums, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Your goal is to reach the last index in the minimum number of jumps. You can assume that you can always reach the last index.
#   {{{2
class Solution:

    #   runtime: TLE
    def jump_DP_TopDown(self, nums: List[int]) -> bool:
        """Adapted from 55-jump-game, track number of jumps required to reach end for each square"""
        canReachEnd = [ math.inf for x in nums ]
        canReachEnd[len(nums)-1] = 0

        def jump_solve(index: int, previous_index: int) -> int:
            if canReachEnd[index] != math.inf:
                return canReachEnd[index]

            for next_index in range(index+1, min(index+nums[index], len(nums)-1)+1):
                trial = jump_solve(next_index, index) 
                if trial != math.inf:
                    canReachEnd[index] = min(canReachEnd[index], trial+1)

            return canReachEnd[index]

        jump_solve(0, None)
        print(canReachEnd)
        return canReachEnd[0]

    
    #   runtime: beats 15%
    def jump_DP_BottomUp_Iterative(self, nums: List[int]) -> int:
        """Adapted from 55-jump-game, track number of jumps required to reach end for each square"""
        canReachEnd = [ math.inf for x in nums ]
        canReachEnd[len(nums)-1] = 0

        for i in range(len(nums)-2, -1, -1):
            #   can we reach a square that can reach end of list
            for j in range(i+1, min(i+nums[i], len(nums)-1)+1):
                if canReachEnd[j] >= 0:
                    canReachEnd[i] = min(canReachEnd[i], canReachEnd[j]+1)

        return canReachEnd[0]


    #   runtime: beats 97%
    def jump_Greedy(self, nums: List[int]) -> int:
        jumps = 0
        currentJumpEnd = 0
        farthest = 0

        for i in range(len(nums)-1):
            farthest = max(farthest, i+nums[i])
            if i == currentJumpEnd:
                jumps += 1
                currentJumpEnd = farthest

        return jumps


s = Solution()

input_values = [ [2,3,1,1,4], [2,3,0,1,4], ]
input_checks = [ 2, 2, ]

test_functions = [ s.jump_DP_BottomUp_Iterative, s.jump_DP_TopDown, s.jump_Greedy, ]

for test_func in test_functions:
    print(test_func.__name__)
    for nums, check in zip(input_values, input_checks):
        print("nums=(%s)" % nums)
        result = test_func(nums)
        print("result=(%s)" % result)
        assert result == check, "Check failed"
    print()

