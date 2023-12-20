import time
import heapq
from typing import List, Optional

class Solution:

    #   runtime: beats 92%
    def buyChoco_iterative(self, prices: List[int], money: int) -> int:
        a, b = None, None
        if prices[0] < prices[1]:
            a, b = 0, 1
        else:
            a, b = 1, 0
        for i in range(2, len(prices)):
            if prices[i] <= prices[a]:
                b = a
                a = i
            elif prices[i] <= prices[b]:
                b = i
        if prices[a] + prices[b] > money:
            return money
        else:
            return money - prices[a] - prices[b]


    #   runtime: beats 96%
    def buyChoco_heapq(self, prices: List[int], money: int) -> int:
        a, b = heapq.nsmallest(2, prices)
        if a + b > money:
            return money
        else:
            return money - a - b


s = Solution()
test_functions = [ s.buyChoco_iterative, s.buyChoco_heapq, ]

inputs = [ ([1,2,2],3), ([3,2,3],3) ]
checks = [ 0, 3, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for (prices, money), check in zip(inputs, checks):
        print(f"prices=({prices}), money=({money})")
        result = f(prices, money)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

