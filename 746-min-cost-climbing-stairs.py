import time
import math
from functools import cache
from typing import List, Optional

class Solution:
    """Determine the minimum cost to reach the top of the staircase, where `cost[i]` is the cost of the `i`th step. After paying the cost of a step, we can climb either one or two stairs. We may start from the 0th or 1st step."""

    #   runtime: beats 90%
    def minCostClimbingStairs_TopDown(self, cost: List[int]) -> int:
        L = len(cost) - 1
        #   table[i]: min cost of reaching the top, starting at stair i
        table = [ math.inf for _ in range(len(cost)) ]
        table[L] = cost[L]
        table[L-1] = cost[L-1]
        for i in range(L-2, -1, -1):
            if table[i+1] > table[i+2]:
                table[i] = table[i+2] + cost[i]
            else:
                table[i] = table[i+1] + cost[i]
        return min(table[0], table[1])


    #   runtime: beats 25%
    def minCostClimbingStairs_BottomUp(self, cost: List[int]) -> int:

        @cache
        def solve(i):
            if i == len(cost)-1 or i == len(cost)-2:
                return cost[i]
            a = solve(i+1)
            b = solve(i+2)
            if b < a:
                return solve(i+2) + cost[i]
            else:
                return solve(i+1) + cost[i]

        return min(solve(0), solve(1))


s = Solution()
test_functions = [ s.minCostClimbingStairs_TopDown, s.minCostClimbingStairs_BottomUp, ]

inputs = [ [10,15,20], [1,100,1,1,1,100,1,1,100,1], ]
checks = [ 15, 6, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for cost, check in zip(inputs, checks):
        print(f"cost=({cost})")
        result = f(cost)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

