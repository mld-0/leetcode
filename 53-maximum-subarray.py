#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import math
import time
from typing import List

#   Find the contiguious subarray with the largest sum

class Solution:

    #   runtime: TLE
    def maxSubArray_bruteForce(self, nums: List[int]) -> int:
        max_sum = -math.inf
        l = 0
        while l < len(nums):
            r = l
            current = 0
            while r < len(nums):
                current += nums[r]
                max_sum = max(current, max_sum)
                r += 1
            l += 1
        return max_sum


    #   runtime: beats 87%
    def maxSubArray_ii(self, nums: List[int]) -> int:
        current_l = 0
        current_sum = nums[0]
        max_l = 0
        max_r = 0
        max_sum = current_sum
        i = 1
        while i < len(nums):
            n = nums[i]
            if current_sum + n > n:
                current_sum = current_sum + n
            else:
                current_sum = n
                current_l = i
            if current_sum > max_sum:
                max_sum = current_sum
                max_l = current_l
                max_r = i
            i += 1
        return max_sum
        

    #   runtime: beats 65%
    def maxSubArray_ans_DP(self, nums: List[int]) -> int:
        current_sum = nums[0]
        max_sum = current_sum
        for n in nums[1:]:
            current_sum = max(n, current_sum + n)
            max_sum = max(max_sum, current_sum)
        return max_sum


    #   runtime: beats 5%
    def maxSubArray_ans_DivideAndConquer(self, nums: List[int]) -> int:
        def findBestSubarray(nums, left, right):
            if left > right:
                return -math.inf

            mid = (left + right) // 2
            curr = best_left_sum = best_right_sum = 0

            for i in range(mid - 1, left - 1, -1):
                curr += nums[i]
                best_left_sum = max(best_left_sum, curr)

            curr = 0
            for i in range(mid + 1, right + 1):
                curr += nums[i]
                best_right_sum = max(best_right_sum, curr)

            best_combined_sum = nums[mid] + best_left_sum + best_right_sum

            left_half = findBestSubarray(nums, left, mid - 1)
            right_half = findBestSubarray(nums, mid + 1, right)

            return max(best_combined_sum, left_half, right_half)
        
        return findBestSubarray(nums, 0, len(nums) - 1)


s = Solution()
test_functions = [ s.maxSubArray_bruteForce, s.maxSubArray_ii, s.maxSubArray_ans_DP, s.maxSubArray_ans_DivideAndConquer, ]

inputs = [ [-2,1,-3,4,-1,2,1,-5,4], [1], [5,4,-1,7,8], [-2,-1], [-1,-2], [-2,-1,-2], [0,-3,1,1], [0,-2,-3], [1,-2,0], [3,2,-3,-1,1,-3,1,-1], ]
checks = [ 6, 1, 23, -1, -1, -1, 2, 0, 1, 5, ]
assert len(inputs) == len(checks)

for f in test_functions:
    print(f.__name__)
    for nums, check in zip(inputs, checks):
        print(f"nums=({nums})")
        result = f(nums)
        print(f"result=({result})")
        assert result == check, f"Comparison failed, check=({check})"
    print()

