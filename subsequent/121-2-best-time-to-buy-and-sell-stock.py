import time
import math
from typing import List

class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        lowest = math.inf
        profit = 0
        for x in prices:
            lowest = min(lowest, x)
            profit = max(profit, x-lowest)
        return profit


s = Solution()
test_functions = [ s.maxProfit, ]

inputs = [ [7,1,5,3,6,4], [7,6,4,3,1], ]
checks = [ 5, 0, ]
assert len(inputs) == len(checks)

for f in test_functions:
    print(f.__name__)
    startTime = time.time()
    for prices, check in zip(inputs, checks):
        print(f"prices=({prices})")
        result = f(prices)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_ms=(%0.2f)" % ((time.time() - startTime) * 1000000))
    print()

