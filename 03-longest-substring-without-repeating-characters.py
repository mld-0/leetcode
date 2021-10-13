#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
from collections import defaultdict
import functools
#   {{{2

class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        """Determine length of longest substring in 's' containing no repeat characters"""
        #return self.lengthOfLongestSubstring_BruteForce(s)
        return self.lengthOfLongestSubstring_SlidingWindowSeenDict(s)


    #   runtime: beats 5%
    def lengthOfLongestSubstring_BruteForce(self, s: str) -> int:
        longest = ""
        for i, val_i in enumerate(s):
            for j in range(i, len(s)):
                if len(s[i:j+1]) == len(set(s[i:j+1])):
                    if len(s[i:j+1]) > len(longest):
                        longest = s[i:j+1]
                else:
                    break
        return len(longest)


    #   runtime: beats 53%
    def lengthOfLongestSubstring_SlidingWindow(self, s: str) -> int:
        result = ""
        l = 0
        window_counter = defaultdict(int)

        for r in range(len(s)):
            window_counter[s[r]] += 1
            while l < r and window_counter[s[r]] > 1:
                window_counter[s[l]] -= 1
                l += 1
            trial = s[l:r+1]
            if len(trial) > len(result):
                result = trial

        return len(result)


    #   runtime: beats 87%
    def lengthOfLongestSubstring_SlidingWindowSeenDict(self, s: str) -> int:
        result = ""
        l = 0

        #   seen[c]: position where 'c' last seen
        seen = dict()

        for r in range(len(s)):
            #   character at 'r' seen before, advance 'l' to after previous instance of said character
            if s[r] in seen and seen[s[r]] >= l:
                l = seen[s[r]] + 1
            trial = s[l:r+1]
            if len(trial) > len(result):
                result = trial
            seen[s[r]] = r

        return len(result)


s = Solution()

input_values = [ "abcabcbb", "bbbbb", "pwwkew", "", " ", ]
input_checks = [ 3, 1, 3, 0, 1, ]

for input_str, check in zip(input_values, input_checks):
    print("input_str=(%s)" % input_str)
    result = s.lengthOfLongestSubstring(input_str)
    print("result=(%s)" % result)
    assert result == check, "Check failed"
    print()

