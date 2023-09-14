import time
import itertools
from typing import List, Optional

class Solution:
    """Find the pivot index of `nums`, that is, the index where the sum of all numbers left of the index is equal to the sum of all numbers to the right of the index (or -1 if not such index exists)"""

    #   runtime: beats 64%
    def pivotIndex_i(self, nums: List[int]) -> int:
        left_sum = [ 0 for _ in nums ]
        right_sum = [ 0 for _ in nums ]
        left_sum[0] = nums[0]
        right_sum[-1] = nums[-1]
        for i in range(1, len(nums)):
            left_sum[i] = left_sum[i-1] + nums[i]
        for i in range(len(nums)-2, -1, -1):
            right_sum[i] = right_sum[i+1] + nums[i]
        for i in range(len(nums)):
            if left_sum[i] == right_sum[i]:
                return i
        return -1


    #   runtime: beats 90%
    def pivotIndex_ii(self, nums: List[int]) -> int:
        left_sum = list(itertools.accumulate(nums))
        right_sum = list(itertools.accumulate(nums[::-1]))[::-1]
        for i in range(len(nums)):
            if left_sum[i] == right_sum[i]:
                return i
        return -1


    #   runtime: beats 94%
    def pivotIndex_ans(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        for i, n in enumerate(nums):
            if left_sum == (total - left_sum - n):
                return i
            left_sum += n
        return -1


s = Solution()
test_functions = [ s.pivotIndex_i, s.pivotIndex_ii, s.pivotIndex_ans, ]

inputs = [ [1,7,3,6,5,6], [1,2,3], [2,1,-1], ]
checks = [ 3, -1, 0, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for vals, check in zip(inputs, checks):
        print(f"vals=({vals})")
        result = f(vals)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

