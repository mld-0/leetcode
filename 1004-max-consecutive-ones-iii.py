import time
import math
from typing import List, Optional

class Solution:
    """Return the length of the longest consecutive subsequence of '1's, if we can flip up to `k` '0's to '1'"""

    #   runtime: beats 53%
    def longestOnes(self, nums: List[int], k: int) -> int:
        result = -math.inf
        l = 0
        r = 0
        current_window_zeros = 0
        if nums[l] == 0:
            current_window_zeros += 1
        while r < len(nums):
            while l < len(nums) and current_window_zeros > k:
                if nums[l] == 0:
                    current_window_zeros -= 1
                l += 1
            while r+1 < len(nums) and (nums[r+1] == 1 or current_window_zeros < k):
                if nums[r+1] == 0:
                    current_window_zeros += 1
                r += 1
            result = max(result, r-l+1)
            if r+1 < len(nums) and nums[r+1] == 0:
                current_window_zeros += 1
            r += 1
        return result


    #   runtime: beats 67%
    def longestOnes_ans_i(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        result = 0
        while r < len(nums):
            if nums[r] == 1 or (nums[r] == 0 and k > 0):
                if nums[r] == 0:
                    k -= 1
                r += 1
            else:
                result = max(result, r-l)
                while k == 0:
                    if nums[l] == 0:
                        k += 1
                    l += 1
        result = max(result, r-l)
        return result


    #   runtime: beats 96%
    def longestOnes_ans_ii(self, nums: List[int], k: int) -> int:
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                k -= 1
            if k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
        return r - l + 1


s = Solution()
test_functions = [ s.longestOnes, s.longestOnes_ans_i, s.longestOnes_ans_ii, ]

inputs = [ ([1,1,1,0,0,0,1,1,1,1,0],2), ([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3), ([1,1,1,0,0,0,1,0,1,0,0,1,1,1,1,0,1,0,1,1,1,0,1,1,0,1,0,1,1,0,1,1,0,1,1,1,0,0,0,1,0,0,0,1,1,1,1,0,0,1],10), ([0,0,0,1],4), ]
checks = [ 6, 10, 30, 4, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for (nums, k), check in zip(inputs, checks):
        print(f"nums=({nums}), k=({k})")
        result = f(nums, k)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

