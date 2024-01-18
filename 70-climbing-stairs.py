import time
import functools
from typing import List, Optional

class Solution:
    """How many ways can a staircase of `n` steps be climbed, if at each stage, 1 or 2 steps can be climbed"""

    #   runtime: beats 95%
    def climbStairs_RecursiveMemoize(self, n: int) -> int:
        memo = { 0: 0, 1: 1, 2: 2, }

        def solve(n: int) -> int:
            if n in memo:
                return memo[n]
            result = solve(n-1) + solve(n-2)
            memo[n] = result
            return result

        return solve(n)


    #   runtime: beats 91%
    def climbStairs_DP_BottomUp(self, n: int) -> int:
        if n < 3:
            return n

        #   table[i]: number of ways to climb staircase, starting at `i`-th stair
        table = [ None for _ in range(n+1) ]
        table[0] = 0
        table[1] = 1
        table[2] = 2
        for i in range(3, n+1):
            table[i] = table[i-1] + table[i-2]

        return table[n]


    #   runtime: beats 91%
    def climbStairs_ans_Fibonacci(self, n: int) -> int:
        if n < 3:
            return n
        a = 1
        b = 2
        for i in range(3, n+1):
            b, a = b + a, b
        return b


    #   runtime: beats 99%
    @functools.lru_cache()
    def climbStairs_RecursiveMemoizeLRUCache(self, n: int) -> int:
        if n < 3:
            return n
        return self.climbStairs_RecursiveMemoizeLRUCache(n-1) + self.climbStairs_RecursiveMemoizeLRUCache(n-2)


    #   runtime: beats 98%
    @functools.cache
    def climbStairs_RecursiveMemoizeDecorator(self, n: int) -> int:
        if n < 3:
            return n
        return self.climbStairs_RecursiveMemoizeDecorator(n-1) + self.climbStairs_RecursiveMemoizeDecorator(n-2)


s = Solution()
test_functions = [ s.climbStairs_RecursiveMemoize, s.climbStairs_DP_BottomUp, s.climbStairs_ans_Fibonacci, s.climbStairs_RecursiveMemoizeLRUCache, s.climbStairs_RecursiveMemoizeDecorator, ]

inputs = [ 1, 2, 3, 44, ]
checks = [ 1, 2, 3, 1134903170, ]
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

