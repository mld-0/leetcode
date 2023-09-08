import time
import copy
from typing import List, Optional

class Solution:
    """Move all 0's to the end of array `nums` in-place (maintaining the order of other elements)"""

    #   runtime: beats 5%
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        r = 0
        while r < len(nums):
            #   move l to next zero
            while l < len(nums) and nums[l] != 0:
                l += 1
            #   move r to next non-zero after l
            r = l + 1
            while r < len(nums) and nums[r] == 0:
                r += 1
            #   break if no more zeros
            if r >= len(nums):
                break
            nums[l], nums[r] = nums[r], nums[l]
            l += 1


    #   runtime: beats 80%
    def moveZeros_extraSpace(self, nums: List[int]) -> None:
        extra_space = [ 0 for _ in nums ]
        i = 0
        for n in nums:
            if n != 0:
                extra_space[i] = n
                i += 1
        nums[:] = extra_space[:]


    #   runtime: beats 95%
    def moveZeroes_ans_i(self, nums: List[int]) -> None:
        r = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[r] = nums[i]
                r += 1
        for i in range(r, len(nums)):
            nums[i] = 0


    #   runtime: beats 98%
    def moveZeroes_ans_ii(self, nums: List[int]) -> None:
        r = 0
        for l in range(len(nums)):
            if nums[l] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                r += 1


s = Solution()
test_functions = [ s.moveZeroes, s.moveZeros_extraSpace, s.moveZeroes_ans_i, s.moveZeroes_ans_ii, ]

n = 20
inputs = [ [0,1,0,3,12], [0], [0,0,1], [1], [1,0], [*[0 for _ in range(n)],1,1,1], ]
checks = [ [1,3,12,0,0], [0], [1,0,0], [1], [1,0], [1,1,1,*[0 for _ in range(n)]], ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for nums, check in zip(inputs, checks):
        nums = copy.deepcopy(nums)
        print(f"nums=({nums})")
        f(nums)
        print(f"result=({nums})")
        assert nums== check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()


