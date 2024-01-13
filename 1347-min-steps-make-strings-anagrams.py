import time
from collections import Counter
from typing import List, Optional

class Solution:

    #   runtime: beats 99%
    def minSteps(self, s: str, t: str) -> int:
        s_letters = Counter(s)
        t_letters = Counter(t)
        result = 0
        for letter, s_count in s_letters.items():
            t_count = t_letters[letter] if letter in t_letters else 0
            if t_count < s_count:
                result += s_count - t_count
        return result


s = Solution()
test_functions = [ s.minSteps, ]

inputs = [ ("bab","aba"), ("leetcode","practice"), ("anagram","mangaar"), ]
checks = [ 1, 5, 0, ]
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

