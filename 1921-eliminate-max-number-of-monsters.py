import time
import heapq
from collections import deque
from typing import List, Optional

class Solution:
    """`dist[i]` gives the initial distance of the i-th monster and `speed[i]` gives the speed of the i-th monster. A single monster can be eliminated per turn. Monsters take d/v turns to reach our position. Determine the number of monsters which can be eliminated before the first monster reaches us"""

    #   runtime: beats 78%
    def eliminateMaximum_GreedySorting(self, dist: List[int], speed: List[int]) -> int:
        arrival_time = deque(sorted( [ d / s for d, s in zip(dist, speed) ] ))
        result = 0
        t = 0
        while len(arrival_time) > 0:
            next_arrival = arrival_time.popleft()
            if next_arrival <= t:
                return result
            else:
                result += 1
            t += 1
        return result


    #   runtime: beats 98%
    def eliminateMaximum_GreedySorting_ii(self, dist: List[int], speed: List[int]) -> int:
        arrival_time = sorted( [ d / s for d, s in zip(dist, speed) ] )
        t = 0
        for i in range(len(arrival_time)):
            if arrival_time[i] <= t:
                break
            t += 1
        return t


    #   runtime: beats 27%
    def eliminateMaximum_ans_Heap(self, dist: List[int], speed: List[int]) -> int:
        arrival_time = [ d / s for d, s in zip(dist, speed) ]
        heapq.heapify(arrival_time)
        t = 0
        while arrival_time:
            if heapq.heappop(arrival_time) <= t:
                break
            t += 1
        return t


s = Solution()
test_functions = [ s.eliminateMaximum_GreedySorting, s.eliminateMaximum_GreedySorting_ii, s.eliminateMaximum_ans_Heap, ]

inputs = [ ([1,3,4],[1,1,1]), ([1,1,2,3],[1,1,1,1]), ([3,2,4],[5,3,2]), ]
checks = [ 3, 1, 1, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for (dist, speed), check in zip(inputs, checks):
        print(f"dist=({dist}), speed=({speed})")
        result = f(dist, speed)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

