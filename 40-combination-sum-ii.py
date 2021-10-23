#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
from collections import Counter
from typing import List
#   {{{2
def is_sortable(obj):
    cls = obj.__class__
    return cls.__lt__ != object.__lt__ or cls.__gt__ != object.__gt__

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.combinationSum2_Backtracking(candidates, target)


    #   runtime: beats 36%
    def combinationSum2_BacktrackCounter(self, candidates, target):
        """Return list of unique combinations of 'candidates' that sum to 'target', without replacement, backtracking using counter to handle duplicates"""
        candidates.sort()
        result = []

        def backtrack(combination, start, counter):
            if sum(combination) == target:
                combination.sort()
                result.append(combination[:])
                return
            elif sum(combination) > target:
                return

            for i in range(start, len(counter)):
                candidate, frequency = counter[i]

                if frequency <= 0:
                    continue

                combination.append(candidate)
                counter[i] = (candidate, frequency-1)
                backtrack(combination, i, counter)
                counter[i] = (candidate, frequency)
                combination.pop()

        counter = Counter(candidates)
        counter = [ (c, counter[c]) for c in counter ] 
        print(counter)

        backtrack([], 0, counter)
        return result


    #   runtime: beats 52%
    def combinationSum2_BacktrackingSkipDuplicates(self, candidates: List[int], target: int) -> List[List[int]]:
        """Return list of unique combinations of 'candidates' that sum to 'target', without replacement, backtracking and skiping duplicate values"""
        candidates.sort()
        result = []

        def backtrack(combination, start):
            if sum(combination) == target:
                result.append(combination[:])
                return
            elif sum(combination) > target:
                return

            for next_start in range(start, len(candidates)):
                #   <skip adjacent equal values>
                if next_start > start and candidates[next_start] == candidates[next_start-1]:
                    continue

                combination.append(candidates[next_start])
                backtrack(combination, next_start+1)
                combination.pop()

        backtrack([], 0)
        return result


    #   runtime: TLE
    def combinationSum2_Backtracking(self, candidates: List[int], target: int) -> List[List[int]]:
        """Return list of unique combinations of 'candidates' that sum to 'target', without replacement"""
        result = []

        def backtrack(combination, start):
            if sum(combination) == target:
                combination.sort()
                if combination not in result:
                    result.append(combination[:])
                return
            elif sum(combination) > target:
                return

            for i in range(start, len(candidates)):
                combination.append(candidates[i])
                backtrack(combination, i+1)
                combination.pop()

        backtrack([], 0)
        return result


s = Solution()

test_functions = [ s.combinationSum2_Backtracking, s.combinationSum2_BacktrackCounter, s.combinationSum2_BacktrackingSkipDuplicates, ]

input_values = [ ([10,1,2,7,6,1,5], 8), ([2,5,2,1,2], 5), ([3,1,3,5,1,1], 8), ]
input_checks = [ [[1,1,6],[1,2,5],[1,7],[2,6]], [[1,2,2],[5]], [[1,1,1,5],[1,1,3,3],[3,5]] ]

for test_func in test_functions:
    print(test_func.__name__)
    for (candidates, target), check in zip(input_values, input_checks):
        print("candidates=(%s), target=(%s)" % (candidates, target))
        result = test_func(candidates, target)
        print("result=(%s)" % result)
        assert is_sortable(result), "Check failed, is_sortable"
        assert sorted(result) == sorted(check), "Check failed"
    print()

