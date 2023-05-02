import copy
import time
from collections import Counter
from typing import List

class Solution:

    #   runtime: beats 62%
    def sortColors_Counting(self, nums: List[int]) -> None:
        counts = Counter(nums)
        if not 0 in counts.keys():
            counts[0] = 0
        if not 1 in counts.keys():
            counts[1] = 0
        if not 2 in counts.keys():
            counts[2] = 0
        i = 0
        for _ in range(counts[0]):
            nums[i] = 0
            i += 1
        for _ in range(counts[1]):
            nums[i] = 1
            i += 1
        for _ in range(counts[2]):
            nums[i] = 2
            i += 1

    #   runtime: beats 62%
    def sortColors_ans_TwoPointers(self, nums: List[int]) -> None:
        i = 0
        l = 0
        r = len(nums) - 1
        while i <= r:
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1


s = Solution()
test_functions = [ s.sortColors_Counting, s.sortColors_ans_TwoPointers, ]

inputs = [ [2,0,2,1,1,0], [2,0,1], ]
checks = [ [0,0,1,1,2,2], [0,1,2], ]
assert len(inputs) == len(checks)

for f in test_functions:
    inputs_copy = copy.deepcopy(inputs)
    print(f.__name__)
    startTime = time.time()
    for nums, check in zip(inputs_copy, checks):
        print(f"nums=({nums})")
        f(nums)
        print(f"result=({nums})")
        assert nums == check, "Check comparison failed"
    print("elapsed_ms=(%0.2f)" % ((time.time() - startTime) * 1000000))
    print()
