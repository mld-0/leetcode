from typing import List

#   Problem: Given integer array 'nums' sorted low->high, remove duplicates in-place, keeping order of list the same, returning the number of elements, k, once duplicates have been removed. Only use O(1) extra memory.

class Solution:

    #   Ongoing: 2022-07-13T23:11:17AEST Problem specifies we are only to use 'O(1)' extra memory, Is a set 'O(1) extra memory'? [...] Between [O(1), O(n)], avg: O(log(n))? 
    #   Runtime: beats 85%
    def removeDuplicates_naive(self, nums: List[int]) -> int:
        nums_set = sorted(set(nums))
        for i, x in enumerate(nums_set):
            nums[i] = x
        for i in range(len(nums_set), len(nums)):
            nums[i] = None
        return len(nums_set)


    #   Runtime: beats 87%
    def removeDuplicates_twoPointers(self, nums: List[int]) -> int:
        #   position of largest unique value
        l = 0
        #   position in the list
        r = 1

        #   Until we reach end of the list
        while r < len(nums):
            #   Current number is larger than largest unique number
            if nums[r] > nums[l]:
                #   Add it as the next unique number 
                nums[l+1] = nums[r]
                l += 1
            r += 1

        #   Set remaining values to None
        #for i in range(l+1, len(nums)):
        #    nums[i] = None

        #   Unique values are given by nums[:l+1]
        return l+1



def validate_result(nums: List[int], expectedNums: List[int], k: int):
    assert k == len(expectedNums), "Check comparison failed"
    for i in range(k):
        assert nums[i] == expectedNums[i], "Check comparison failed"


s = Solution()
test_functions = [ s.removeDuplicates_naive, s.removeDuplicates_twoPointers, ]

input_values = [ [1,1,2], [0,0,1,1,1,2,2,3,3,4], [-1,0,0,0,0,3,3], ]
check_values = [ (2, [1,2]), (5, [0,1,2,3,4]), (3, [-1,0,3]), ]

assert len(input_values) == len(check_values), "input/check Mismatch"


for f in test_functions:
    print(f.__name__)
    for nums, (expectedK, expectedNums) in zip(input_values, check_values):
        nums = nums[:]
        print("nums=(%s)" % nums)
        k = f(nums)
        print("nums=(%s), k=(%s)" % (nums, k))
        assert k == expectedK, "Check comparison failed"
        validate_result(nums, expectedNums, k)
    print()

