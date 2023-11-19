import time
import copy
import math
from collections import Counter
from typing import List, Optional

class Solution:
    """Given an integer array nums, your goal is to make all elements in nums equal. To complete one operation, follow these steps:
            - Find the largest value in nums. Let its index be i (0-indexed) and its value be largest. If there are multiple elements with the largest value, pick the smallest i.
            - Find the next largest value in nums strictly smaller than largest. Let its value be nextLargest.
            - Reduce nums[i] to nextLargest.
        Return the number of operations to make all elements in nums equal."""

    #   runtime: beats 85%
    def reductionOperations_i(self, nums: List[int]) -> int:
        counts = Counter(nums)
        result = 0
        seen = 0
        for n in sorted(counts.keys())[1:]:
            seen += 1
            result += counts[n] * seen
        return result


    #   runtime: beats 80%
    def reductionOperations_ii(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        unique_count = 0
        previous = nums[0]
        count = 0
        for i, n in enumerate(nums):
            if n != previous:
                if previous != nums[0]:
                    result += count * unique_count
                unique_count += 1
                count = 1
            else:
                count += 1
            previous = n
        result += count * unique_count
        return result


    #   runtime: beats 80%
    def reductionOperations_ans(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        count = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                count += 1
            result += count
        return result


s = Solution()
test_functions = [ s.reductionOperations_i, s.reductionOperations_ii, s.reductionOperations_ans, ]

inputs = [ [5,1,3], [1,1,1], [1,1,2,2,3], [7,9,10,8,6,4,1,5,2,3], [27664,47570,27664,27664,27664,27664,27664,27664,27664,27664], ]
checks = [ 3, 0, 4, 45, 1, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for vals, check in zip(inputs, checks):
        vals = copy.deepcopy(vals)
        print(f"vals=({vals})")
        result = f(vals)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

