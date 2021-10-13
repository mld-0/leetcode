#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
import math
import bisect
from typing import List
#   {{{2
class Solution:

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #return self.minSubArrayLen_ii(target, nums)
        #return self.minSubArrayLen_TwoPointers(target, nums)
        return self.minSubArrayLen_BinarySearch(target, nums)


    #   runtime: beats 64%
    def minSubArrayLen_TwoPointers(self, target: int, nums: List[int]) -> int:
        result = math.inf
        l = 0
        trial = 0
        for r in range(len(nums)):
            trial += nums[r]
            while trial >= target:
                if r - l + 1 < result:
                    result = r - l + 1
                trial -= nums[l]
                l += 1
        if result == math.inf:
            return 0
        return result


    #   runtime: beats 35%
    def minSubArrayLen_BinarySearch(self, target: int, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        result = math.inf

        #   sums[n] = sum of first n elements in nums
        sums = [0] * (len(nums)+1)
        for i in range(1, len(nums)+1):
            sums[i] = sums[i-1] + nums[i-1]

        for i in range(1, len(nums)+1):
            search = target + sums[i-1]
            bound = bisect.bisect_left(sums, search)
            if bound != len(sums):
                if bound - i + 1 < result:
                    result = bound - i + 1

        if result == math.inf:
            return 0
        return result


    #   runtime: TLE
    def minSubArrayLen_i(self, target: int, nums: List[int]) -> int:
        result = math.inf
        for l in range(len(nums)):
            for r in range(l, len(nums)):
                trial = sum(nums[l:r+1])
                if target <= trial  and r - l + 1 < result:
                    result_sum = trial
                    result = r - l + 1
        if result == math.inf:
            return 0
        return result


    #   runtime: TLE
    def minSubArrayLen_ii(self, target: int, nums: List[int]) -> int:
        result = math.inf
        sums = [0] * len(nums)
        for i in range(1, len(nums)):
            sums[i] = sums[i-1] + nums[i]
        for l in range(len(nums)):
            for r in range(l, len(nums)):
                trial = sums[r] - sums[l] + nums[l]
                if target <= trial and r - l + 1 < result:
                    result_sum = trial
                    result = r - l + 1
                    break
        if result == math.inf:
            return 0
        return result


s = Solution()

input_values = [ (7, [2,3,1,2,4,3]), (4, [1,4,4]), (11, [1,1,1,1,1,1,1,1]), (11, [1,2,3,4,5]), ]
input_checks = [ 2, 1, 0, 3, ]

for (target, nums), check in zip(input_values, input_checks):
    print("target=(%s), nums=(%s)" % (target, nums))
    result = s.minSubArrayLen(target, nums)
    print("result=(%s)" % result)
    assert result == check, "Check failed"
    print()

