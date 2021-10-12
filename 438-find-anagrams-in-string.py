#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
from typing import List
from collections import Counter, defaultdict
#   {{{2

class Solution:

    def findAnagrams(self, s: str, p: str) -> List[int]:
        return self.findAnagrams_SlidingWindowCounter_ii(s, p)


    #   runtime: beats 5%
    def findAnagrams_SlidingWindowCounter_i(self, s: str, p: str) -> List[int]:
        """Find start indices of all anagrams of search string 'p' in input string 's', creating new counter for each search window"""
        result = []
        search_counts = Counter(p)
        for i in range(len(s)-len(p)+1):
            window_str = s[i:i+len(p)]
            window_counts = Counter(window_str)
            if window_counts == search_counts:
                result.append(i)
        return result


    #   runtime: beats 85%
    def findAnagrams_SlidingWindowCounter_ii(self, s: str, p: str) -> List[int]:
        """Find start indices of all anagrams of search string 'p' in input string 's', updating counter for each search window"""
        if len(p) > len(s):
            return []

        result = []

        #   count characters in search string
        search_counts = Counter(p)

        #   count characters in first window and compare to 'search_counts'
        window_counts = defaultdict(int)
        for c in s[:len(p)]:
            window_counts[c] += 1
        if window_counts == search_counts:
            result.append(0)

        #   count characters in each subsequent window and compare to 'search_counts'
        for i in range(1, len(s)-len(p)+1):
            c_remove = s[i-1]
            c_add = s[i+len(p)-1]

            #   Add last character of new window to count
            window_counts[c_add] += 1

            #   Remove first character of previous window from count
            window_counts[c_remove] -= 1
            if window_counts[c_remove] == 0: del window_counts[c_remove]

            #   Is current window an anagram of search string?
            if window_counts == search_counts:
                result.append(i)

        return result


    #   runtime: beats 85%
    def findAnagrams_SlidingWindowCounter_iii(self, s: str, p: str) -> List[int]:
        """Find start indices of all anagrams of search string 'p' in input string 's', using list instead of hash to count character"""
        if len(p) > len(s):
            return []

        result = []

        #   count characters in search string
        search_counts = [ 0 ] * 26
        for c in p:
            search_counts[ord(c)-ord('a')] += 1

        #   count characters in first window and compare to 'search_counts'
        window_counts = [ 0 ] * 26
        for c in s[:len(p)]:
            window_counts[ord(c)-ord('a')] += 1
        if window_counts == search_counts:
            result.append(0)

        #   count characters in each subsequent window and compare to 'search_counts'
        for i in range(1, len(s)-len(p)+1):
            c_remove = s[i-1]
            c_add = s[i+len(p)-1]

            #   Add last character of new window to count
            window_counts[ord(c_add)-ord('a')] += 1

            #   Remove first character of previous window from count
            window_counts[ord(c_remove)-ord('a')] -= 1

            #   Is current window an anagram of seach string?
            if window_counts == search_counts:
                result.append(i)

        return result


s = Solution()

input_values = [ ("cbaebabacd", "abc"), ("abab", "ab"), ]
input_checks = [ [0,6], [0,1,2], ]

for (input_s, input_p), check in zip(input_values, input_checks):
    print("input_s=(%s), input_p=(%s)" % (input_s, input_p))
    result = s.findAnagrams(input_s, input_p)
    print("result=(%s)" % result)
    assert result == check, "Check failed"
    print()

