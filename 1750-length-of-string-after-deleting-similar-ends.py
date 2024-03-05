#   {{{3
       #   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
from typing import List, Optional

class Solution:
    """Given a string, repeatedly remove continuous sequences of characters from the start and end for so long as the character of those start/end sequences match, then return the length of the remaining string"""

    #   runtime: beats 11%
    def minimumLength_TwoPointers_Substrings(self, s: str) -> int:

        def trim_ends(s):
            if len(s) == 0:
                return ""
            if len(s) == 1:
                return s
            l = 0
            r = len(s) - 1
            if s[l] != s[r]:
                return s
            while s[l] == s[0] and l < r:
                l += 1
            while s[r] == s[0] and l <= r:
                r -= 1
            return s[l:r+1]

        previous = None
        current = s
        while current != previous:
            previous = current
            current = trim_ends(current)
        return len(current)


    #   runtime: beats 98%
    def minimumLength_TwoPointers_TailRecursion(self, s: str) -> int:

        def trim_ends(s, l, r):
            if r - l + 1 == 0:
                return 0
            if r - l + 1 == 1:
                return 1
            if s[l] != s[r]:
                return r - l + 1
            c = s[l]
            while s[l] == c and l < r:
                l += 1
            while s[r] == c and l <= r:
                r -= 1
            return trim_ends(s, l, r)

        return trim_ends(s, 0, len(s)-1)


    #   runtime: beats 99%
    def minimumLength_TwoPointers_Iterative(self, s: str) -> int:
        l = 0
        r = len(s) - 1
        while l <= r:
            if r == l:
                return 1
            if s[l] != s[r]:
                return r - l + 1
            current = s[l]
            while s[l] == current and l < r:
                l += 1
            while s[r] == current and l <= r:
                r -= 1
        return 0


s = Solution()
test_functions = [ s.minimumLength_TwoPointers_Substrings, s.minimumLength_TwoPointers_TailRecursion, s.minimumLength_TwoPointers_Iterative, ]

inputs = [ "ca", "cabaabac", "aabccabba", "bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb", "c", ]
checks = [ 2, 0, 3, 1, 1, ]
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

