#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
import math
from functools import cache
from typing import List, Optional

class Solution:
    """Starting with a single character, at each stage, we can either copy all current characters, or paste the last copy, determine the minimum number of operations to obtain 'n' characters"""

    #   runtime: MLE
    def minSteps_i(self, n: int) -> int:

        @cache
        def solve(current, copied, step):
            nonlocal n
            nonlocal result
            if step >= result:
                return
            if current > n:
                return
            if current == n:
                result = step
                return
            #   do not copy
            if current + copied <= n:
                solve(current+copied, copied, step+1)
            #   do copy
            if current + current <= n:
                solve(current, current, step+1)

        if n == 1:
            return 0
        result = math.inf
        solve(1, 1, 1)
        return result


    #   runtime: beats 55%
    #    memory: beats 13%
    def minSteps_ans_DP_TopDown(self, n: int) -> int:

        @cache
        def solve(current, copied):
            nonlocal n
            if current == n:
                return 0
            if current > n:
                return math.inf
            trial_a = math.inf
            trial_b = math.inf
            #   do not copy
            trial_a = 1 + solve(current+copied, copied)
            #   do copy
            trial_b = 2 + solve(current+current, current)
            return min(trial_a, trial_b)

        if n == 1:
            return 0
        result = 1 + solve(1, 1)
        return result


    def minSteps_ans_DP_BottomUp(self, n: int) -> int:
        raise NotImplementedError("review TopDown ans, continue BottomUp, Factorisation ans")


    def minSteps_ans_Factorisation(self, n: int) -> int:
        raise NotImplementedError("review TopDown ans, continue BottomUp, Factorisation ans")



s = Solution()
test_functions = [ s.minSteps_i, s.minSteps_ans_DP_TopDown, s.minSteps_ans_DP_BottomUp, ]

inputs = [ 3, 1, 18, 25, 111, ]
checks = [ 3, 0, 8, 10, 40, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for s, check in zip(inputs, checks):
        print(f"s=({s})")
        result = f(s)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

