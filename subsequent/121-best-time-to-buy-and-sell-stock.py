import math
from typing import List

class Solution:

    #   runtime: beats 86%
    def maxProfit(self, prices: List[int]) -> int:
        minimum = math.inf
        result = -math.inf
        for price in prices:
            if price < minimum:
                minimum = price
            trial = price - minimum 
            if trial > result:
                result = trial
        return result


s = Solution()
test_functions = [ s.maxProfit, ]

inputs = [ [7,1,5,3,6,4], [7,6,4,3,1], ]
checks = [ 5, 0, ]
assert len(inputs) == len(checks)

for f in test_functions:
    print(f.__name__)
    for prices, check in zip(inputs, checks):
        print(f"prices=({prices})")
        result = f(prices)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print()


