#   VIM SETTINGS: {{{3
        #   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
import math
from typing import List
#   {{{2

class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.findMin_B(nums)
        #return self.findMin_bsearch(nums)


    #   runtime: beats 20%
    def findMin_bsearch(self, nums: List[int]) -> int:
        """Binary search for index about which the list has been rotated (index of min element in rotated sorted list)"""
        l = 0
        r = len(nums) - 1
        if len(nums) == 1:
            return nums[0]
        if nums[l] < nums[r]:
            return nums[l]
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            if nums[l] < nums[mid]:
                l = mid + 1
            else:
                r = mid - 1


    #       runtime: beats 98%
    def findMin_B(self, nums: list[int]) -> int:
        """Binary search for min value in a rotated sorted list"""
        if len(nums) == 1:
            return nums[0]
        l = 0
        r = len(nums)
        mid = (r - l + 1) // 2 + l
        while (nums[mid] > nums[mid-1]):
            if (nums[l] > nums[mid]):
                r = mid
            else:
                l = mid
            mid = (r - l + 1) // 2 + l
            while mid >= len(nums):
                mid -= len(nums) 
        return nums[mid]


s = Solution()

input_values = [ [3,4,5,1,2], [4,5,6,7,0,1,2], [11,13,15,17], [1,2], [2,3,4,5,6,1], [284,287,289,293,295,298,0,3,8,9,10,11,12,15,17,19,20,22,26,29,30,31,35,36,37,38,42,43,45,50,51,54,56,58,59,60,62,63,68,70,73,74,81,83,84,87,92,95,99,101,102,105,108,109,112,114,115,116,122,125,126,127,129,132,134,136,137,138,139,147,149,152,153,154,155,159,160,161,163,164,165,166,168,169,171,172,174,176,177,180,187,188,190,191,192,198,200,203,204,206,207,209,210,212,214,216,221,224,227,228,229,230,233,235,237,241,242,243,244,246,248,252,253,255,257,259,260,261,262,265,266,268,269,270,271,272,273,277,279,281], [1], ]
input_checks = [ min(x) for x in input_values ]

for nums, check in zip(input_values, input_checks):
    print("nums=(%s)" % nums)
    result = s.findMin(nums)
    print("result=(%s)" % result)
    assert result == check, "Check failed"
    print()

