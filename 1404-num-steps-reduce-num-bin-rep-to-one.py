import time
from collections import deque
from typing import List, Optional

class Solution:
    """Determine the number of steps to reduce a binary number given as a string to 1, dividing even numbers by 2 and adding 1 to odd numbers"""


    #   runtime: beats 100%
    #    memory: beats 81%
    def numSteps_naive(self, s: str) -> int:
        n = int(s, 2)
        result = 0
        while n > 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = n + 1
            result += 1
        return result


    def numSteps_bitwise_deque(self, s: str) -> int:
        raise NotImplementedError("Continue When Leetcode is no longer down (2026-02-26)")

        #   Division by two is a bitshift right
        def div_two(bits):
            bits.pop()
            bits.appendleft("0")

        #   Flip bits moving R->L, stopping when we encounter a zero
        def add_one(bits):
            L = len(bits)
            i = L - 1
            while i >= 0:
                if bits[i] == "1":
                    bits[i] = "0"
                else:
                    bits[i] = "1"
                    break
                i -= 1
            if i == -1:
                bits.appendleft("1")

        def is_one(bits):
            for i in range(len(bits)-1):
                if bits[i] == "1":
                    return False
            if bits[-1] == "1":
                return True
            return False

        def is_even(bits):
            return bits[-1] == "0"

        bits = deque( [ c for c in s ] )
        result = 0
        while not is_one(bits):
            if is_even(bits):
                div_two(bits)
            else:
                add_one(bits)
            result += 1
        return result


    def numSteps_ans(self, s: str) -> int:
        raise NotImplementedError("Continue When Leetcode is no longer down (2026-02-26)")


s = Solution()
test_functions = [ s.numSteps_naive, s.numSteps_bitwise_deque, ]

inputs = [ "1101", "10", "1", "1111011110000011100000110001011011110010111001010111110001", "111", ]
checks = [ 6, 1, 0, 85, 4, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for s, check in zip(inputs, checks):
        print(f"s=({s})")
        result = f(s)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
        print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

