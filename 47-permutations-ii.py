#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
from typing import List
import itertools
from collections import Counter
import time
#   {{{2
def is_sortable(obj):
    cls = obj.__class__
    return cls.__lt__ != object.__lt__ or cls.__gt__ != object.__gt__

class Solution:

    #   runtime: beats 97%
    def permuteUnique_BacktrackCounter(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(counter, combination):
            if len(combination) == len(nums):
                result.append(combination[:])
                return
            for n in counter:
                if counter[n] > 0:
                    combination.append(n)
                    counter[n] -= 1
                    backtrack(counter, combination)
                    combination.pop()
                    counter[n] += 1

        backtrack(Counter(nums), [])
        return result
    

    #   runtime: beats 5%
    def permute_i_Unique_Backtracking(self, nums: List[int]) -> List[List[int]]:
        result = []

        def permute(index=0):
            if index == len(nums):
                if nums not in result:
                    result.append(nums[:])
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                permute(index+1)
                nums[index], nums[i] = nums[i], nums[index]

        permute()
        return result


    #   runtime: beats 8%
    def permute_i_Unique_Recursive(self, nums: List[int]) -> List[List[int]]:
        result = []

        def permute(remaining, combination):
            if len(remaining) == 0:
                if combination not in result:
                    result.append(combination)
                return
            for i in range(len(remaining)):
                new_remaining = remaining[:i] + remaining[i+1:]
                new_combination = combination + [ remaining[i] ]
                permute(new_remaining, new_combination)

        permute(nums, [])
        return result
         

    #   runtime: beats 8%
    def permute_i_Unique_Itertools(self, nums: List[int]) -> List[List[int]]:
        result = []
        for x in itertools.permutations(nums):
            x = list(x)
            if x not in result:
                result.append(x)
        return result


s = Solution()

test_functions = [ s.permuteUnique_BacktrackCounter, s.permute_i_Unique_Backtracking, s.permute_i_Unique_Recursive, s.permute_i_Unique_Itertools, ]

input_values = [ [1,1,2], [1,2,3], ]
input_checks = [ [[1,1,2],[1,2,1],[2,1,1]], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]], ]
assert len(input_values) == len(input_checks)

for f in test_functions:
    print(f.__name__)
    startTime = time.time()
    for nums, check in zip(input_values, input_checks):
        print("nums=(%s)" % nums)
        result = f(nums)
        print("result=(%s)" % result)
        assert is_sortable(result), "Check failed is_sortable"
        assert sorted(result) == sorted(check), "Check failed"
    print("elapsed_ms=(%0.2f)" % ((time.time() - startTime) * 1000000))
    print()


