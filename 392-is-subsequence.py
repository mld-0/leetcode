import time
from collections import defaultdict
from typing import List, Optional

class Solution:
    """Determine whether `s` can be formed from `t` by deleting some (or none) of the letters from the latter"""

    #   runtime: beats 98%
    def isSubsequence_twoPointers(self, s: str, t: str) -> bool:
        if s == t or len(s) == 0:
            return True
        if len(s) > len(t):
            return False
        l = 0
        for c in t:
            if c == s[l]:
                l += 1
            if l == len(s):
                return True
        return False


    def isSubsequence_Recursive(self, s: str, t: str) -> bool:

        def solve(l: int, r: int) -> bool:
            if l == len(s):
                return True
            if r == len(t):
                return False
            if s[l] == t[r]:
                l += 1
            r += 1
            return solve(l, r)

        return solve(0, 0)

    
    def isSubsequence_Map(self, s: str, t: str) -> bool:
        d = defaultdict(list)
        for i, c in enumerate(t):
            d[c].append(i)
        raise NotImplementedError()


    def isSubsequence_DP(self, s: str, t: str) -> bool:
        raise NotImplementedError()


s = Solution()
test_functions = [ s.isSubsequence_twoPointers, s.isSubsequence_Recursive, s.isSubsequence_Map, s.isSubsequence_DP, ]

inputs = [ ("abc","ahbgdc"), ("axc","ahbgdc"), ("","ahbgdc"), ("b","abc"), ]
checks = [ True, False, True, True, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for (s, t), check in zip(inputs, checks):
        print(f"s=({s}), t=({t})")
        result = f(s, t)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

