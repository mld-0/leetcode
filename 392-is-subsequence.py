import time
import pprint
from collections import defaultdict
from functools import cache
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


    #   runtime: beats 99%
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

    
    #   runtime: beats 97%
    def isSubsequence_Map(self, s: str, t: str) -> bool:
        d = defaultdict(list)
        for i, c in enumerate(t):
            d[c].append(i)
        l = -1
        for c in s:
            if c not in d:
                return False
            l_previous = l
            for i in d[c]:
                if i > l:
                    l = i
                    break
            if l == l_previous:
                return False
        return True


    #   runtime: beats 6%
    def isSubsequence_DP_BottomUp(self, s: str, t: str) -> bool:
        if s == t or len(s) == 0:
            return True
        if len(s) > len(t):
            return False 

        #   table[i][j]: max length of the subsequence of s[:i] that can be constructed from t[:j] by deleting characters from the latter
        table = [ [ 0 for _ in range(len(t)+1) ] for _ in range(len(s)+1) ]

        for col in range(1, len(t)+1):
            for row in range(1, len(s)+1):
                if s[row-1] == t[col-1]:
                    table[row][col] = table[row-1][col-1] + 1
                else:
                    table[row][col] = max(table[row][col-1], table[row-1][col])

            if table[-1][col] == len(s):
                return True
            
        return False


    #   runtime: beats 6%
    def isSubsequence_DP_TopDown(self, s: str, t: str) -> bool:
        if s == t or len(s) == 0:
            return True
        if len(s) > len(t):
            return False 

        @cache
        def solve(row: int, col: int) -> bool:
            if row == len(s):
                return True
            if col == len(t):
                return False
            if s[row] == t[col]:
                return solve(row+1, col+1) or solve(row, col+1)
            else:
                return solve(row, col+1)

        return solve(0, 0)


s = Solution()
test_functions = [ s.isSubsequence_twoPointers, s.isSubsequence_Recursive, s.isSubsequence_Map, s.isSubsequence_DP_BottomUp, s.isSubsequence_DP_TopDown, ]

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

