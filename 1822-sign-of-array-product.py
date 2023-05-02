import time
import math
from typing import List

class Solution:

    #   runtime: beats 9%
    def arraySign_i(self, nums: List[int]) -> int:
        product = math.prod(nums)
        if product > 0:
            return 1
        elif product < 0:
            return -1
        else:
            return 0

    #   runtime: beats 11%
    def arraySign_ii(self, nums: List[int]) -> int:
        count_negative = 0
        for n in nums:
            if n == 0:
                return 0
            elif n < 0:
                count_negative += 1
        if count_negative % 2 == 1:
            return -1
        else:
            return 1


s = Solution()
test_functions = [ s.arraySign_i, s.arraySign_ii, ]

inputs = [ [-1,-2,-3,-4,3,2,1], [1,5,0,2,-3], [-1,1,-1,1,-1], ]
checks = [ 1, 0, -1, ]
assert len(inputs) == len(checks)

for f in test_functions:
    print(f.__name__)
    startTime = time.time()
    for nums, check in zip(inputs, checks):
        print(f"nums=({nums})")
        result = f(nums)
        print(f"result=({result})")
        assert result == check
    print("elapsed_ms=(%0.2f)" % ((time.time() - startTime) * 1000000))
