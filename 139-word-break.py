#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
from typing import List
from collections import deque
#   Problem: determine whether a given string, 's', can be divided into words from a given list 'wordDict'
#   {{{2
class Solution:

    #   runtime: beats 96%
    def wordBreak_RecursiveMemorize(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        memo = dict()

        def wordbreak_solve(l: int):
            """Is substring of 's' beginning at 'l' comprised only of words in 'wordDict'"""
            if l in memo:
                return memo[l]
            #   base case: 'l' is beyond end of 's'
            if l == len(s):
                memo[l] = True
                return True
            for r in range(l, len(s)):
                if s[l:r+1] in wordDict:
                    if wordbreak_solve(r+1):
                        memo[l] = True
                        return True
            memo[l] = False
            return False

        return wordbreak_solve(0)


    #   runtime: beats 96%
    def wordBreak_DFS(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        queue = deque()
        visited = set()

        queue.append(0)
        while len(queue) > 0:
            l = queue.popleft()
            if l in visited:
                continue
            for r in range(l, len(s)):
                if s[l:r+1] in wordDict:
                    queue.append(r+1)
                    if r == len(s)-1:
                        return True
            visited.add(l)

        return False


    #   runtime: beats 96%
    def wordBreak_DP_Iterative(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        #   table[i]: True if 's[:i+1]' can be comprised of strings from 'wordDict' 
        table = [ False for x in range(len(s)+1) ]
        table[0] = True

        for r in range(0, len(s)):
            for l in range(r+1):
                if table[l] == True and s[l:r+1] in wordDict:
                    table[r+1] = True
                    break

        print(table)
        return table[len(s)]


s = Solution()
test_functions = [ s.wordBreak_RecursiveMemorize, s.wordBreak_DFS, s.wordBreak_DP_Iterative, ]

input_values = [ ("leetcode", ["leet", "code"]), ("applepenapple", ["apple", "pen"]), ("catsandog", ["cats", "dog", "sand", "and", "cat"]), ("a", ["a"]), ]
input_checks = [ True, True, False, True, ]

for test_func in test_functions:
    print(test_func.__name__)
    for (text, words), check in zip(input_values, input_checks):
        print("text=(%s), words=(%s)" % (text, words))
        result = test_func(text, words)
        print("result=(%s)" % result)
        assert result == check, "Check comparison failed"
    print()

