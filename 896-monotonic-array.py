import time
from typing import List, Optional

class Solution:
    """Determine whether the array `nums` is monotonic (increasing or decreasing) or not"""

    #   runtime: beats 96%
    def isMonotonic(self, nums: List[int]) -> bool:

        def is_increasing(nums: List[int]) -> bool:
            for i in range(1, len(nums)):
                if nums[i-1] > nums[i]:
                    return False
            return True

        def is_decreasing(nums: List[int]) -> bool:
            for i in range(1, len(nums)):
                if nums[i-1] < nums[i]:
                    return False
            return True

        return is_increasing(nums) or is_decreasing(nums)


s = Solution()
test_functions = [ s.isMonotonic, ]

inputs = [ [1,2,2,3], [6,5,4,4], [1,3,2], [1,1,2], ]
checks = [ True, True, False, True, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for nums, check in zip(inputs, checks):
        print(f"nums=({nums})")
        result = f(nums)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

