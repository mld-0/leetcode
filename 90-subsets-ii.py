#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
import itertools
from typing import List
#   {{{2
#   TODO: 2021-10-19T21:18:26AEDT _leetcode, 90-subsets-ii, review/implement ans
#   TODO: 2021-10-19T21:26:24AEDT _leetcode, 90-subsets-ii, why subsets_i_Backtracking fails when 'nums' is not sorted?

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #return self.subsets_i_Cascading_ii(nums)
        return self.subsets_i_Backtracking(nums)


    #   runtime: beats 47%
    def subsets_i_Cascading_ii(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for n in nums:
            for i in range(len(result)):
                temp = result[i] + [n]
                temp.sort()
                if temp not in result:
                    result.append(temp)
        return result


    #   runtime: beats 47%
    def subsets_i_Backtracking(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        def backtrack(k, first=0, curr=None):
            if curr is None: 
                curr = []
            if len(curr) == k:
                curr.sort()
                if curr[:] not in result:
                    result.append(curr[:])
                return
            for i in range(first, len(nums)):
                curr.append(nums[i])
                backtrack(k, i+1, curr)
                curr.pop()
        for k in range(len(nums)+1):
            backtrack(k)
        return result


    #   runtime: beats 63%
    def subsets_i_Bitmask(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(2**len(nums), 2**(len(nums)+1)):
            bitmask = bin(i)[3:]
            trial = [ nums[j] for j in range(len(nums)) if bitmask[j] == '1' ] 
            trial.sort()
            if trial not in result:
                result.append(trial)
        return result
    

s = Solution()

input_values = [ [1,2,3], [0], [1,2,2], [4,1,0], ]
input_checks = [ [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]], [[],[0]], [[],[1],[1,2],[1,2,2],[2],[2,2]], [[],[0],[0,1],[0,1,4],[0,4],[1],[1,4],[4]], ]

for nums, check in zip(input_values, input_checks):
    print("nums=(%s)" % nums)
    result = s.subsets(nums)
    print("result=(%s)" % result)
    assert sorted(result) == sorted(check), "Check failed"
    print()

