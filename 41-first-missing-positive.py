import time
import copy
from typing import List

class Solution:
    """Using only O(1) space, return the smallest missing positive integer in the input"""

    #   runtime: beats 95%
    def firstMissingPositive_ans_indexAsKey(self, nums: List[int]) -> int:
        if 1 not in nums:
            return 1
        elif len(nums) == 1:
            return 2
        for i in range(len(nums)):
            if nums[i] < 1:
                nums[i] = 1
        for i in range(len(nums)):
            n = abs(nums[i])
            if n < len(nums):
                nums[n] = -1 * abs(nums[n])
            elif n == len(nums):
                nums[0] = -1 * abs(nums[0])
        for i in range(1, len(nums)):
            if nums[i] > 0:
                return i
        if nums[0] > 0:
            return len(nums)
        return len(nums) + 1


s = Solution()
test_functions = [ s.firstMissingPositive_ans_indexAsKey, ]

inputs = [ [1,2,0], [3,4,-1,1], [7,8,9,11,12], [1], [2,1], [1,2,6,3,5,4], ]
checks = [ 3, 2, 1, 2, 3, 7, ]
assert len(inputs) == len(checks)

for f in test_functions:
    print(f.__name__)
    startTime = time.time()
    for nums, check in zip(inputs, checks):
        nums = copy.deepcopy(nums)
        print(f"nums=({nums})")
        result = f(nums)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_ms=(%0.2f)" % ((time.time() - startTime) * 1000000))
    print()

