import time
import copy
from typing import List, Optional

class Solution:
    """The frequency of an element is the number of times it occurs in an array.
    You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.
    Return the maximum possible frequency of an element after performing at most k operations."""

    #   runtime: TLE
    def maxFrequency_i(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = 0
        for r in range(len(nums)):
            temp = 1
            remaining = k
            for l in range(r-1, -1, -1):
                remaining -= (nums[r] - nums[l])
                if remaining >= 0:
                    temp += 1
                if remaining <= 0:
                    break
            result = max(result, temp)
        return result


    #   runtime: beats 92%
    def maxFrequency_ii(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = 1
        window_len = 1
        window_sum = nums[0]
        for r in range(1, len(nums)):
            delta = (window_len * nums[r]) - window_sum
            if delta <= k:
                window_len += 1
            elif r - window_len >= 0:
                window_sum -= nums[r-window_len]
            window_sum += nums[r]
            result = max(result, window_len)
        return result


    #   runtime: beats 94%
    def maxFrequency_ans_SlidingWindow(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        curr = 0
        for right in range(len(nums)):
            target = nums[right]
            curr += target
            if (right - left + 1) * target - curr > k:
                curr -= nums[left]
                left += 1
        return len(nums) - left


s = Solution()
test_functions = [ s.maxFrequency_i, s.maxFrequency_ii, s.maxFrequency_ans_SlidingWindow, ]

inputs = [ ([1,2,4],5), ([1,4,8,13],5), ([3,9,6],2), ([9926,9960,10000,9992,9917,9986,9934,9985,9977,9950,9922,9913,9971,9978,9984,9959,9934,9948,9918,9916,9967,9965,9985,9977,9988,9983,9900,9945,9913,9966,9968,9986,9939,9914,9980,9957,9921,9927,9917,9972,9974,9953,9984,9912,9975,9920,9966,9932,9921,9904,9928,9959,9993,9937,9934,9974,9937,9964,9922,9963,9991,9930,9944,9930,9982,9980,9967,9904,9955,9947,9924,9973,9997,9950,9905,9924,9990,9947,9953,9924,9977,9938,9951,9982,9932,9926,9928,9912,9917,9929,9924,9921,9987,9910,9927,9921,9929,9937,9919,9995,9949,9953],3044), ]
checks = [ 3, 2, 1, 82, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for (nums, k), check in zip(inputs, checks):
        nums = copy.deepcopy(nums)
        print(f"nums=({nums}), k=({k})")
        result = f(nums, k)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

