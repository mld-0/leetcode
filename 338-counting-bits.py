import time
from typing import List, Optional

class Solution:

    #   runtime: beats 38%
    def countBits_naive_i(self, n: int) -> List[int]:
        result = []
        for i in range(n+1):
            b = bin(i)[2:]
            n = 0
            for c in b:
                if c == '1':
                    n += 1
            result.append(n)
        return result


    #   runtime: beats 87%
    def countBits_naive_ii(self, n: int) -> List[int]:
        return [ bin(i).count('1') for i in range(n+1) ]


    #   runtime: beats 89%
    def countBits_ans_DP(self, n: int) -> List[int]:
        result = [ 0 for _ in range(n+1) ]
        x = 0
        b = 1
        while b <= n:
            while x < b and x + b <= n:
                result[x+b] = result[x] + 1
                x += 1
            x = 0
            b *= 2
        return result


s = Solution()
test_functions = [ s.countBits_naive_i, s.countBits_naive_ii, s.countBits_ans_DP, ]

inputs = [ 2, 5, ]
checks = [ [0,1,1], [0,1,1,2,1,2], ]
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

