from typing import List

class Solution:

    #   runtime: beats 92%
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def bsearch_find_left(nums: List[int], target: int) -> List[int]:
            """Get index of leftmost instance of 'target' in sorted list 'nums', or -1 if not found"""
            l = 0
            r = len(nums) - 1
            while l <= r:
                mid = (r + l) // 2
                if nums[mid] == target:
                    while mid-1 >= 0 and nums[mid-1] == target:
                        mid = mid - 1
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
            return -1

        def bsearch_find_right(nums: List[int], target: int) -> List[int]:
            """Get index of rightmost instance of 'target' in sorted list 'nums', or -1 if not found"""
            l = 0
            r = len(nums) - 1
            while l <= r:
                mid = (r + l) // 2
                if nums[mid] == target:
                    while mid+1 < len(nums) and nums[mid+1] == target:
                        mid = mid + 1
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
            return -1

        l = bsearch_find_left(nums, target)
        r = bsearch_find_right(nums, target)
        return [l, r]


s = Solution()

input_values = [ ([5,7,7,8,8,10], 8), ([5,7,7,8,8,10], 6), ([], 0), ([1,2,3,3,3,4], 3), ([1], 1), ([1,1,2], 1), ]
input_checks = [ [3,4], [-1,-1], [-1,-1], [2,4], [0,0], [0,1], ]

for (nums, target), check in zip(input_values, input_checks):
    print("nums=(%s), target=(%s)" % (nums, target))
    result = s.searchRange(nums, target)
    print("result=(%s)" % result)
    assert result == check, "Check failed"
    print()

