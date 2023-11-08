import time
from typing import List, Optional

class Solution:

    #   runtime: beats 96%
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if (sx == fx and sy == fy) and t == 1:
            return False
        delta_x = abs(sx - fx)
        delta_y = abs(sy - fy)
        a = max(delta_x, delta_y)
        return max(delta_x, delta_y) <= t


s = Solution()
test_functions = [ s.isReachableAtTime, ]

inputs = [ (2,4,7,7,6), (3,1,7,3,3), (1,2,1,2,1), (1,1,1,1,3), (1,3,1,3,0), (5,3,5,3,2), ]
checks = [ True, False, False, True, True, True, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for (sx, sy, fx, fy, t), check in zip(inputs, checks):
        print(f"sx=({sx}), sy=({sy}), fx=({fx}), fy=({fy}), t=({t})")
        result = f(sx, sy, fx, fy, t)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

