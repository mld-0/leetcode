import time
import math
from functools import cache

class Solution:
    """Return the length of the longest common subsequence between `text1` and `text2`, that is, the longest matching sequence of letters that can be formed by deleting some or no letters from one or both strings"""

    #   runtime: beats 50%
    def longestCommonSubsequence_DP_BottomUp_Iterative(self, text1: str, text2: str) -> int:

        #   table[i][j]: longest common subsequence between text1[:i] and text2[:j]
        table = [ [ 0 for _ in range(len(text2)+1) ] for _ in range(len(text1)+1) ]

        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    table[i][j] = table[i-1][j-1] + 1
                else:
                    table[i][j] = max(table[i-1][j], table[i][j-1])

        return table[-1][-1]


    #   runtime: beats 18%
    def longestCommonSubsequence_DP_TopDown_RecursiveMemorize(self, text1: str, text2: str) -> int:

        @cache
        def solve(i: int, j: int) -> int:
            if i == 0 or j == 0:
                return 0
            if text1[i-1] == text2[j-1]:
                return solve(i-1, j-1) + 1
            else:
                trial1 = solve(i-1, j)
                trial2 = solve(i, j-1)
                return max(trial1, trial2)

        return solve(len(text1), len(text2))


    #   runtime: beats 96%
    def longestCommonSubsequence_ans(self, text1: str, text2: str) -> int:
        if len(text1) > len(text2):
            text1, text2 = text2, text1
        previous = [ 0 for _ in range(len(text1)+1) ]
        for j in reversed(range(len(text2))):
            current = [ 0 for _ in range(len(text1)+1) ]
            for i in reversed(range(len(text1))):
                if text2[j] == text1[i]:
                    current[i] = 1 + previous[i+1]
                else:
                    current[i] = max(previous[i], current[i+1])
            previous = current
        return previous[0]


s = Solution()
test_functions = [ s.longestCommonSubsequence_DP_BottomUp_Iterative, s.longestCommonSubsequence_DP_TopDown_RecursiveMemorize, s.longestCommonSubsequence_ans, ]

inputs = [ ("abcde", "ace"), ("abc", "abc"), ("abc", "def"), ("bsbininm","jmjkbkjkv"), ]
checks = [ 3, 3, 0, 1, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    startTime = time.time()
    for (text1, text2), check in zip(inputs, checks):
        print("text1=(%s), text2=(%s)" % (text1, text2))
        result = f(text1, text2)
        print("result=(%s)" % result)
        assert result == check, "Check comparison failed"
    print("elapsed_ms=(%0.2f)" % ((time.time() - startTime) * 1000000))
    print()

