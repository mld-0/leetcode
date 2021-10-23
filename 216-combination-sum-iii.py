#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
from typing import List
import itertools
#   {{{2
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """Find all valid combinations of digits in range [0,9] that contain k numbers and sum to n"""
        return self.combinationSum3_Itertools(k, n)
        #return self.combinationSum3_i(k, n)


    #   runtime: beats 92%
    def combinationSum3_Itertools(self, k: int, n: int) -> List[List[int]]:
        values = [ x for x in range(1,10) ]
        result = [ list(x) for x in itertools.combinations(values, k) if sum(x) == n ]
        return result
        

    #   runtime: beats 80%
    def combinationSum3_Backtrack(self, k: int, n: int) -> List[List[int]]:
        values = [ x for x in range(1,10) ]
        result = []

        def backtrack(combination, start):
            if sum(combination) > n:
                return
            if len(combination) == k:
                if sum(combination) == n:
                    result.append(combination[:])
                return
            for i in range(start, len(values)+1):
                combination.append(i)
                backtrack(combination, i+1)
                combination.pop()

        backtrack([], 1)
        return result


s = Solution()
test_functions = [ s.combinationSum3_Itertools, s.combinationSum3_Backtrack, ]

input_values = [ (3,7), (3,9), (4,1), (3,2), (9,45), ]
input_checks = [ [[1,2,4]], [[1,2,6],[1,3,5],[2,3,4]], [], [], [[1,2,3,4,5,6,7,8,9]], ]

for test_func in test_functions:
    print(test_func.__name__)
    for (k, n), check in zip(input_values, input_checks):
        print("k=(%s), n=(%s)" % (k, n))
        result = test_func(k, n)
        print("result=(%s)" % str(result))
        assert sorted(result) == sorted(check), "Check failed"
    print()

