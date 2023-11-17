import time
import copy
import math
from typing import List, Optional

class Solution:
    """Given list of numbers, `nums`, divide its elements into pairs such that the sum of the pair with the largest sum is minimised"""

    #   runtime: beats 46%
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = -math.inf
        l = 0
        r = len(nums) - 1
        while l < r:
            pair = (nums[l], nums[r])
            result = max(result, sum(pair))
            l += 1
            r -= 1
        return result


    #   runtime: beats 75%
    def minPairSum_ans(self, nums: List[int]) -> int:
        nums.sort()
        return max(a+b for a,b in zip(nums, nums[::-1]))


s = Solution()
test_functions = [ s.minPairSum, s.minPairSum_ans, ]

inputs = [ [3,5,2,3], [3,5,4,2,4,6], ]
checks = [ 7, 8, ]
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

