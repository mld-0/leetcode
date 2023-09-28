import time
from typing import List, Optional

def guess(num: int) -> int:
    if num > pick:
        return -1
    elif num < pick:
        return 1
    elif num == pick:
        return 0
    raise UnreachableError()

class Solution:

    #   runtime: beats 89%
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n
        while True:
            mid = l + (r - l) // 2
            trial = guess(mid)
            if trial == 0:
                return mid
            elif trial > 0:
                l = mid + 1
            elif trial < 0:
                r = mid - 1


s = Solution()
test_functions = [ s.guessNumber, ]

inputs = [ (10,6), (1,1), (2,1), ]
checks = [ 6, 1, 1, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for (n, pick), check in zip(inputs, checks):
        print(f"n=({n}), pick=({pick})")
        result = f(n)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

