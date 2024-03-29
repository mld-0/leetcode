import time
import copy
from typing import List

class Solution:
    """Move all '0's to the end of 'nums' (in-place), preserving order of other elements"""

    #   runtime: beats 6%
    def move_Zeroes_A(self, nums: List[int]) -> None:
        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l] == 0:
                #   shuffle each element between [l, end] forward one position, and move element 'l' to end of list
                for j in range(l+1, len(nums)):
                    nums[j-1] = nums[j]
                nums[-1] = 0
                r -= 1
            else:
                l += 1

    #   runtime: beats 30%
    def move_Zeroes_B(self, nums: List[int]) -> None:
        result = [ 0 for x in nums ]
        k = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                result[k] = nums[r]
                k += 1
        nums[:] = result[:]


    #   runtime: beats 18%
    def move_Zeroes_C(self, nums: List[int]) -> None:
        #   Invariants:
        #       all elements before l are non-zeros
        #       all elements between r and l are zeros
        l = 0
        r = 0
        while r < len(nums):
            if nums[r] != 0:
                nums[r], nums[l] = nums[l], nums[r]
                l += 1
            r += 1

    #   runtime: beats 16%
    def move_Zeroes_D(self, nums: List[int]) -> None:
        l = 0
        r = 0
        while r < len(nums):
            if nums[r] != 0:
                nums[l] = nums[r]
                l += 1
            r += 1
        r = l
        while r < len(nums):
            nums[r] = 0
            r += 1

    #   runtime: beats 24%
    def move_Zeroes_E(self, nums: List[int]) -> None:
        snowBall = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                snowBall += 1
            elif snowBall > 0:
                temp = nums[i]
                nums[i] = 0
                nums[i-snowBall] = temp


    #   runtime: beats 60%
    def moveZeroes_F(self, nums: List[int]) -> None:
        """Two pointers approach, at each stage, move the next non-zero value, 'p_current', with the end of the list of non-zero values, 'p_firstZero'"""
        p_firstZero = 0
        p_current = 0
        while p_current < len(nums):
            if nums[p_current] != 0:
                nums[p_current], nums[p_firstZero] = nums[p_firstZero], nums[p_current]
                p_firstZero += 1
            p_current += 1



s = Solution()
test_functions = [ s.move_Zeroes_A, s.move_Zeroes_B, s.move_Zeroes_C, s.move_Zeroes_D, s.move_Zeroes_E, s.moveZeroes_F, ]

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
        assert nums == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

