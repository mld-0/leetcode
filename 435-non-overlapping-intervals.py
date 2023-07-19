import math
import time
from typing import List

#   Greedy solution to the interval scheduling problem: 
#   For each set of overlapping intervals, keep the one with the earlist finish time

class Solution:

    #   runtime: beats 5%
    def eraseOverlapIntervals_i(self, intervals: List[List[int]]) -> int:
        intitial_len = len(intervals)
        intervals = sorted(intervals)
        i = 1
        while i < len(intervals):
            a = intervals[i-1]
            b = intervals[i]
            if b[0] < a[1]:
                if b[1] < a[1]:
                    intervals.remove(a)
                else:
                    intervals.remove(b)
            else:
                i += 1
        return intitial_len - len(intervals) 


    #   runtime: beats 5%
    def eraseOverlapIntervals_ii(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        removed = set()
        i = 1
        while i < len(intervals):
            l = i-1
            while l in removed:
                l -= 1
            r = i
            while r in removed:
                r -= 1
            a = intervals[l]
            b = intervals[r]
            if b[0] < a[1]:
                if b[1] < a[1]:
                    removed.add(l)
                else:
                    removed.add(r)
            i += 1
        return len(removed)


    #   runtime: beats 99%
    def eraseOverlapIntervals_ans(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[1])
        result_intervals = set()
        most_recent_end_time = -math.inf
        for i, (start, end) in enumerate(intervals):
            if start >= most_recent_end_time:
                most_recent_end_time = end
                result_intervals.add(i)
        return len(intervals) - len(result_intervals)


s = Solution()
test_functions = [ s.eraseOverlapIntervals_i, s.eraseOverlapIntervals_ii, s.eraseOverlapIntervals_ans, ]

inputs = [ [[1,2],[2,3],[3,4],[1,3]], [[1,2],[1,2],[1,2]], [[1,2],[2,3]], [[1,100],[11,22],[1,11],[2,12]], [[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]], ]
checks = [ 1, 2, 0, 2, 7, ]
assert len(inputs) == len(checks)

for f in test_functions:
    print(f.__name__)
    startTime = time.time()
    for intervals, check in zip(inputs, checks):
        print(f"intervals=({intervals})")
        result = f(intervals)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_ms=(%0.2f)" % ((time.time() - startTime) * 1_000_000))
    print()

