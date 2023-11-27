import sys
import time
from functools import cache
from typing import List, Optional

class Solution:

    #   runtime: beats 46%
    def knightDialer_DP_TopDown(self, n: int) -> int:
        connected = { 1: [8,6], 2: [7,9], 3: [4,8], 4: [3,9,0], 5: [], 6: [1,7,0], 7: [2,6], 8: [1,3], 9: [4,2], 0: [4,6], }

        @cache
        def solve(current_num: int, n: int) -> int:
            if n == 0:
                return 1
            result = 0
            for next_num in connected[current_num]:
                result += solve(next_num, n-1)
            return result

        sys.setrecursionlimit(100_000)
        solutions = []
        result = 0
        for start in range(0, 10):
            result += solve(start, n-1)

        return result % (10**9 + 7)


    #   runtime: beats 62%
    def knightDialer_DP_BottomUp(self, n: int) -> int:
        connected = { 1: [8,6], 2: [7,9], 3: [4,8], 4: [3,9,0], 5: [], 6: [1,7,0], 7: [2,6], 8: [1,3], 9: [4,2], 0: [4,6], }

        #   table[j][i]: number of numbers that can be made from current_num=i with n=j jumps remaining
        table = [ [ 0 for _ in range(0,10) ] for _ in range(0,n) ]

        for i in range(0,10):
            table[0][i] = 1

        for j in range(1, n):
            for current_num in range(0,10):
                for next_num in connected[current_num]:
                    table[j][current_num] += table[j-1][next_num]

        result = sum(table[n-1])
        return result % (10**9 + 7)


    #   runtime: beats 67%
    def knightDialer_DP_BottomUp_Optimised(self, n: int) -> int:
        connected = { 1: [8,6], 2: [7,9], 3: [4,8], 4: [3,9,0], 5: [], 6: [1,7,0], 7: [2,6], 8: [1,3], 9: [4,2], 0: [4,6], }

        table_previous = [ 1 for _ in range(0,10) ]
        table_current = table_previous

        for j in range(1, n):
            table_current = [ 0 for _ in range(0,10) ]
            for current_num in range(0,10):
                for next_num in connected[current_num]:
                    table_current[current_num] += table_previous[next_num]
            table_previous = table_current

        result = sum(table_current)
        return result % (10**9 + 7)


    #   runtime: beats 98%
    def knightDialer_ans_States(self, n: int) -> int:
        if n == 1:
            return 10
        A = 4
        B = 2
        C = 2
        D = 1
        MOD = 10 ** 9 + 7
        for _ in range(n - 1):
            A, B, C, D = (2 * (B + C)) % MOD, A, (A + 2 * D) % MOD, C 
        return (A + B + C + D) % MOD


    #   runtime: beats 93%
    def knightDialer_ans_LinearAlgebra(self, n: int) -> int:

        def multiply(A, B):
            result = [[0] * len(B[0]) for _ in range(len(A))]
            for i in range(len(A)):
                for j in range(len(B[0])):
                    for k in range(len(B)):
                        result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % MOD
            return result

        if n == 1:
            return 10
        A = [ [0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 1, 0, 0, 0, 1, 0], [1, 0, 0, 1, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 1, 0, 0, 0, 0, 0], ]
        v = [[1] * 10]
        MOD = 10 ** 9 + 7
        n -= 1
        while n:
            if n & 1:
                v = multiply(v, A)

            A = multiply(A, A)
            n >>= 1
        return sum(v[0]) % MOD


s = Solution()
test_functions = [ s.knightDialer_DP_TopDown, s.knightDialer_DP_BottomUp, s.knightDialer_DP_BottomUp_Optimised, s.knightDialer_ans_States, s.knightDialer_ans_LinearAlgebra, ]

inputs = [ 1, 2, 3131, ]
checks = [ 10, 20, 136006598, ]
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

