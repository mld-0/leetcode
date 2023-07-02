#   vim-modelines: {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
import copy
import math
from typing import List

class Solution:

    #   runtime: beats 5%
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 0
        result = 0

        while r <= len(nums) - 1:
            #   l points to start of next number
            #   move r to end of current number
            r = l
            while r < len(nums) - 1 and nums[r+1] == nums[l]:
                r += 1
            count = r - l + 1
            if count > 2:
                i = 0
                while r + i + 1 < len(nums):
                    nums[l+2+i] = nums[r+i+1]
                    i += 1
                while l + 2 + i < len(nums):
                    nums[l+2+i] = -math.inf
                    i += 1
                l = l + 2
                result += 2
            else:
                l = r + 1
                result += count
            if r == len(nums) - 1:
                break
            if nums[l] == -math.inf:
                break

        return result


    def removeDuplicates_ii(self, nums: List[int]) -> int:
        raise NotImplementedError()



def validate_result(nums, result_len, check_len, check):
    if result_len != check_len:
        return False
    for i in range(check_len):
        if nums[i] != check[i]:
            return False
    return True

s = Solution()
test_functions = [ s.removeDuplicates, s.removeDuplicates_ii, ]

inputs = [ [1,1,1,2,2,3], [0,0,1,1,1,1,2,3,3], [1,1,1,1,1,1,2,2,2,3,3,4], [1], [1,1,1], [1,1,1,2], ]
checks = [ (5,[1,1,2,2,3]), (7,[0,0,1,1,2,3,3]), (7,[1,1,2,2,3,3,4]), (1,[1]), (2,[1,1]), (3,[1,1,2]), ]
assert len(inputs) == len(checks)

for f in test_functions:
    print(f.__name__)
    inputs_copy = copy.deepcopy(inputs)
    startTime = time.time()
    for nums, (check_len, check) in zip(inputs_copy, checks):
        print(f"nums=({nums})")
        result_len = f(nums)
        print(f"len=({result_len}), result=({nums})")
        assert validate_result(nums, result_len, check_len, check), "Check comparison failed"        
    print("elapsed_ms=(%0.2f)" % ((time.time() - startTime) * 1000000))
    print()

