import time
from collections import Counter
from typing import List, Optional

class Solution:
    """Determine if `word2` can be constructed from `word1` by re-arranging the letters, and swapping every instance of a given pair of letters for one another"""

    #   runtime: beats 86%
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        word1_counts = Counter(word1)
        word2_counts = Counter(word2)
        return sorted(word1_counts.keys()) == sorted(word2_counts.keys()) and sorted(word1_counts.values()) == sorted(word2_counts.values())


s = Solution()
test_functions = [ s.closeStrings, ]

inputs = [ ("abc","bca"), ("a","aa"), ("cabbba","abbccc"), ("aaabbbbccddeeeeefffff","aaaaabbcccdddeeeeffff"), ("uau","ssx"), ]
checks = [ True, False, True, False, False, ]
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

