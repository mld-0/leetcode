#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
import math
#   Problem: Number of unique paths from top-left to bottom-right in an m x n grid, where movement is limited to rightward and downward
#   {{{2
class Solution:

    #   runtime: TLE
    def uniquePaths_Recursive(self, m: int, n: int) -> int:
        """Number of unique paths through m x n grid, recursive solution"""
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths_Recursive(m-1, n) + self.uniquePaths_Recursive(m, n-1)


    #   runtime: TLE
    def uniquePaths_RecursiveMemorized(self, m: int, n: int) -> int:
        """Number of unique paths through m x n grid, as per recursive solution, using memoization"""
        memo = dict()

        def solve(m: int, n: int) -> int:
            if (m,n) in memo:
                return memo[(m,n)]
            if m == 1 or n == 1:
                memo[(m,n)] = 1
                return 1
            result = self.uniquePaths_RecursiveMemorized(m-1, n) + self.uniquePaths_RecursiveMemorized(m, n-1)
            memo[(m,n)] = result
            return result

        return solve(m,n)


    #   runtime: beats 98%
    def uniquePaths_DP_BottomUp(self, m: int, n: int) -> int:
        """Number of unique paths through m x n grid, filling table giving number of paths from each cell"""
        #   paths[row][col]: number of unique paths from given cell to bottom-right
        paths = [ [ math.inf for col in range(n) ] for row in range(m) ]

        #   boundry conditions:
        paths[m-1][n-1] = 0
        for row in range(m): paths[row][n-1] = 1
        for col in range(n): paths[m-1][col] = 1

        #   fill table:
        for row in range(m-2, -1, -1):
            for col in range(n-2, -1, -1):
                paths[row][col] = paths[row+1][col] + paths[row][col+1]

        return paths[0][0]
    

    #   runtime: beats 99%
    def uniquePaths_Mathematical(self, m: int, n: int) -> int:
        """Number of unique paths through m x n grid, using binomial coefficenct nCk(h,h+v) where h=m-1 and v=n-1"""
        return math.factorial(m+n-2) // math.factorial(n-1) // math.factorial(m-1)


s = Solution()
test_functions = [ s.uniquePaths_Recursive, s.uniquePaths_RecursiveMemorized, s.uniquePaths_DP_BottomUp, s.uniquePaths_Mathematical, ]

input_values = [ (3,7), (3,2), (7,3), (3,3), ]
input_checks = [ 28, 3, 28, 6, ]

for test_func in test_functions:
    print(test_func.__name__)
    for (m, n), check in zip(input_values, input_checks):
        print("m=(%s), n=(%s)" % (m, n))
        result = test_func(m, n)
        print("result=(%s)" % result)
        assert result == check, "Check failed"
    print()

