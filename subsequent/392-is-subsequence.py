import time
from typing import List, Optional

class Solution:
    """Determine whether `s` can be formed from `t` by deleting some (or none) of the letters from the latter"""

    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        if s == t:
            return True
        l = 0
        r = 0
        while r < len(t):
            if s[l] == t[r]:
                l += 1
            if l >= len(s):
                return True
            r += 1
        return False
        

s = Solution()
test_functions = [ s.isSubsequence ]

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

