#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
import math
from typing import List, Optional

class Solution:
    """Find the maximum `(n[i]-n[j])*n[k]` where i<j<k for an array `n`"""

    #   runtime: TLE
    def maximumTripletValue_naive(self, nums: List[int]) -> int:
        N = len(nums)
        result = 0
        for i in range(N):
            for j in range(i+1, N):
                for k in range(j+1, N):
                    trial = ( nums[i] - nums[j] ) * nums[k]
                    result = max(result, trial)
        return result


    #   runtime: TLE
    def maximumTripletValue_prefix(self, nums: List[int]) -> int:
        N = len(nums)

        #   prefix_nums[j]: max value of `nums[i]-nums[j]` for i<j
        prefix_nums = [ 0 ] * N
        for i in range(N-1):
            for j in range(i+1, N):
                prefix_nums[j] = max(prefix_nums[j], prefix_nums[j-1], nums[i]-nums[j])

        result = 0
        for k in range(2, N):
            trial = prefix_nums[k-1] * nums[k]
            result = max(trial, result)
        return result



    #   runtime: beats 24%
    #    memory: beats 15%
    def maximumTripletValue_prefixsuffix(self, nums: List[int]) -> int:
        N = len(nums)

        #   prefix_nums[z]: max( nums[:z+1] )
        prefix_nums = [ 0 ] * N
        prefix_nums[0] = nums[0]
        for z in range(1, N):
            prefix_nums[z] = max(nums[z], prefix_nums[z-1])

        #   suffix_nums[z] = max( nums[z:] )
        suffix_nums = [ 0 ] * N
        suffix_nums[N-1] = nums[N-1]
        for z in range(N-2, -1, -1):
            suffix_nums[z] = max(nums[z], suffix_nums[z+1])

        result = 0
        for j in range(1, N-1):
            trial = ( prefix_nums[j-1] - nums[j] ) * suffix_nums[j+1]
            result = max(result, trial)
        return result


    #   runtime: beats 78%
    #    memory: beats 87%
    def maximumTripletValue_ans_greedy(self, nums: List[int]) -> int:
        n = len(nums)
        res, imax, dmax = 0, 0, 0
        for k in range(n):
            res = max(res, dmax * nums[k])
            dmax = max(dmax, imax - nums[k])
            imax = max(imax, nums[k])
        return res


s = Solution()
test_functions = [ s.maximumTripletValue_naive, s.maximumTripletValue_prefix, s.maximumTripletValue_prefixsuffix, s.maximumTripletValue_ans_greedy, ]

inputs = [ [12,6,1,2,7], [1,10,3,4,19], [1,2,3], ]
checks = [ 77, 133, 0, ]
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

