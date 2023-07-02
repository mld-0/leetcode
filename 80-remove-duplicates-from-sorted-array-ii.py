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
    def removeDuplicates_shuffle_i(self, nums: List[int]) -> int:
        l = 0       #   index of first current number
        r = 0       #   index of last current number
        result = 0

        while r <= len(nums) - 1:
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


    #   runtime: beats 98%
    def removeDuplicates_ans_pop(self, nums: List[int]) -> int:
        i = 1
        count = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                count += 1
                if count > 2:
                    nums.pop(i)
                    i -= 1
            else:
                count = 1
            i += 1
        return len(nums)


    #   runtime: beats 94%
    def removeDuplicates_ans_twoPointers_overwrite(self, nums: List[int]) -> int:
        k = 2
        l = 1
        r = 1
        count = 1
        while r < len(nums):
            if nums[r] == nums[r-1]:
                count += 1
            else:
                count = 1
            if count <= k:
                nums[l] = nums[r]
                l += 1
            r += 1
        return l


    #   runtime: beats 97%
    def removeDuplicates_ans_simple(self, nums: List[int]) -> int:
        k = 2
        i = 0
        for x in nums:
            if i < k or x > nums[i-k]:
                nums[i] = x
                i += 1
        return i



def validate_result(nums, result_len, check_len, check):
    if result_len != check_len:
        return False
    for i in range(check_len):
        if nums[i] != check[i]:
            return False
    return True

s = Solution()
test_functions = [ s.removeDuplicates_shuffle_i, s.removeDuplicates_ans_pop, s.removeDuplicates_ans_twoPointers_overwrite, s.removeDuplicates_ans_simple, ]

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

