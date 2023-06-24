import time
import math
from functools import cache
from typing import List, Tuple, Optional

class Solution:

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


    #   runtime: beats 97%
    def maxProfit_greedy(self, prices: List[int]) -> int:
        result = 0
        high = prices[0]
        low = prices[0]
        i = 0
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i+1] <= prices[i]:
                i += 1
            low = prices[i]
            while i < len(prices) - 1 and prices[i+1] >= prices[i]:
                i += 1
            high = prices[i]
            result += high - low 
        return result


    #   runtime: beats 94%
    def maxProfit_greedy_simplified(self, prices: List[int]) -> int:
        result = 0
        i = 0
        while i < len(prices) - 1:
            if prices[i+1] > prices[i]:
                result += prices[i+1] - prices[i]
            i += 1
        return result


    #   runtime: beats 79%
    def maxProfit_ans_DP_bottomUp(self, prices: List[int]) -> int:
        cur_hold = -math.inf
        cur_not_hold = 0
        for p in prices:
            prev_hold, prev_not_hold = cur_hold, cur_not_hold
            #   either continue to hold, or sell 
            cur_hold = max(prev_hold, prev_not_hold - p)
            #   either continue to not-hold, or buy
            cur_not_hold = max(prev_not_hold, prev_hold + p)
        return cur_not_hold


    #   runtime: beats 34%
    def maxProfit_ans_DP_topDown(self, prices: List[int]) -> int:
        memoize = dict()

        def solve(day: int) -> Tuple[int,int]:
            if day == 0:
                return ( -prices[0], 0 )
            if day in memoize:
                return memoize[day]
            prev_hold, prev_not_hold = solve(day - 1)
            cur_hold = max(prev_hold, prev_not_hold - prices[day])            
            cur_not_hold = max(prev_not_hold, prev_hold + prices[day])
            memoize[day] = (cur_hold, cur_not_hold)
            return (cur_hold, cur_not_hold)

        cur_hold, cur_not_hold = solve(len(prices) - 1)
        return cur_not_hold


s = Solution()
test_functions = [ s.maxProfit_recursiveMemoize, s.maxProfit_greedy, s.maxProfit_greedy_simplified, s.maxProfit_ans_DP_bottomUp, s.maxProfit_ans_DP_topDown, ]

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

