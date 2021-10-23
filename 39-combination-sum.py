#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
from typing import List
#   {{{2
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.combinationSum_Backtrack(candidates, target)


    #   runtime: beats 35%
    def combinationSum_Backtrack(self, candidates, target):
        """Return list of unique combinations of 'candidates' that sum to 'target', with replacement"""
        result = []

        def backtrack(combination, start):
            if sum(combination) == target:
                result.append(combination[:])
                return
            elif sum(combination) > target:
                return
            for i in range(start, len(candidates)):
                combination.append(candidates[i])
                backtrack(combination, i)
                combination.pop()

        backtrack([], 0)
        return result
            

s = Solution()

input_values = [ ([2,3,6,7], 7), ([2,3,5], 8), ([2], 1), ([1], 1), ([1], 2), ]
input_checks = [ [[2,2,3],[7]], [[2,2,2,2],[2,3,3],[3,5]], [], [[1]], [[1,1]], ]

for (candidates, target), check in zip(input_values, input_checks):
    print("candidates=(%s), target=(%s)" % (candidates, target))
    result = s.combinationSum(candidates, target)
    print("result=(%s)" % result)
    assert sorted(result) == sorted(check), "Check failed"
    print()

