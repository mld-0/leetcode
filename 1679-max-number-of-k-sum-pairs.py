import time
from collections import defaultdict, Counter
from typing import List, Optional

class Solution:
    """Determine how many pairs of numbers in `nums` sum to `k`"""

    #   runtime: beats 73%
    def maxOperations_TwoPointers(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        result = 0
        l = 0
        r = len(nums) - 1
        while l < r:
            trial = nums[l] + nums[r]
            if trial == k:
                result += 1
                l += 1
                r -= 1
            elif trial > k:
                r -= 1
            elif trial < k:
                l += 1
        return result


    #   runtime: TLE
    def maxOperations_HashMap(self, nums: List[int], k: int) -> int:
        d = defaultdict(set)
        used = set()
        result = 0
        for i, n in enumerate(nums):
            d[n].add(i)
        for i, n in enumerate(nums):
            if i in used:
                continue
            delta = k - n
            for j in d[delta]:
                if i == j:
                    continue
                if j not in used:
                    used.add(i)
                    used.add(j)
                    result += 1
                    break
        return result


    #   runtime: beats 94%
    def maxOperations_Counter(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        result = 0
        for n in c.keys():
            if n + n == k and c[n] > 1:
                result += c[n] // 2
                c[n] %= 2
        for n in c.keys():
            if c[n] > 0:
                delta = k - n
                if delta == n:
                    continue
                if delta in c.keys() and c[delta] > 0:
                    pairs = min(c[n], c[delta])
                    c[n] -= pairs
                    c[delta] -= pairs
                    result += pairs
        return result


    #   runtime: beats 92%
    def maxOperations_ans_CounterOnePass(self, nums: List[int], k: int) -> int:
        c = defaultdict(int)
        result = 0
        for i, n in enumerate(nums):
            delta = k - n
            if delta in c and c[delta] > 0:
                c[delta] = c[delta] - 1
                result += 1
            else:
                c[n] = c[n] + 1
        return result


s = Solution()
test_functions = [ s.maxOperations_TwoPointers, s.maxOperations_HashMap, s.maxOperations_Counter, s.maxOperations_ans_CounterOnePass, ]

n = 20
inputs = [ ([1,2,3,4],5), ([3,1,3,4,3],6), ([3,1,5,1,1,1,1,1,2,2,3,2,2],1), ([2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2],3), ([x for _ in range(n) for x in [2,3]],5), ]
checks = [ 2, 1, 0, 4, n, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for (nums, k), check in zip(inputs, checks):
        print(f"nums=({nums}), k=({k})")
        result = f(nums, k)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

