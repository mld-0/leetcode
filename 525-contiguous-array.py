#   {{{3
       #   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
from collections import defaultdict
from typing import List, Optional

class Solution:
    """Determine the max length contiguous subarray with an equal number of 0 and 1"""

    def findMaxLength_i(self, nums: List[int]) -> int:

        def is_equal_num(l, r):
            trial = ongoing_sum[r]
            if l > 0:
                trial -= ongoing_sum[l-1]
            result = trial == (r-l+1) / 2
            return result
            
        ongoing_sum = [ 0 for _ in nums ]
        ongoing_sum[0] = nums[0]
        for i in range(1, len(nums)):
            ongoing_sum[i] = ongoing_sum[i-1] + nums[i]

        result = 0
        for l in range(0, len(nums)):
            for r in range(l, len(nums)):
                if is_equal_num(l, r):
                    result = max(result, r-l+1)

        return result


    #   runtime: beats 93%
    def findMaxLength_ans_deltaCount(self, nums: List[int]) -> int:
        delta_10 = 0
        deltas = defaultdict(list)

        deltas[0].append(0)
        for i, n in enumerate(nums):
            if n == 1:
                delta_10 += 1
            elif n == 0:
                delta_10 -= 1
            deltas[delta_10].append(i+1)

        result = 0
        for k in deltas:
            temp = max(deltas[k]) - min(deltas[k])
            result = max(result, temp)

        return result
            

s = Solution()
test_functions = [ s.findMaxLength_i, s.findMaxLength_ans_deltaCount, ]

inputs = [ [0,0,1,0,0,0,1,1], [0,1], [0,1,0], ]
checks = [ 6, 2, 2, ]
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

