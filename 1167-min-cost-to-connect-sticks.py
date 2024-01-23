import time
import heapq
from typing import List, Optional

class Solution:
    """Sticks of length `x` and `y` can be connected with a cost of `x+y`. Determine the minimum cost to connect all sticks, where `sticks[i]` gives the length of the `i`-th stick"""

    #   runtime: beats 99%
    def connectSticks_HeapPriorityQueue(self, sticks: List[int]) -> int:
        if len(sticks) <= 1:
            return 0
        heapq.heapify(sticks)
        result = 0
        while len(sticks) > 1:
            s1 = heapq.heappop(sticks)
            s2 = heapq.heappop(sticks)
            s3 = s1 + s2
            result += s3
            heapq.heappush(sticks, s3)
        return result


s = Solution()
test_functions = [ s.connectSticks_HeapPriorityQueue, ]

inputs = [ [2,4,3], [1,8,3,5], [5], [3354,4316,3259,4904,4598,474,3166,6322,8080,9009], ]
checks = [ 14, 30, 0, 151646, ]
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

