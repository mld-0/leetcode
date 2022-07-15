from typing import List

#   Problem: remove all occurences of 'val' in 'nums', in-place, returning the number of elements remaining, 'k'. The order of elements may be changed. Only use O(1) extra memory.

#   Continue: 2022-07-14T21:39:41AEST leetcode, 27-remove-element, two-pointers problem

class Solution:
    
    #   runtime: beats 98%
    def removeElement_naive(self, nums: List[int], val: int) -> int:
        l = 0
        while l < len(nums):
            if nums[l] == val:
                nums.pop(l)
                l -= 1
            l += 1
        return len(nums)


    #   runtime: beats 53%
    def removeElement_twoPointers(self, nums: List[int], val: int) -> int:
        l = 0
        r = len(nums) - 1
        while r >= 0 and nums[r] == val:
            r -= 1
        while l <= r:
            while r >= 0 and nums[r] == val:
                r -= 1
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            else:
                l += 1
        return l


    #   runtime: beats 58%
    def removeElement_twoPointers_ii(self, nums: List[int], val: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            else:
                l += 1
        return l


    #   runtime: beats 75%
    def removeElements_Ans_twoPointers(self, nums: List[int], val: int) -> int:
        l = 0
        for r in range(len(nums)):
            if nums[r] != val:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return l



def validate_result(nums: List[int], k: int, expectedNums: List[int]):
    nums[0:k] = sorted(nums[0:k])
    expectedNums[0:k] = sorted(expectedNums[0:k])
    for i in range(k):
        assert nums[i] == expectedNums[i], "Check comparison failed (nums)"


s = Solution()
test_functions = [ s.removeElement_naive, s.removeElement_twoPointers, s.removeElement_twoPointers_ii, s.removeElements_Ans_twoPointers, ]

input_values = [ ([3,2,2,3], 3), ([0,1,2,2,3,0,4,2], 2), ([1], 1), ([3,3], 3), ([4,5], 4), ([2], 3), ([2,2,3], 2), ]
check_values = [ (2, [2,2,None,None]), (5, [0,1,4,0,3,None,None,None]), (0, [None]), (0, [None,None]), (1, [5,None]), (1, [2]), (1, [3,None]), ]
assert len(input_values) == len(check_values), "input/check len mismatch"

for test_func in test_functions:
    print(test_func.__name__)
    for (nums, val), (expectedK, expectedNums) in zip(input_values, check_values):
        nums = nums[:]
        expectedNums[:] = expectedNums
        print("nums=(%s), val=(%s)" % (nums, val))
        k = test_func(nums, val)
        print("result=(%s), k=(%s)" % (nums, k))
        assert k == expectedK, "Check comparison failed (k)"
        validate_result(nums, k, expectedNums)
    print()

