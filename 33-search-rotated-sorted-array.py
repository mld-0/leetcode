from typing import List

class Solution:

    def search(self, nums: List[int], target: int) -> int:
        #return self.search_twoPass(nums, target)
        return self.search_onePass(nums, target)


    #   runtime: beats 92%
    def search_twoPass(self, nums: List[int], target: int) -> int:
        """Find the index of the given element in a rotated sorted list, or -1 if not found, performing one search to find index about which list has been rotated (minimum element) and then another search on the half containing the target value"""

        def binary_search(nums: List[int], target: int) -> int:
            """Binary search, find the index of a given element in a list, or -1 if not found"""
            l = 0
            r = len(nums)-1
            while l <= r:
                mid = (r + l) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
            return -1

        def find_rotation_index(nums: List[int]) -> int:
            """Binary search for index about which the list has been rotated (index of min element)"""
            l = 0
            r = len(nums)-1
            if nums[l] < nums[r]:
                return 0
            while l <= r:
                mid = (r + l) // 2
                if nums[mid] > nums[mid+1]:
                    return mid + 1
                else:
                    if nums[mid] < nums[l]:
                        r = mid - 1
                    else:
                        l = mid + 1
            return -1

        #   handle single-element case
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        #   get index list has been rotated about (min element)
        rotate_index = find_rotation_index(nums)

        #   if target is at rotate_index
        if nums[rotate_index] == target:
            return rotate_index

        #   if nums is not rotated, search entire list
        if rotate_index == 0:
            return binary_search(nums, target)

        #   search half of list containing target
        if target < nums[0]:
            trial = binary_search(nums[rotate_index:], target) 
            if trial != -1:
                trial = trial + rotate_index
            return trial
        else:
            return binary_search(nums[:rotate_index], target)


    #   TODO: 2021-10-04T11:42:39AEDT _leetcode, 33-search-rotated-sorted-array, intuition for 'search_onePass()' solution
    #   runtime: beats 80%
    def search_onePass(self, nums: List[int], target: int) -> int:
        """Find index of item 'target' in 'nums', or -1 if not found, performing a single binary search"""
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[l] <= nums[mid]:
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[l] > nums[mid]:
                if target <= nums[r] and target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


s = Solution()

input_values = [ ([4,5,6,7,0,1,2], 0), ([4,5,6,7,0,1,2], 3), ([1], 0), ]
input_checks = [ 4, -1, -1 ]

for (nums, target), check in zip(input_values, input_checks):
    print("nums=(%s), target=(%s)" % (nums, target))
    result = s.search(nums, target)
    print("result=(%s)" % result)
    assert result == check, "Check failed"
    print()

