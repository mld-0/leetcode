import time
from collections import defaultdict
from typing import List, Optional

class Solution:
    """Find the number of (non-sequential) subsequences of `s` which are three letter palindromes"""

    #   runtime: beats 48%
    def countPalindromicSubsequence_i(self, s: str) -> int:
        letter_positions = defaultdict(list)
        for i, c in enumerate(s):
            letter_positions[c].append(i)
        result = 0
        for c, positions in letter_positions.items():
            if len(positions) <= 1:
                continue
            l = positions[0]
            r = positions[-1]
            seen = set()
            for i in range(l+1, r):
                seen.add(s[i])
            result += len(seen)
        return result


    #   runtime: beats 53%
    def countPalindromicSubsequence_ii(self, s: str) -> int:
        letters = set(s)
        result = 0
        for c in letters:
            l = s.find(c)
            r = s.rfind(c)
            if l == r:
                continue
            seen = set()
            for i in range(l+1, r):
                seen.add(s[i])
            result += len(seen)
        return result


    #   runtime: beats 96%
    def countPalindromicSubsequence_iii(self, s: str) -> int:
        letters = set(s)
        result = 0
        for c in letters:
            l = s.find(c)
            r = s.rfind(c)
            if l == r:
                continue
            result += len(set(s[l+1:r]))
        return result


    #   runtime: beats 93%
    def countPalindromicSubsequence_ans_CountBetween_OneLiner(self, s: str) -> int:
        return sum([len(set(s[s.index(letter)+1:s.rindex(letter)])) for letter in set(s)])


s = Solution()
test_functions = [ s.countPalindromicSubsequence_i, s.countPalindromicSubsequence_ii, s.countPalindromicSubsequence_iii, s.countPalindromicSubsequence_ans_CountBetween_OneLiner, ]

inputs = [ "aabca", "adc", "bbcbaba", "tlpjzdmtwderpkpmgoyrcxttiheassztncqvnfjeyxxp" ]
checks = [ 3, 0, 4, 161, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for vals, check in zip(inputs, checks):
        print(f"vals=({vals})")
        result = f(vals)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

