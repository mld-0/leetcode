import time
import copy
from typing import List, Optional

class Solution:
    """Compress the input `chars`, replacing any consecutive repeating characters with a single character followed by the number of that character, in-place"""

    #   runtime: beats 99%
    def compress(self, chars: List[str]) -> int:
        l = 0
        r = 0
        r_previous = r
        while r <= len(chars):
            while r < len(chars) and chars[r] == chars[r_previous]:
                r += 1
            delta = r - r_previous
            encode = chars[r_previous]
            if delta > 1:
                encode += str(delta)
            for c in encode:
                chars[l] = c
                l += 1
            r_previous = r
            r += 1
        return l


s = Solution()
test_functions = [ s.compress, ]

inputs = [ ["a","a","b","b","c","c","c"], ["a"], ["a","b","b","b","b","b","b","b","b","b","b","b","b"], ["a","b","c"], ]
checks = [ (6,["a","2","b","2","c","3"]), (1,["a"]), (4,["a","b","1","2"]), (3,["a","b","c"]), ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for chars, (check_len, check_array) in zip(inputs, checks):
        chars = copy.deepcopy(chars)
        print(f"chars=({chars})")
        result = f(chars)
        print(f"result=({chars[:result]}, {result})")
        assert result == check_len, "Check comparison failed"
        assert chars[:check_len] == check_array, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

