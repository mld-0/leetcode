import time
import itertools
from typing import List, Optional

class Solution:
    """Find the number of contiguous substrings in `s` where all characters in the substring are the same"""

    #   runtime: beats 12%
    def countHomogenous_i(self, s: str) -> int:
        splits = []
        current = [ s[0] ]
        i = 1
        while i < len(s):
            if s[i] == current[-1]:
                current.append(s[i])
            else:
                splits.append(''.join(current))
                current = [ s[i] ]
            i += 1
        splits.append(''.join(current))
        result = 0
        for split in splits:
            n = len(split)
            result += (n * (n+1)) // 2
        return result % (10 ** 9 + 7)


    #   runtime: beats 33%
    def countHomogenous_ii(self, s: str) -> int:
        result = 0
        current = s[0]
        current_length = 1
        i = 1
        while i < len(s):
            if s[i] == current:
                current_length += 1
            else:
                result += (current_length * (current_length+1)) // 2
                current = s[i]
                current_length = 1
            i += 1
        result += (current_length * (current_length+1)) // 2
        return result % (10 ** 9 + 7)


    #   runtime: beats 30%
    def countHomogenous_ans_i(self, s: str) -> int:
        result = 0
        curr_streak = 0
        MOD = 10 ** 9 + 7
        for i in range(len(s)):
            if i == 0 or s[i] == s[i - 1]:
                curr_streak += 1
            else:
                curr_streak = 1
            result = (result + curr_streak) % MOD
        return result


    #   runtime: beats 98%
    def countHomogenous_ans_groupby(self, s):
        result = 0
        for c, s in itertools.groupby(s):
            n = len(list(s))
            result += (n * (n + 1)) // 2
        return result % (10**9 + 7)


s = Solution()
test_functions = [ s.countHomogenous_i, s.countHomogenous_ii, s.countHomogenous_ans_i, s.countHomogenous_ans_groupby, ]

inputs = [ "abbcccaa", "xy", "zzzzz", ]
checks = [ 13, 2, 15, ]
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

