#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import math
import time
from typing import List

class Solution:

    #   123-best-time-to-buy-and-sell-stock-iii k=2 solutions:
    #   {{{
    #def maxProfit_k_eq_2_DP_bidirectional(self, prices: List[int]) -> int:
    #    forwards = [ None for _ in prices ]
    #    reverse = [ None for _ in prices ]
    #    lowest = math.inf
    #    profit = 0
    #    for i, x in enumerate(prices):
    #        lowest = min(lowest, x)
    #        profit = max(profit, x-lowest)
    #        forwards[i] = profit
    #    highest = -math.inf
    #    profit = 0
    #    for i, x in enumerate(reversed(prices)):
    #        highest = max(highest, x)
    #        profit = max(profit, highest - x)
    #        reverse[len(prices)-i-1] = profit
    #    result = 0
    #    for i in range(len(prices)):
    #        result = max(forwards[i] + reverse[i], result)
    #    return result
    #def maxProfit_k_eq_2_ans_DP_constSpace(self, prices: List[int]) -> int:
    #    t1_cost, t2_cost = math.inf, math.inf
    #    t1_profit, t2_profit = 0, 0
    #    for x in prices:
    #        t1_cost = min(t1_cost, x)
    #        t1_profit = max(t1_profit, x - t1_cost)
    #        t2_cost = min(t2_cost, x - t1_profit)
    #        t2_profit = max(t2_profit, x - t2_cost)
    #    return t2_profit
    #   }}}

    def maxProfit_greedy(self, prices: List[int]) -> int:
        result = 0
        i = 0
        while i < len(prices) - 1:
            if prices[i+1] > prices[i]:
                result += prices[i+1] - prices[i]
            i += 1
        return result


    #   runtime: beats 94%
    def maxProfit_generalise_k_eq_2_DP_constSpace(self, k: int, prices: List[int]) -> int:
        if 2*k > len(prices):
            return self.maxProfit_greedy(prices)

        costs = [ math.inf for _ in range(k) ]
        profits = [ 0 for _ in range(k) ] 

        for x in prices:
            costs[0] = min(costs[0], x)
            profits[0] = max(profits[0], x-costs[0])
            for i in range(1, k):
                costs[i] = min(costs[i], x - profits[i-1])
                profits[i] = max(profits[i], x - costs[i])

        return profits[-1]


    #   runtime: beats 48%
    def maxProfit_ans_DP_two_tables(self, k: int, prices: List[int]) -> int:
        if 2*k > len(prices):
            return self.maxProfit_greedy(prices)

        #   i = day, j = number of completed transactions
        hold = [ [ -math.inf for _ in range(k+1) ] for _ in range(len(prices)) ]
        not_hold = [ [ -math.inf for _ in range(k+1) ] for _ in range(len(prices)) ]

        #   initial conditions:
        hold[0][1] = -1 * prices[0]
        not_hold[0][0] = 0

        for i in range(1, len(prices)):
            for j in range(k+1):
                not_hold[i][j] = max( not_hold[i-1][j], hold[i-1][j] + prices[i] )
                if j > 0:
                    hold[i][j] = max( hold[i-1][j], not_hold[i-1][j-1] - prices[i] )

        result = 0
        for j in range(k+1):
            result = max(result, not_hold[-1][j])
        return result


    def maxProfit_ans_merging(self, k: int, prices: List[int]) -> int:
        raise NotImplementedError()


    def maxProfit_ans_DP_one_table(self, k: int, prices: List[int]) -> int:
        raise NotImplementedError()


s = Solution()
test_functions = [ s.maxProfit_generalise_k_eq_2_DP_constSpace, s.maxProfit_ans_DP_two_tables, ]

inputs = [ (1,[7,1,5,3,6,4]), (1,[7,6,4,3,1]), (2,[2,4,1]), (2,[3,2,6,5,0,3]), (4,[1,2,4,2,5,7,2,4,9,0]), ]
checks = [ 5, 0, 2, 7, 15, ]
assert len(inputs) == len(checks)

for f in test_functions:
    print(f.__name__)
    startTime = time.time()
    for (k, prices), check in zip(inputs, checks):
        print(f"k=({k}), prices=({prices})")
        result = f(k, prices)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_ms=(%0.2f)" % ((time.time() - startTime) * 1000000))
    print()

