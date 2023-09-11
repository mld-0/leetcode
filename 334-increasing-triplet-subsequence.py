import time
import math
from typing import List, Optional

class Solution:
    """Determine if there exists a triple of indicies, (i,j,k), such that i<j<k and nums[i]<nums[j]<nums[k]"""

    #   runtime: beats 80%
    def increasingTriplet_ans_i(self, nums: List[int]) -> bool:
        a = math.inf
        b = math.inf
        c = math.inf
        for n in nums:
            if n < a and n < b and n < c:
                a = n
            elif n > a and n < b and n < c:
                b = n
            elif n > a and n > b and n < c:
                c = n
        return (a < math.inf) and (b < math.inf) and (c < math.inf)


    #   runtime: beats 89%
    def increasingTriplet_ans_ii(self, nums: List[int]) -> bool:
        a = math.inf
        b = math.inf
        for n in nums:
            if n < a and n < b:
                a = n
            elif n > a and n < b:
                b = n
            elif n > a and n > b:
                return True
        return False


s = Solution()
test_functions = [ s.increasingTriplet_ans_i, s.increasingTriplet_ans_ii, ]

inputs = [ [1,2,3,4,5], [5,4,3,2,1], [2,1,5,0,4,6], [20,100,10,12,5,13], [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], [6,7,1,2], ]
checks = [ True, False, True, True, False, False, ]
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

