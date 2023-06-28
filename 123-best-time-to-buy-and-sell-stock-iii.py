import time
import math
from typing import List

class Solution:

    #   runtime: beats 54%
    def maxProfit_DP_bidirectional(self, prices: List[int]) -> int:
        forwards = [ None for _ in prices ]
        reverse = [ None for _ in prices ]

        lowest = math.inf
        profit = 0
        for i, x in enumerate(prices):
            lowest = min(lowest, x)
            profit = max(profit, x-lowest)
            forwards[i] = profit

        highest = -math.inf
        profit = 0
        for i, x in enumerate(reversed(prices)):
            highest = max(highest, x)
            profit = max(profit, highest - x)
            reverse[len(prices)-i-1] = profit

        result = 0
        for i in range(len(prices)):
            result = max(forwards[i] + reverse[i], result)
        return result


s = Solution()
test_functions = [ s.maxProfit_DP_bidirectional, ]

inputs = [ [3,3,5,0,0,3,1,4], [1,2,3,4,5], [7,6,4,3,1], ]
checks = [ 6, 4, 0, ]
assert len(inputs) == len(checks)

for f in test_functions:
    print(f.__name__)
    startTime = time.time()
    for prices, check in zip(inputs, checks):
        print(f"inputs=({inputs})")
        result = f(prices)
        print(f"result=({result})")
        #assert result == check, "Check comparison failed"
    print("elapsed_ms=(%0.2f)" % ((time.time() - startTime) * 1000000))
    print()

