#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
from typing import List
#   {{{2
class Solution:

    #   Ongoing: 2021-10-24T21:39:11AEDT _leetcode, 55-jump-game, ans DP_BottomUp is slow, ans DP_TopDown is TLE, both look to be optimal-ish, backtracking (is worse?), greedy (is better?)
    #   TODO: 2021-10-24T21:41:23AEDT _leetcode, 55-jump-game, (continuing), backtracking, greedy solutions, evaluation of solution

    #   runtime: TLE
    def canJump_DP_TopDown(self, nums: List[int]) -> bool:
        canReachEnd = [ 'Unknown' for x in nums ]
        canReachEnd[len(nums)-1] = 'True'

        def canjump_solve(index: int) -> bool:
            if canReachEnd[index] != 'Unknown':
                return canReachEnd[index] == 'True'

            for next_index in range(index+1, min(index+nums[index], len(nums)-1)+1):
                if canjump_solve(next_index):
                    canReachEnd[index] = 'True'
                    return True

            canReachEnd[index] = 'False'
            return False

        canjump_solve(0)
        return canReachEnd[0] == 'True'


    #   runtime: beats 8%
    def canJump_DP_BottomUp_Iterative(self, nums: List[int]) -> bool:
        canReachEnd = [ False for x in nums ]
        canReachEnd[len(nums)-1] = True

        for i in range(len(nums)-2, -1, -1):
            #   can we reach a square that can reach end of list
            for j in range(i+1, min(i+nums[i], len(nums)-1)+1):
                if canReachEnd[j] == True:
                    canReachEnd[i] = True
                    break

        return canReachEnd[0]


s = Solution()
test_functions = [ s.canJump_DP_TopDown, s.canJump_DP_BottomUp_Iterative, ]

input_values = [ [2,3,1,1,4], [3,2,1,0,4], [1,3,2], ]
input_checks = [ True, False, True, ]

for test_func in test_functions:
    print(test_func.__name__)
    for nums, check in zip(input_values, input_checks):
        print("nums=(%s)" % nums)
        result = test_func(nums)
        print("result=(%s)" % result)
        assert result == check, "Check failed"
    print()


