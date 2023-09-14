import time
import itertools
from typing import List, Optional

class Solution:
    """Given array of elevation changes, `gain`, determine the maximum gain in altitude above the starting point"""

    #   runtime: beats 97%
    def largestAltitude_i(self, gain: List[int]) -> int:
        altitude = [ 0 for _ in range(len(gain)+1) ]
        for i, climb in enumerate(gain):
            altitude[i+1] = altitude[i] + climb
        return max(altitude)


    #   runtime: beats 98%
    def largestAltitude_ii(self, gain: List[int]) -> int:
        altitude = [0] + list(itertools.accumulate(gain))
        return max(altitude)


    #   runtime: beats 95%
    def largestAltitude_iii(self, gain: List[int]) -> int:
        total = 0
        result = 0
        for climb in gain:
            total += climb
            result = max(result, total)
        return result


s = Solution()
test_functions = [ s.largestAltitude_i, s.largestAltitude_ii, s.largestAltitude_iii, ]

inputs = [ [-5,1,5,0,-7], [-4,-3,-2,-1,4,3,2], ]
checks = [ 1, 0, ]
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

