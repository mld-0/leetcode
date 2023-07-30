#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
import copy
from typing import List

class Solution:

    def nextPermutation_ans(self, nums: List[int]) -> None:
        #   starting from rear, find first decreasing element, nums[l]
        l = len(nums) - 2
        while l >= 0 and nums[l] >= nums[l+1]:
            l -= 1
        #   if we have gone passed the end, the list is sorted decending
        if l < 0:
            nums.reverse()
            return
        #   for r > l, find the smallest nums[r] such that nums[r] > nums[l]
        r = l + 1
        for i in range(l+2, len(nums)):
            if nums[i] > nums[l] and nums[i] < nums[r]:
                r = i
        #   swap elements at l/r
        nums[l], nums[r] = nums[r], nums[l]
        #   reverse list after l
        nums[l+1:] = nums[l+1:][::-1]


s = Solution()
test_nextPermutations = [ s.nextPermutation_ans, ]

inputs = [ [1,5,8,4,7,6,5,3,1], [1,3,2,5,4], [1,3,2,4], [1,2,3], [3,2,1], [2,1,3], [2,3,1], [1,1,5], [1,3,2], [5,1,1], ]
checks = [ [1,5,8,5,1,3,4,6,7], [1,3,4,2,5], [1,3,4,2], [1,3,2], [1,2,3], [2,3,1], [3,1,2], [1,5,1], [2,1,3], [1,1,5], ]
assert len(inputs) == len(checks)

for f in test_nextPermutations:
    print(f.__name__)
    startTime = time.time()
    for nums, check in zip(inputs, checks):
        nums = nums.copy()
        print(f"nums=({nums})")
        f(nums)
        print(f"result=({nums})")
        assert nums == check, "Check comparison failed"
    print("elapsed_ms=(%0.2f)" % ((time.time() - startTime) * 1000000))
    print()

