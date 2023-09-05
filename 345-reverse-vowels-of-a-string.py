import time
from typing import List, Optional

class Solution:

    #   runtime: beats 99%
    def reverseVowels(self, s: str) -> str:
        s = [ c for c in s ]
        vowels = set( ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] )
        vowel_locations = []
        for i in range(len(s)):
            if s[i] in vowels:
                vowel_locations.append(i)
        l = 0
        r = len(vowel_locations) - 1
        while l < r:
            i, j = vowel_locations[l], vowel_locations[r]
            s[i], s[j] = s[j], s[i]
            l += 1
            r -= 1
        return ''.join(s)


s = Solution()
test_functions = [ s.reverseVowels, ]

inputs = [ "hello", "leetcode", "aA", ]
checks = [ "holle", "leotcede", "Aa", ]
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

