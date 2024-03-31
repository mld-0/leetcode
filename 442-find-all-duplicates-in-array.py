#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
import math
from typing import List, Optional

class Solution:
    """Given an unsorted list of numbers in the range [1,n] of length n, where each value occurs either zero, one, or two times, return a list of the numbers which appear twice, in O(n) time and O(1) space"""

    #   runtime: beats 82%
    #    memory: beats 59%
    def findDuplicates_SetNegative(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            current = nums[index]
            if current < 0:
                result.append(index+1)
            else:
                nums[index] = -1 * current
        return result


s = Solution()
test_functions = [ s.findDuplicates_SetNegative, ]

inputs = [ [4,3,2,7,8,2,3,1], [1,1,2], [1], [10,2,5,10,9,1,1,4,3,7], ]
checks = [ [2,3], [1], [], [10,1], ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for nums, check in zip(inputs, checks):
        print(f"nums=({nums})")
        result = f(nums[:])
        print(f"result=({result})")
        assert sorted(result) == sorted(check), "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

