#   {{{3
       #   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
from typing import List, Optional

class Solution:
    """Determine the length of the longest substring that contains at most two distinct characters"""

    #   runtime: beats 81%
    #    memory: beats 77%
    def lengthOfLongestSubstringTwoDistinct_SlidingWindowCounter(self, s: str) -> int:
        result = 0
        l = 0
        r = 0
        window_letters = dict()
        non_zero_counts = 0
        while r < len(s):
            r_c = s[r]
            if r_c not in window_letters or window_letters[r_c] == 0:
                window_letters[r_c] = 1
                non_zero_counts += 1
            else:
                window_letters[r_c] += 1
            while non_zero_counts > 2:
                l_c = s[l]
                window_letters[l_c] -= 1
                if window_letters[l_c] == 0:
                    non_zero_counts -= 1
                l += 1
            result = max(result, r-l+1)
            r += 1
        return result


    #   runtime: beats 98%
    #    memory: beats 77%
    def lengthOfLongestSubstringTwoDistinct_ans_TwoPointers(self, s: str) -> int:
        l = -1
        r = -1
        current = 0
        result = 0
        for i in range(len(s)):
            if l == -1 or s[i] == s[l]:
                l = i
                current += 1
            elif l == -1 or s[i] == s[r]:
                r = i
                current += 1
            else:
                if l < r:
                    current = i - l
                    l = i
                else:
                    current = i - r
                    r = i
            result = max(result, current)
        return result


s = Solution()
test_functions = [ s.lengthOfLongestSubstringTwoDistinct_SlidingWindowCounter, s.lengthOfLongestSubstringTwoDistinct_ans_SlidingWindow, ]

inputs = [ "eceba", "ccaabbb", "abc", ]
checks = [ 3, 5, 2, ]
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

