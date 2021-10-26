#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
from typing import List
import itertools
#   {{{2
#   Problem: Determine number of 'arithmetic-slices' in a given list, that is, number of sublists where the difference between each subsiquent element is constant
class Solution:

    #   runtime: beats 95%
    def numberOfArithmeticSlices_BruteForce(self, nums: List[int]) -> int:
        """Determine slices count by checking every sublist length 3 or more in 'nums'"""

        def is_arthmetic_slice(l, r):
            """Returns whether the difference between each element in nums[l:r+1] constant"""
            deltas = [ nums[i] - nums[i-1] for i in range(l+1, r+1) ]
            return deltas[:-1] == deltas[1:]

        result_count = 0
        for l in range(len(nums)-2):
            for r in range(l+2, len(nums)):
                if is_arthmetic_slice(l, r):
                    result_count += 1
                else:
                    break

        return result_count

   
    #   runtime: beats 95%
    def numberOfArithmeticSlices_BruteForceStoreDeltas(self, nums: List[int]) -> int:
        """Calculate deltas list, and checking each sublist length 2 or more"""
        deltas = [ nums[i] - nums[i-1] for i in range(1, len(nums)) ]

        def deltas_interval_is_const(l, r):
            """Return whether deltas[l:r+1] is constant"""
            temp = deltas[l:r+1]
            return temp[:-1] == temp[1:]

        result_count = 0

        for l in range(len(deltas)-1):
            for r in range(l+1, len(deltas)):
                if deltas_interval_is_const(l, r):
                    result_count += 1
                else:
                    break

        return result_count


    #   runtime: beats 95%
    def numberOfArithmeticSlices_Recursive(self, nums: List[int]) -> int:
        result = { 'value': 0 }

        def slices_solve(i: int):
            if i < 2:
                return 0
            count = 0
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                count = 1 + slices_solve(i-1)
                result['value'] += count
            else:
                slices_solve(i-1)
            return count

        slices_solve(len(nums)-1)
        return result['value']


    #   runtime: beats 95%
    def numberOfArithmeticSlices_DP_BottomUp(self, nums: List[int]) -> int:
        table = [ 0 for x in range(len(nums)) ]
        result = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                table[i] = 1 + table[i-1]
                result += table[i]
        return result


s = Solution()
test_functions = [ s.numberOfArithmeticSlices_BruteForce, s.numberOfArithmeticSlices_BruteForceStoreDeltas, s.numberOfArithmeticSlices_Recursive, s.numberOfArithmeticSlices_DP_BottomUp, ]

input_values = [ [1,2,3,4], [1], ]
input_checks = [ 3, 0, ]

for test_func in test_functions:
    print(test_func.__name__)
    for nums, check in zip(input_values, input_checks):
        print("nums=(%s)" % nums)
        result = test_func(nums)
        print("result=(%s)" % result)
        assert result == check, "Check failed"
    print()

