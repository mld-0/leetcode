import math
import time
from typing import List

class Solution:

    #   runtime: beats 6%
    def average_sorting(self, salary: List[int]) -> float:
        return sum(sorted(salary)[1:-1]) / (len(salary)-2)


    #   runtime: beats 36%
    def average_ii(self, salary: List[int]) -> float:
        total = 0
        top = -math.inf
        bottom = math.inf
        for x in salary:
            top = max(top, x)
            bottom = min(bottom, x)
            total += x
        return (total - top - bottom) / (len(salary) - 2)


    #   runtime: beats 40%
    def average_iii(self, salary: List[int]) -> float:
        return (sum(salary) - max(salary) - min(salary)) / (len(salary) - 2)


s = Solution()

test_functions = [ s.average_sorting, s.average_ii, s.average_iii, ]

inputs = [ [4000,3000,1000,2000], [1000,2000,3000], ]
checks = [ 2500.0, 2000.0, ]
assert len(inputs) == len(checks)

for f in test_functions:
    print(f.__name__)
    startTime = time.time()
    for salary, check in zip(inputs, checks):
        print(f"salary=({salary})")
        result = f(salary)
        print(f"result=({result})")
        assert abs(check - result) < 10**-5, "Check comparison failed"
    print(f"elapsed_ms=(%0.2f)" % ((time.time() - startTime)*1000000))
    print()

