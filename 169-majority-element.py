import time
from typing import List, Optional

class Solution:
    """Determine which element in `nums` occurs at least `len(nums)/2` times in O(n) time and O(1) space"""

    #   runtime: beats 94%
    def majorityElement(self, nums: List[int]) -> int:
        current = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == current:
                count += 1
            else:
                count -= 1
            if count <= 0:
                current = nums[i]
                count = 1
        return current


s = Solution()
test_functions = [ s.majorityElement, ]

inputs = [ [3,2,3], [2,2,1,1,1,2,2], [3,3,4], [1,3,1,1,4,1,1,5,1,1,6,2,2], ]
checks = [ 3, 2, 3, 1, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for vals, check in zip(inputs, checks):
        print(f"vals=({vals})")
        result = f(vals)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

