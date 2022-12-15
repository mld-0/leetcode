#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
from typing import List
import pprint
#   {{{2
class Solution:

    #   Brute force solution - time limit exceded
    def longestPalindrome_BruteForce(self, s: str) -> str:

        def is_palindrome(s: str) -> bool:
            result = s == s[::-1]
            return result

        result = ""
        for i in range(0, len(s)):
            for j in range(i+1, len(s)+1):
                loop_str = s[i:j]
                if is_palindrome(loop_str):
                    if len(loop_str) > len(result):
                        result = loop_str
        return result


    #   runtime: beats 15%
    def longestPalindrome_DP_BottomUp(self, s: str) -> str:
        #   longest palindrome is given by s[start:end+1]
        start = 0
        end = 0

        #   is_palindrome[i][j]: True if s[i:j+1] is a palindrome
        is_palindrome = [ [ False for y in range(len(s)) ] for x in range(len(s)) ]

        #   All substrings of length 1 are palindromes
        for i in range(len(s)):
            is_palindrome[i][i] = True

        #   Substrings of length 2 are palindromes if start/end letters match
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                is_palindrome[i][i+1] = True
                start = i
                end = i + 1

        #   s[l:r+1] is a palindrome if s[l] == s[r] and is_palindrome[l+1][r-1] == True
        for r in range(1, len(s)):
            for l in range(r-2, -1, -1):
                if s[l] == s[r] and is_palindrome[l+1][r-1]:
                    is_palindrome[l][r] = True
                    if r-l > end-start:
                        end = r
                        start = l

        return s[start:end+1]

    
    #   TODO: 2021-10-26T17:21:24AEDT _leetcode, 05-longest-palindromic-substring, intuition for TwoPointers solution
    #   runtime: beats 91%
    def longestPalindrome_TwoPointers(self, s: str) -> str:
        result_start = 0
        result_len = 1

        for i in range(0, len(s)):
            r = i
            while r < len(s) and s[i] == s[r]:
                r += 1

            l = i - 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            trial_len = r - l - 1
            if trial_len > result_len:
                result_len = trial_len
                result_start = l + 1

        return s[result_start:result_start+result_len]


s = Solution()

input_values = [ "debabec", "ceebababefd", "a", "ac", "bb" ]
input_checks = [ "ebabe", "ebababe", "a", [ "a", "c" ], "bb" ]

test_functions = [ s.longestPalindrome_BruteForce, s.longestPalindrome_DP_BottomUp, s.longestPalindrome_TwoPointers, ]

for test_func in test_functions:
    print(test_func.__name__)
    for text, check in zip(input_values, input_checks):
        print("text=(%s)" % text)
        result = test_func(text)
        print("result=(%s)" % result)
        assert type(result) == str, "Check failed, result is str"
        if type(check) == str:
            assert result == check, "Check failed"
        elif type(check) == list:
            assert result in check, "Check failed"
    print()

