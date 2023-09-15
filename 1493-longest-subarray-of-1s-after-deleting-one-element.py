import time
import math
from typing import List, Optional

class Solution:
    """Given array `nums`, determine the longest possible contiguous series of '1's after we delete exactly 1 element from the array"""

    #   runtime: beats 32%
    def longestSubarray_twoPointers(self, nums: List[int]) -> int:
        l = 0
        r = 0
        zeros_in_window = 0
        result = 0
        if nums[0] == 0:
            zeros_in_window += 1
        while r+1 < len(nums) and (zeros_in_window < 1 or nums[r+1] == 1):
            if nums[r+1] == 0:
                zeros_in_window += 1
            r += 1
        trial = r - l 
        result = max(result, trial)
        while r+1 < len(nums):
            while zeros_in_window >= 1 and l < len(nums):
                if nums[l] == 0:
                    zeros_in_window -= 1
                l += 1
            while r+1 < len(nums) and (zeros_in_window < 1 or nums[r+1] == 1):
                if nums[r+1] == 0:
                    zeros_in_window += 1
                r += 1
            trial = r - l 
            result = max(result, trial)
        return result


    #   runtime: beats 63%
    def longestSubarray_ans_SlidingWindow(self, nums: List[int]) -> int:
        zeros_in_window = 0
        l = 0
        result = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zeros_in_window += 1
            while zeros_in_window > 1:
                if nums[l] == 0:
                    zeros_in_window -= 1
                l += 1
            result = max(result, r - l)
        return result


    #   runtime: beats 91%
    def longestSubarray_ans_longestOnes(self, nums: List[int]) -> int:
        k = 1
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                k -= 1
            if k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
        return r - l


s = Solution()
test_functions = [ s.longestSubarray_twoPointers, s.longestSubarray_ans_SlidingWindow, s.longestSubarray_ans_longestOnes, ]

inputs = [ [1,1,0,1], [0,1,1,1,0,1,1,0,1], [1,1,1], [1,1,0,0,1,1,1,0,1], [1,0,0,0,0], [1,0,1,1,1,1,1,1,0,1,1,1,1,1], [1], [0,1,1,1,1,1], ]
checks = [ 3, 5, 2, 4, 1, 11, 0, 5, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for nums, check in zip(inputs, checks):
        print(f"nums=({nums})")
        result = f(nums)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

