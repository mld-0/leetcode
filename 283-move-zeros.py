import sys
import logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

class Solution:

    #   Problem forbids copying of nums(?)

    def moveZeros(self, nums: list[int]) -> None:
        """Move all '0's to the end of 'nums' (inplace), preserving order of other elements"""
        #self.move_Zeroes_A(nums)
        self.moveZeroes_F(nums)

    #   runtime: beats 6%
    def move_Zeroes_A(self, nums: list[int]) -> None:
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
    def move_Zeroes_B(self, nums: list[int]) -> None:
        result = [ 0 for x in nums ]
        k = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                result[k] = nums[r]
                k += 1
        nums[:] = result[:]


    #   runtime: beats 18%
    def move_Zeroes_C(self, nums: list[int]) -> None:
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
    def move_Zeroes_D(self, nums: list[int]) -> None:
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
    def move_Zeroes_E(self, nums: list[int]) -> None:
        snowBall = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                snowBall += 1
            elif snowBall > 0:
                temp = nums[i]
                nums[i] = 0
                nums[i-snowBall] = temp


    #   runtime: beats 60%
    def moveZeroes_F(self, nums: list[int]) -> None:
        """Two pointers approach, at each stage, move the next non-zero value, 'p_current', with the end of the list of non-zero values, 'p_firstZero'"""

        p_firstZero = 0
        p_current = 0

        while p_current < len(nums):
            if nums[p_current] != 0:
                nums[p_current], nums[p_firstZero] = nums[p_firstZero], nums[p_current]
                p_firstZero += 1
            p_current += 1



s = Solution()

input_values = [ [0,1,0,3,12], [0], [0,0,1] ]
input_checks = [ [1,3,12,0,0], [0], [1,0,0] ]

for nums, check in zip(input_values, input_checks):
    s.moveZeros(nums)
    print("nums=(%s)" % str(nums))
    assert( nums == check )
    print()

