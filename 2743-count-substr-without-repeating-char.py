#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
from collections import defaultdict
from typing import List, Optional

class Solution:
    """Count the number of substrings that contain no duplicate characters"""

    #   runtime: beats 53%
    #    memory: beats 62%
    def numberOfSpecialSubstrings_i(self, s: str) -> int:
        result = 0
        counter = defaultdict(int)
        l = 0
        r = 0
        while r < len(s):
            while counter[s[r]] >= 1:
                counter[s[l]] -= 1
                l += 1
            counter[s[r]] += 1
            r += 1
            delta = r - l
            result += delta
        return result


    #   runtime: beats 65%
    #    memory: beats 62%
    def numberOfSpecialSubstrings_ii(self, s: str) -> int:
        result = 0
        counter = [ 0 ] * 26
        ord_z = ord('z')
        l = 0
        for r in range(len(s)):
            while counter[ord_z-ord(s[r])] >= 1:
                counter[ord_z-ord(s[l])] -= 1
                l += 1
            counter[ord_z-ord(s[r])] += 1
            result += r - l + 1
        return result


s = Solution()
test_functions = [ s.numberOfSpecialSubstrings_i, s.numberOfSpecialSubstrings_ii, ]

inputs = [ "abcd", "ooo", "abab", ]
checks = [ 10, 3, 7, ]
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

