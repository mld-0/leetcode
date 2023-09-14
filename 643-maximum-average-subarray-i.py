import time
import math
from typing import List, Optional

class Solution:
    """Find the contiguious subarray of length `k` in `nums` with the largest average (and return that average)"""

    #   runtime: beats 89%
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        subarray_sum = sum(nums[:k])
        result = subarray_sum / k
        for l in range(0, len(nums)-k):
            subarray_sum = subarray_sum - nums[l] + nums[l+k]
            result = max(result, subarray_sum / k)
        return result


s = Solution()
test_functions = [ s.findMaxAverage, ]

inputs = [ ([1,12,-5,-6,50,3],4), ([5],1), ([1,2,3,4,5],2), ]
checks = [ 12.75, 5.0, 4.5, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for (nums, k), check in zip(inputs, checks):
        print(f"nums=({nums}), k=({k})")
        result = f(nums, k)
        print(f"result=({result})")
        assert abs(result-check) <= 10**-5, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

