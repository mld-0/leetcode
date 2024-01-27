import time
import itertools
import functools
from typing import List, Optional

class Solution:
    """For an array, [1..n] (inclusive), determine the number of arrangements that have `k` inverse pairs - that is, pairs `(i,j)` such that i < j and nums[j] < nums[i]"""

    #   hint: that is, the number of times a number is shifted left from the origional array

    #   runtime: TLE
    def kInversePairs_naive(self, n: int, k: int) -> int:

        def count_inverse_pairs(vals):
            count = 0
            for i in range(len(vals)-1):
                for j in range(i+1, len(vals)):
                    if vals[i] > vals[j]:
                        count += 1
            return count

        result = 0
        for perm in itertools.permutations(range(1, n+1)):
            if count_inverse_pairs(perm) == k:
                result += 1

        return result % (10**9 + 7)


    #   runtime: TLE
    def kInversePairs_ans_DP_TopDown(self, n: int, k: int) -> int:

        @functools.lru_cache
        def solve(n, k):
            if n == 0:
                return 0
            if k == 0:
                return 1
            result = 0
            for i in range(0, min(k,n-1)+1):
                result += solve(n-1, k-i)
            return result

        return solve(n, k) % (10**9 + 7)


    #   runtime: TLE
    def kInversePairs_ans_DP_BottomUp(self, n: int, k: int) -> int:
        table = [ [ 0 for _ in range(k+1) ] for _ in range(n+1) ]
        for i in range(1, n+1):
            for j in range(0, k+1):
                if j == 0:
                    table[i][j] = 1
                else:
                    for p in range(0, min(j, i-1)+1):
                        table[i][j] = table[i][j] + table[i-1][j-p]
        return table[n][k] % (10**9 + 7)


    def kInversePairs_ans_NotTLE(self, n: int, k: int) -> int:
        raise NotImplementedError("Even first two DP ans are TLE - there are more ans yet to be implemented, surely not all are TLE?")


s = Solution()
test_functions = [ s.kInversePairs_naive, s.kInversePairs_ans_DP_TopDown, s.kInversePairs_ans_DP_BottomUp, s.kInversePairs_ans_NotTLE, ]

inputs = [ [3,0], [3,1], [2,1], [5,1], [4,3], ]
checks = [ 1, 2, 1, 4, 6, ]

assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for (n, k), check in zip(inputs, checks):
        print(f"n=({n}), k=({k})")
        result = f(n, k)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

