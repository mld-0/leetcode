#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
import pprint
#   {{{2
class Solution:

    #   TODO: 2021-10-29T18:42:27AEDT _leetcode, 72-edit-distance, determine edit operations from DP table
    def trace_minDistance_Table(self, table):
        #   LINK: https://stackoverflow.com/questions/10638597/minimum-edit-distance-reconstruction
        raise NotImplementedError()


    #   runtime: beats 42%
    def minDistance_Iterative(self, word1: str, word2: str) -> int:
        #   one of the input strings is empty: edit distance is length of other string
        if len(word1) == 0 or len(word2) == 0:
            return len(word1) + len(word2)

        #   table[i][j]: edit distance between word1[:i] and word2[:j]
        table = [ [ 0 for col in range(len(word2)+1) ] for row in range(len(word1)+1) ]

        #   initial conditions:
        for row in range(len(table)):
            table[row][0] = row
        for col in range(len(table[0])):
            table[0][col] = col

        for row in range(1, len(table)):
            for col in range(1, len(table[0])):

                left = table[row-1][col] + 1    #   Remove
                down = table[row][col-1] + 1    #   Insert
                diag = table[row-1][col-1]  
                if word1[row-1] != word2[col-1]:
                    diag = diag + 1             #   Replace

                table[row][col] = min(left, down, diag)

        return table[-1][-1]


    #   runtime: beats 98%
    def minDistance_RecursiveMemorize(self, word1: str, word2: str) -> int:
        memo = dict()

        def solve(m: int=None, n: int=None):
            if (m,n) in memo:
                return memo[(m,n)]

            if m == 0 or n == 0:
                result = m + n
                memo[(m,n)] = result
                return result

            if word1[m-1] == word2[n-1]:
                result = solve(m-1, n-1)
                memo[(m,n)] = result
                return result

            left = solve(m-1, n)     #   Remove
            down = solve(m, n-1)     #   Insert
            diag = solve(m-1, n-1)   #   Replace

            result = 1 + min(left, down, diag)
            memo[(m,n)] = result
            return result

        return solve(len(word1), len(word2))


s = Solution()
test_functions = [ s.minDistance_Iterative, s.minDistance_RecursiveMemorize, ]

input_values = [ ("horse", "ros"), ("intention", "execution"), ]
input_checks = [ 3, 5, ]

for test_func in test_functions:
    print(test_func.__name__)
    for (word1, word2), check in zip(input_values, input_checks):
        print("word1=(%s), word2=(%s)" % (word1, word2))
        result = test_func(word1, word2)
        print("result=(%s)" % result)
        assert result == check, "Check comparison failed"
    print()

