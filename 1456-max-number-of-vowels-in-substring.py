import time
from typing import List, Optional

class Solution:
    """Return the maximum number of vowels in any substring of `s` with length`k`"""

    #   runtime: beats 95%
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set( ['a', 'e', 'i', 'o', 'u'] )
        count = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1
        result = count
        for i in range(len(s)-k):
            if s[i] in vowels:
                count -= 1
            if s[i+k] in vowels:
                count += 1
            result = max(result, count)
        return result


s = Solution()
test_functions = [ s.maxVowels, ]

inputs = [ ("abciiidef",3), ("aeiou",2), ("leetcode",3), ]
checks = [ 3, 2, 2, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for (s, k), check in zip(inputs, checks):
        print(f"s=({s}), k=({k})")
        result = f(s, k)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()


