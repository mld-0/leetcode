#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
import bisect
import functools
import math
from typing import List
#   {{{2

class Solution:

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        #return self.numSubarrayProductLessThanK_SlidingWindow(nums, k)
        return self.numSubarrayProductLessThanK_LogBinarySearch(nums, k)

    
    #   runtime: beats 87%
    def numSubarrayProductLessThanK_SlidingWindow(self, nums: List[int], k: int) -> int:
        """Number of contiguous subarrays in 'nums' with product less than 'k'"""
        if k <= 1: 
            return 0
        result = 0
        trial = 1
        l = 0
        for r, val in enumerate(nums):
            trial *= val
            while trial >= k:
                trial //= nums[l]
                l += 1
            result += r - l + 1
        return result


    #   runtime: beats 33%
    def numSubarrayProductLessThanK_LogBinarySearch(self, nums: List[int], k: int) -> int:
        """Number of contiguous subarrays in 'nums' with product less than 'k', using property that log-of-product == sum-of-logs"""
        if k <= 1:
            return 0
        k = math.log(k)

        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + math.log(x))

        result = 0
        for l, x in enumerate(prefix):
            r = bisect.bisect_left(prefix, x+k, l+1)
            result += r - l - 1

        return result



    #   runtime: TLE
    def numSubarrayProductLessThanK_i(self, nums: List[int], k: int) -> int:
        result = 0
        for window_size in range(1, len(nums)+1):
            for window_start in range(len(nums)-window_size+1):
                trial_product = math.prod(nums[window_start:window_start+window_size])
                if trial_product < k:
                    result += 1
        return result


    #   runtime: TLE
    def numSubarrayProductLessThanK_ii(self, nums: List[int], k: int) -> int:
        result = 0
        for window_size in range(1, len(nums)+1):
            trial_product = math.prod(nums[:window_size])
            if trial_product < k:
                result += 1
            for window_start in range(1, len(nums)-window_size+1):
                trial_product = trial_product // nums[window_start-1]
                trial_product = trial_product * nums[window_start+window_size-1]
                if trial_product < k:
                    result += 1
        return result


    #   runtime: TLE
    def numSubarrayProductLessThanK_iii(self, nums: List[int], k: int) -> int:
        result = 0
        for window_start in range(0, len(nums)):
            trial_product = nums[window_start]
            if trial_product < k:
                result += 1
            else:
                break
            for window_size in range(2, len(nums)+1-window_start):
                trial_product *= nums[window_start+window_size-1]
                if trial_product < k:
                    result += 1
                else:
                    break
        return result




s = Solution()

input_values = [ ([10,5,2,6], 100), ([1,2,3], 0), ]
input_checks = [ 8, 0, ]

for (nums, k), check in zip(input_values, input_checks):
    print("nums=(%s), k=(%s)" % (nums, k))
    result = s.numSubarrayProductLessThanK(nums, k)
    print("result=(%s)" % result)
    assert result == check, "Check failed"
    print()

