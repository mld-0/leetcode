import time
from typing import List, Optional, Tuple

class Solution:

    #   runtime: beats 98%
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:

        def chebyshev_distance(x1, y1, x2, y2):
            dx = abs(x2 - x1)
            dy = abs(y2 - y1)
            return max(dx, dy)

        result = 0
        for i in range(1, len(points)):
            current = points[i]
            previous = points[i-1]
            result += chebyshev_distance(*current, *previous)
        return result


s = Solution()
test_functions = [ s.minTimeToVisitAllPoints, ]

inputs = [ [[1,1],[3,4],[-1,0]], [[3,2],[-2,2]], ]
checks = [ 7, 5, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for points, check in zip(inputs, checks):
        print(f"points=({points})")
        result = f(points)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

