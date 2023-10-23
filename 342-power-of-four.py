import time
import math
from typing import List, Optional

class Solution:

    #   runtime: beats 84%
    def isPowerOfFour_naive(self, n: int) -> bool:
        if n <= 0:
            return False
        l = int(math.log(n) / math.log(4)) + 1
        for i in range(0, l):
            if 4 ** i == n:
                return True
        return False


    #   runtime: beats 95%
    def isPowerOfFour_ans_division(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 4 == 0:
            n /= 4
        return n == 1


    #   runtime: beats 72%
    def __init__(self):
        max_power = 15
        self.nums = nums = [1] * (max_power + 1)
        for i in range(1, max_power + 1):
            nums[i] = 4 * nums[i - 1]
        self.nums = set(self.nums)
    def isPowerOfFour_ans_precompute(self, n: int) -> bool:
        return n in self.nums


    #   runtime: beats 97%
    def isPowerOfFour_ans_math(self, n: int) -> bool:
        return n > 0 and math.log2(n) % 2 == 0


    #   runtime: beats 99%
    def isPowerOfFour_ans_bitwise(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0 and n & 0xaaaaaaaa == 0


s = Solution()
test_functions = [ s.isPowerOfFour_naive, s.isPowerOfFour_ans_division, s.isPowerOfFour_ans_precompute, s.isPowerOfFour_ans_math, s.isPowerOfFour_ans_math, s.isPowerOfFour_ans_bitwise, ]

inputs = [ 16, 5, 1, -2147483648, ]
checks = [ True, False, True, False, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for n, check in zip(inputs, checks):
        print(f"n=({n})")
        result = f(n)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

