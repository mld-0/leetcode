import time
from functools import cache
from typing import List, Optional

class Solution:

    #   runtime: beats 91%
    def tribonacci_DP_TopDown(self, n: int) -> int:

        @cache
        def solve(n: int) -> int:
            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1
            return solve(n-3) + solve(n-2) + solve(n-1)

        return solve(n)


    #   runtime: beats 95%
    def tribonacci_DP_BottomUp(self, n: int) -> int:
        table = [ 0, 1, 1, ]
        while len(table) <= n:
            table.append(table[-1] + table[-2] + table[-3])
        return table[n]


s = Solution()
test_functions = [ s.tribonacci_DP_TopDown, s.tribonacci_DP_BottomUp, ]

inputs = [ 4, 25, 7, 9, 31, ]
checks = [ 4, 1389537, 24, 81, 53798080,  ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for n, check in zip(inputs, checks):
        print(f"n=({n})")
        result = f(n)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

