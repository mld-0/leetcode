#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
from typing import List
#   {{{2
#   Insight: result is max of HouseRobberI for values[0:n-1] and values[1:n]
class Solution:

    #   runtime: beats 76%
    def rob_DP_TopDown_RecursiveMemorize(self, values: List[int]) -> int:
        """Recursive solution from '198-house-robber-i', solve for first and last house missing, and return the greater"""

        def rob_solve(values, i):
            #   no more houses
            if i >= len(values):
                return 0

            #   use memorized solution
            if i in maxRobbedAmount:
                return maxRobbedAmount[i]

            #   skip current house
            trial_skip = rob_solve(values, i+1)
            #   rob current house
            trial_rob = rob_solve(values, i+2) + values[i]

            maxRobbedAmount[i] = max(trial_skip, trial_rob)
            return maxRobbedAmount[i]

        if len(values) == 1:
            return values[0]
        maxRobbedAmount = dict()
        trial_skipLast = rob_solve(values[:-1], 0)
        maxRobbedAmount = dict()
        trial_skipFirst = rob_solve(values[1:], 0)
        return max(trial_skipFirst, trial_skipLast)


    #   runtime: beats 98%
    def rob_DP_BottomUp_Iterative(self, values: List[int]) -> int:
        """Iterative solution from '198-house-robber-i', solve for first and last house missing, and return the greater"""

        def rob_solve(values):
            maxRobbedAmount = dict()

            maxRobbedAmount[len(values)] = 0
            maxRobbedAmount[len(values)-1] = values[len(values)-1]

            for i in range(len(values)-2, -1, -1):
                trial_skip = maxRobbedAmount[i+1]
                trial_rob = maxRobbedAmount[i+2] + values[i]

                maxRobbedAmount[i] = max(trial_skip, trial_rob)

            return maxRobbedAmount[0]

        if len(values) == 1:
            return values[0]
        maxRobbedAmount = dict()
        trial_skipLast = rob_solve(values[:-1])
        maxRobbedAmount = dict()
        trial_skipFirst = rob_solve(values[1:])
        return max(trial_skipFirst, trial_skipLast)


s = Solution()
test_functions = [ s.rob_DP_TopDown_RecursiveMemorize, s.rob_DP_BottomUp_Iterative, ]

input_values = [ [2,3,2], [1,2,3,1], [1,2,3], [1], ]
input_checks = [ 3, 4, 3, 1, ]

for test_func in test_functions:
    print(test_func.__name__)
    for values, check in zip(input_values, input_checks):
        print("values=(%s)" % values)
        result = test_func(values)
        print("result=(%s)" % result)
        assert result == check, "Check failed"
    print()

