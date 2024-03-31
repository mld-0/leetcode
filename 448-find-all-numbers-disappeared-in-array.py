#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
import copy
from typing import List, Optional

class Solution:
    """Given a list of `n` non-unique numbers in the range [1,n], determine which numbers do not appear, (ideally in O(n) time using no extra space other than the result)"""

    #   runtime: beats 96%
    #    memory: beats 20%
    def findDisappearedNumbers_Set(self, nums: List[int]) -> List[int]:
        lowest = 1
        highest = len(nums)
        unique_nums = set(nums)
        result = []
        for i in range(lowest, highest+1):
            if i not in unique_nums:
                result.append(i)
        return result


    #   runtime: beats 59% 
    #    memory: beats 93%
    def findDisappearedNumbers_SetNegative(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -1 * abs(nums[index])

        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i+1)
        return result


    #   runtime: beats 60%
    #    memory: beats 93%
    def findDisappearedNumbers_ans_SwapElements(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

        result = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                result.append(i+1)
        return result


s = Solution()
test_functions = [ s.findDisappearedNumbers_Set, s.findDisappearedNumbers_ConstSpace, s.findDisappearedNumbers_ans_SwapElements, ]

inputs = [ [4,3,2,7,8,2,3,1], [1,1], [5,4,6,7,9,3,10,9,5,6], ]
checks = [ [5,6], [2], [1,2,8], ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for nums, check in zip(inputs, checks):
        print(f"nums=({nums})")
        result = f(nums[:])
        print(f"result=({result})")
        assert sorted(result) == sorted(check), "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

