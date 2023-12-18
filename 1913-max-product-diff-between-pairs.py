import time
import copy
import heapq
from typing import List, Optional

class Solution:

    #   runtime: beats 70%
    def maxProductDifference_Sorting(self, nums: List[int]) -> int:
        nums.sort()
        return nums[-1] * nums[-2] - nums[0] * nums[1]


    #   runtime: beats 95%
    def maxProductDifference_Heap(self, nums: List[int]) -> int:
        a = heapq.nlargest(2, nums)
        b = heapq.nsmallest(2, nums)
        return a[0] * a[1] - b[0] * b[1]


s = Solution()
test_functions = [ s.maxProductDifference_Sorting, s.maxProductDifference_Heap, ]

inputs = [ [5,6,2,7,4], [4,2,5,9,7,4,8], ]
checks = [ 34, 64, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for nums, check in zip(inputs, checks):
        nums = copy.deepcopy(nums)
        print(f"nums=({nums})")
        result = f(nums)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

