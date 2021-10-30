#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
from typing import List
import math
#   {{{2
class Solution:

    #   runtime: beats 76%
    def coinChange_DP_TopDown(self, coins: List[int], amount: int) -> int:
        """Determine minimum number of values from 'coins' (with replacement) that sum to 'amount'"""
        memo = dict()

        def solve(remaining):
            if remaining in memo:
                return memo[remaining]

            if remaining < 0:
                memo[remaining] = -1
                return -1
            if remaining == 0:
                memo[remaining] = 0
                return 0

            minimum = math.inf
            for c in coins:
                result = solve(remaining-c)
                if result >= 0 and result < minimum:
                    minimum = 1 + result

            if minimum == math.inf:
                memo[remaining] = -1
                return -1
            else:
                memo[remaining] = minimum
                return minimum

        return solve(amount)

    
    #   runtime: beats 86%
    def coinChange_DP_BottomUp(self, coins: List[int], amount: int) -> int:
        """Determine minimum number of values from 'coins' (with replacement) that sum to 'amount'"""
        #   table[i]: minimum number of coins that sum to amount
        table = [ math.inf for x in range(amount+1) ]
        table[0] = 0

        for c in coins:
            for x in range(c, amount+1):
                table[x] = min(table[x], table[x-c] + 1)

        if table[amount] == math.inf:
            return -1
        else:
            return table[amount]


s = Solution()
test_functions = [ s.coinChange_DP_TopDown, s.coinChange_DP_BottomUp, ]

input_values = [ ([1,2,5], 11), ([2], 3), ([1], 0), ([1], 1), ([1], 2), ]
input_checks = [ 3, -1, 0, 1, 2, ]

for test_func in test_functions:
    print(test_func.__name__)
    for (coins, amount), check in zip(input_values, input_checks):
        print("coins=(%s), amount=(%s)" % (coins, amount))
        result = test_func(coins, amount)
        print("result=(%s)" % result)
        assert result == check, "Check comparison failed"
    print()

