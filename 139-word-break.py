#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
from functools import cache
from collections import deque
from typing import List

class Solution:
    """Problem: determine whether string `s` can be constructed from words in `wordDict`"""

    #   runtime: beats 99%
    def wordBreak_DP_TopDown(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)

        @cache
        def solve(l: int):
            """Is substring `s[l:]` comprised only of words in `wordSet`"""
            if l == len(s):
                return True
            for r in range(l, len(s)):
                if s[l:r+1] in wordSet:
                    if solve(r+1):
                        return True
            return False
        
        return solve(0)


    #   runtime: beats 96%
    def wordBreak_DP_BottomUp(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)

        #   table[i]: True if `s[:i+1]` can be comprised of strings from `wordDict` 
        table = [ False for _ in range(len(s)+1) ]

        #   base case: empty string can be created from wordDict
        table[0] = True

        for r in range(len(s)):
            for l in range(r+1):
                if table[l] and s[l:r+1] in wordSet:
                    table[r+1] = True
                    break

        return table[-1]


    #   runtime: beats 98%
    def wordBreak_BFS(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)

        queue = deque()
        visited = set()
        queue.append(0)

        while len(queue) > 0:
            l = queue.popleft()
            if l in visited:
                continue
            for r in range(l, len(s)):
                if s[l:r+1] in wordSet:
                    queue.append(r+1)
                    if r == len(s)-1:
                        return True
            visited.add(l)

        return False


s = Solution()
test_functions = [ s.wordBreak_DP_TopDown, s.wordBreak_DP_BottomUp, s.wordBreak_BFS, ]

inputs = [ ("leetcode",["leet","code"]),("applepenapple",["apple","pen"]),("catsandog",["cats","dog","sand","and","cat"]),("a",["a"]), ("aaaaaaa",["aaaa","aaa"]), ]
checks = [ True, True, False, True, True, ]
assert len(inputs) == len(checks)

for f in test_functions:
    print(f.__name__)
    startTime = time.time()
    for (s, wordDict), check in zip(inputs, checks):
        print(f"s=({s}), wordDict=({wordDict})")
        result = f(s, wordDict)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_ms=(%0.2f)" % ((time.time() - startTime) * 1000000))
    print()

