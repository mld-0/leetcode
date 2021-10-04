from typing import List

#   TODO: 2021-10-04T15:31:41AEDT _leetcode, 162-find-peak-element, (intuition behind how) bsearch_recursive identifies peak when only making a comparison with the following element, and not the previous (also - how increasing/decreasing sections are identified?) (also looking at/comparing to iterative)

class Solution:

    def findPeakElement(self, nums: List[int]) -> int:
        #return self.findPeakElement_linear(nums)
        #return self.findPeakElement_bsearch_recursive(nums)
        return self.findPeakElement_bsearch_iterative(nums)


    #   runtime: beats 57%
    def findPeakElement_linear(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            strictly_greater = True
            if i-1 > 0 and nums[i] <= nums[i-1]:
                strictly_greater = False
            if i+1 < len(nums) and nums[i] <= nums[i+1]:
                strictly_greater = False
            if strictly_greater is True:
                return i
        return -1


    #   runtime: beats 80%
    def findPeakElement_bsearch_recursive(self, nums: List[int]) -> int:
        def search(l: int, r: int) -> int:
            if l == r:
                return l
            mid = (l + r) // 2
            if nums[mid] > nums[mid+1]:
                return search(l, mid)
            else:
                return search(mid+1, r)
        return search(0, len(nums)-1)


    #   runtime: beats 25%
    def findPeakElement_bsearch_iterative(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid + 1
        return l



s = Solution()

input_values = [ [1,2,3,1], [1,2,1,3,5,6,4], ]
input_checks = [ (2,), (1,5), ]

for nums, check in zip(input_values, input_checks):
    print("nums=(%s)" % nums)
    result = s.findPeakElement(nums)
    print("result=(%s)" % result)
    assert result in check, "Check failed"
    print()

