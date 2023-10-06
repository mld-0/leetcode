#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
import math
import itertools
from functools import cache
import functools
from typing import List, Optional

class Solution:
    """Given integer `n`, break it into the sum of `k` positive integers in order to maximise the product of those integers, returning that maximum product"""

    #   runtime: TLE
    def integerBreak_naive(self, n: int) -> int:

        @cache
        def sum_options(n: int) -> List[int]:
            if n == 0:
                return [ [] ]
            if n == 1:
                return [ [1] ]
            result = set()
            for k in range(1, n+1):
                remaining_options = sum_options(n-k)
                for option in remaining_options:
                    loop_option = tuple(sorted( [k, *option] ))
                    result.add(loop_option)
            result = sorted(list(result))
            return result

        result = 0
        result_option = []
        options = sum_options(n)
        for option in options:
            if len(option) == 1:
                continue
            trial = functools.reduce(lambda x,y: x*y, option)
            if trial > result:
                result = trial
                result_option = option
        return result


    #   runtime: beats 99%
    def integerBreak_mathematical(self, n: int) -> int:
        if n == 2:
            return 1
        option = []
        while n > 0:
            if n == 6:
                n -= 6
                option.append(3)
                option.append(3)
            elif n >= 5:
                n -= 3
                option.append(3)
            elif n >= 2:
                n -= 2
                option.append(2)
            else:
                n -= 1
                option.append(1)
        return functools.reduce(lambda x,y: x*y, option)
                

s = Solution()
test_functions = [ s.integerBreak_naive, s.integerBreak_mathematical, ]

#   {{{
inputs = [ 10, 2, 6, 47, ]
checks = [ 36, 1, 9, 28697814, ]
#   }}}
inputs = [ 10, 2, 6, 12, 14, 15, 16, ]
checks = [ 36, 1, 9, 81, 162, 243, 324, ]
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

