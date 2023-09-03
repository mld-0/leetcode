import time
from typing import List, Optional

class Solution:
    """Merge Strings by adding letters in alternating order"""

    #   runtime: beats 97%
    def mergeAlternately_twoPointers(self, word1: str, word2: str) -> str:
        l = 0
        r = 0
        result = ""
        while l < len(word1) and r < len(word2):
            result += word1[l]
            result += word2[r]
            l += 1
            r += 1
        while l < len(word1):
            result += word1[l]
            l += 1
        while r < len(word2):
            result += word2[r]
            r += 1
        return result


s = Solution()
test_functions = [ s.mergeAlternately_twoPointers, ]

inputs = [ ("abc","pqr"), ("ab","pqrs"), ("abcd","pq"), ]
checks = [ "apbqcr", "apbqrs", "apbqcd", ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for (word1, word2), check in zip(inputs, checks):
        print(f"word1=({word1}), word2=({word2})")
        result = f(word1, word2)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

