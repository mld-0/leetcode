import time
import math
from typing import List, Optional

class Solution:

    #   runtime: TLE
    def maxProfit_recursive(self, prices: List[int]) -> int:

        def solve(prices: List[int], holding: Optional[int]) -> int:
            if len(prices) == 0:
                return 0
            result = 0
            for i in range(len(prices)):
                sell = -math.inf
                hold = -math.inf
                buy = -math.inf
                if not holding is None:
                    sell = prices[i] + solve(prices[i+1:], None)
                else:
                    buy = solve(prices[i+1:], prices[i]) - prices[i]
                hold = solve(prices[i+1:], holding)
                result = max(result, sell, hold, buy)
            return result

        return solve(prices, None)
        

    #   runtime: TLE
    def maxProfit_recursiveMemoize(self, prices: List[int]) -> int:
        memoize = dict()

        def solve(prices: List[int], holding: Optional[int]) -> int:
            if len(prices) == 0:
                return 0
            if (tuple(prices),holding) in memoize:
                return memoize[(tuple(prices),holding)]
            result = 0
            for i in range(len(prices)):
                sell = -math.inf
                hold = -math.inf
                buy = -math.inf
                if not holding is None:
                    sell = prices[i] + solve(prices[i+1:], None)
                else:
                    buy = solve(prices[i+1:], prices[i]) - prices[i]
                hold = solve(prices[i+1:], holding)
                result = max(result, sell, hold, buy)
            memoize[(tuple(prices),holding)] = result
            return result

        return solve(prices, None)


s = Solution()
test_functions = [ s.maxProfit_recursive, s.maxProfit_recursiveMemoize, ]

inputs = [ [7,1,5,3,6,4], [1,2,3,4,5], [7,6,4,3,1], ]
checks = [ 7, 4, 0, ]
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

