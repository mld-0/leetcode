import time
from typing import List, Optional

class Solution:
    """Determine the length of the longest continuous subarray that is increasing or decreasing"""

    #   runtime: beats 58%
    #    memory: beats 82%
    def longestMonotonicSubarray_linear(self, nums: List[int]) -> int:
        result = 1
        S = len(nums)
        delta = [ 0 ] * S
        window_length = 1
        for i in range(1, S):
            if nums[i] - nums[i-1] > 0:
                delta[i] = 1
            elif nums[i] - nums[i-1] < 0:
                delta[i] = -1
        for i in range(1, S):
            if (window_length == 1 and delta[i] != 0) or (delta[i] == delta[i-1] and delta[i] != 0):
                window_length += 1
            elif delta[i] != 0:
                window_length = 2
            else:
                window_length = 1
            result = max(result, window_length)
        return result


    #   runtime: beats 42%
    #    memory: beats 83%
    def longestMonotonicSubarray_linear_ii(self, nums: List[int]) -> int:
        result = 1
        S = len(nums)
        delta = [(b > a) - (b < a) for a, b in zip(nums, nums[1:])]
        window_length = 1
        for i in range(S-1):
            if (window_length == 1 and delta[i] != 0) or (delta[i] == delta[i-1] and delta[i] != 0):
                window_length += 1
            elif delta[i] != 0:
                window_length = 2
            else:
                window_length = 1
            result = max(result, window_length)
        return result


    #   runtime: beats 100%
    #    memory: beats 83%
    def longestMonotonicSubarray_ans_claude(self, nums: List[int]) -> int:
        best = inc = dec = 1
        prev = nums[0]
        for x in nums:
            if x > prev:
                inc += 1
                dec = 1
                if inc > best:
                    best = inc
            elif x < prev:
                dec += 1
                inc = 1
                if dec > best:
                    best = dec
            else:
                inc = dec = 1
            prev = x
        return best


s = Solution()
test_functions = [ s.longestMonotonicSubarray_linear, s.longestMonotonicSubarray_linear_ii, s.longestMonotonicSubarray_ans_claude, ]

inputs = [ [1,4,3,3,2], [3,3,3,3], [3,2,1], [1,9,7,1], [1], [5,8,10,9,8], [24,47,24,23,14,6,9,2,3,19], [21,32,1,39,40,24,6,21,24,33,25,33,6,50,34,14,24,12,2,1], [50,32,13,18,32,16,12,4,18,36,5,6,12,14,37,45,36,13,14,48,8,45,33,39,40,8,45,4,36,13,44,32,15,35,1,50,14,41,43,17,13,11,44,3,25,14,10,7,2,44], [50,22,16,14,47,36,36,33,23,5,50,19,17,15,19,27,33,6,12,32,25,42,44,30,30,42,35,19,28,2,36,33,15,5,24,19,17,42,33,46,40,39,5,2,37,36,41,7,27,28], [49,50,50,49,48,47,50,46,45,44,43,42,41,40,39,38,37,36,35,34,33,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5], [50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50], ]
checks = [ 2, 1, 3, 3, 1, 3, 5, 4, 6, 5, 43, 1, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for s, check in zip(inputs, checks):
        print(f"s=({s})")
        result = f(s)
        print(f"result=({result})")
        assert result == check, "Wrong Result"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

