import time
from typing import List, Optional

class Solution:

    #   runtime: beats 95%
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        leftmost = -1
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] == target:
                if mid > 0 and nums[mid-1] == target:
                    r = mid - 1
                else:
                    leftmost = mid
                    break

        rightmost = -1
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] == target:
                if mid < len(nums) - 1 and nums[mid+1] == target:
                    l = mid + 1
                else:
                    rightmost = mid
                    break

        return [ leftmost, rightmost ]


s = Solution()
test_functions = [ s.searchRange, ]

inputs = [ ([5,7,7,8,8,10], 8), ([5,7,7,8,8,10], 6), ([], 0), ([1,2,3,3,3,4], 3), ([1], 1), ([1,1,2], 1), ]
checks = [ [3,4], [-1,-1], [-1,-1], [2,4], [0,0], [0,1], ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for (nums, target), check in zip(inputs, checks):
        print(f"nums=({nums}), target=({target})")
        result = f(nums,target)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

