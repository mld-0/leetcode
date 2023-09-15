import time
from collections import Counter
from typing import List, Optional

class Solution:
    """Determine if `word2` can be constructed from `word1` by re-arranging the letters, and swapping every instance of a given pair of letters for one another"""

    #   runtime: beats 95%
    def closeStrings_Counter(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        c1 = Counter(word1)
        c2 = Counter(word2)
        return sorted(c1.keys()) == sorted(c2.keys()) and sorted(c1.values()) == sorted(c2.values())


    #   runtime: beats 20%
    def closeStrings_ans_FrequencyArray(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        c1 = [ 0 for _ in range(26) ]
        c2 = [ 0 for _ in range(26) ]
        for c in word1:
            c1[ord(c)-ord('a')] += 1
        for c in word2:
            c2[ord(c)-ord('a')] += 1
        for i in range(len(c1)):
            if (c1[i] > 0 and c2[i] == 0) or (c1[i] == 0 and c2[i] > 0):
                return False
        return sorted(c1) == sorted(c2)


    #   runtime: beats 5%
    def closeStrings_ans_FrequencyArrayAndBitwiseSet(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        c1 = [ 0 for _ in range(26) ]
        c2 = [ 0 for _ in range(26) ]
        s1 = 0
        s2 = 0
        for c in word1:
            c1[ord(c)-ord('a')] += 1
            s1 = s1 | (1 << (ord(c)-ord('a')))
        for c in word2:
            c2[ord(c)-ord('a')] += 1
            s2 = s2 | (1 << (ord(c)-ord('a')))
        if s1 != s2:
            return False
        return sorted(c1) == sorted(c2)


s = Solution()
test_functions = [ s.closeStrings_Counter, s.closeStrings_ans_FrequencyArray, s.closeStrings_ans_FrequencyArrayAndBitwiseSet, ]

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

