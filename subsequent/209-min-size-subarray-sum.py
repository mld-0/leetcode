import time
import math
from typing import List

class Solution:

    #   runtime: TLE
    def minSubArrayLen_naive(self, target: int, nums: List[int]) -> int:
        total = sum(nums)
        if target > total:
            return 0
        if target == total:
            return len(nums)

        result = math.inf
        for l in range(len(nums)):
            r = l
            trial = 0
            while r < len(nums) and trial < target:
                trial += nums[r]
                r += 1
            if trial >= target:
                result = min(result, r - l)

        return result

    
    #   runtime: beats 93%
    def minSubArrayLen_ans_slidingWindow(self, target: int, nums: List[int]) -> int:
        total = sum(nums)
        if target > total:
            return 0
        elif target == total:
            return len(nums)

        result = math.inf
        l = 0
        trial = 0
        for r in range(len(nums)):
            trial += nums[r]
            while trial >= target:
                result = min(result, r-l+1)
                trial -= nums[l]
                l += 1

        return result


    #   runtime: beats 7%
    def minSubArrayLen_ans_BSearch(self, target, nums):
    
        def find_left(left, right, nums, target, n):
            while left < right:
                mid = (left + right) // 2
                if n - nums[mid] >= target:
                    left = mid + 1
                else:
                    right = mid
            return left            

        result = len(nums) + 1
        for i, n in enumerate(nums[1:], 1):
            nums[i] = nums[i - 1] + n

        l = 0
        for r, n in enumerate(nums):
            if n >= target:
                l = find_left(l, r, nums, target, n)
                result = min(result, r - l + 1)
        return result if result <= len(nums) else 0


s = Solution()
test_functions = [ s.minSubArrayLen_naive, s.minSubArrayLen_ans_slidingWindow, s.minSubArrayLen_ans_BSearch, ]

inputs = [ (7,[2,3,1,2,4,3]), (4,[1,4,4]), (11,[1,1,1,1,1,1,1,1]), (11,[1,2,3,4,5]), (15,[1,2,3,4,5]), (80,[10,5,13,4,8,4,5,11,14,9,16,10,20,8]), ]
checks = [ 2, 1, 0, 3, 5, 6, ]
assert len(inputs) == len(checks)

for f in test_functions:
    print(f.__name__)
    startTime = time.time()
    for (target, nums), check in zip(inputs, checks):
        print(f"target=({target}), nums=({nums})")
        result = f(target, nums)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_ms=(%0.2f)" % ((time.time() - startTime) * 1000000))
    print()

