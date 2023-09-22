import time
from collections import deque
from typing import List, Optional

#   runtime: beats 8%
class RecentCounter_i:
    def __init__(self):
        self.requests = deque()
        self.past_delta = 3000   
    def ping(self, t: int) -> int:
        self.requests.appendleft(t)
        r = [ t-self.past_delta, t ]
        result = 0
        for i, x in enumerate(self.requests):
            if x >= r[0] and x <= r[1]:
                result += 1
            else:
                break
        return result


#   runtime: beats 95%
class RecentCounter_ii:
    def __init__(self):
        self.requests = deque()
        self.past_delta = 3000
    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[0] < t - self.past_delta:
            self.requests.popleft()
        return len(self.requests)


test_classes = [ RecentCounter_i, RecentCounter_ii, ]

inputs = [ [1,100,3001,3002], ]
checks = [ [1,2,3,3], ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for c in test_classes:
    s = c()
    f = s.ping
    print(f.__name__)
    start_time = time.time()
    for vals, check in zip(inputs, checks):
        print(f"vals=({vals})")
        result = []
        for t in vals:
            result.append(f(t))
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()


