import time
import itertools
from typing import List, Set

class Solution:

    #   runtime: beats 79%
    def combine_Backtrack(self, n: int, k: int):
        result = []
        values = list(range(1, n+1))

        def backtrack(first=0, cur=None):
            nonlocal n
            if cur is None:
                cur = []
            if len(cur) == k:
                result.append(cur[:])
                return
            for i in range(first, len(values)):
                cur.append(values[i])
                backtrack(i+1, cur)
                cur.pop()

        backtrack()
        return result


    #   runtime: beats 77%
    def combine_Backtrack_subsequent(self, n: int, k: int) -> List[List[int]]:

        def solve(partial: Set[int], n: int, k: int):
            if k == 0:
                result.add(tuple(sorted(partial)))
                return
            for n in range(1,n+1):
                if n in partial:
                    continue
                partial.add(n)
                solve(partial, n, k-1)
                partial.remove(n)

        result = set()
        solve(set(), n, k)
        return [ list(x) for x in result ]


    #   runtime: beats 70%
    def combine_Recursive(self, n: int, k: int): 
        result = []
        values = list(range(1, n+1))

        def combinations(sofar, rest, n):
            if n == 0:
                result.append(sofar)
                return
            for i in range(len(rest)):
                combinations(sofar + [ rest[i] ], rest[i+1:], n-1)

        combinations([], values, k)
        return result


    #   runtime: beats 99%
    def combine_Lexicographic(self, n: int, k: int):
        #   first combination
        nums = list(range(1, k+1)) + [n+1]
        result = []
        j = 0

        while j < k:
            #   add current combination
            result.append(nums[:k])
            j = 0
            while j < k and nums[j+1] == nums[j] + 1:
                nums[j] = j + 1
                j += 1
            nums[j] += 1

        return result


    #   runtime: beats 99%
    def combine_Itertools(self, n: int, k: int) -> List[List[int]]:
        values = list(range(1, n+1))
        result = [ list(x) for x in itertools.combinations(values, k) ]
        return result


    #   runtime: beats 98%
    def combine_ItertoolsEquivalent(self, n: int, k: int) -> List[List[int]]:

        def combinations(iterable, r):
            # combinations('ABCD', 2) --> AB AC AD BC BD CD
            # combinations(range(4), 3) --> 012 013 023 123
            pool = tuple(iterable)
            n = len(pool)
            if r > n:
                return
            indices = list(range(r))
            yield tuple(pool[i] for i in indices)
            while True:
                for i in reversed(range(r)):
                    if indices[i] != i + n - r:
                        break
                else:
                    return
                indices[i] += 1
                for j in range(i+1, r):
                    indices[j] = indices[j-1] + 1
                yield tuple(pool[i] for i in indices)

        values = list(range(1, n+1))
        result = [ list(x) for x in combinations(values, k) ]
        return result


def compare_sorted(result, check):
    return sorted([sorted(x) for x in result]) == sorted([ sorted(x) for x in check])

s = Solution()
test_functions = [ s.combine_Backtrack, s.combine_Backtrack_subsequent, s.combine_Recursive, s.combine_Lexicographic, s.combine_Itertools, s.combine_ItertoolsEquivalent, ]

inputs = [ (4,2), (1,1), (3,1), ]
checks = [ [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]], [[1]], [[1],[2],[3]], ]
assert len(inputs) == len(checks)

for f in test_functions:
    print(f.__name__)
    startTime = time.time()
    for (n, k), check in zip(inputs, checks):
        print(f"n=({n}), k=({k})")
        result = f(n, k)
        print(f"result=({result})")
        assert compare_sorted(result, check), "Check comparison failed"
    print("elapsed_ms=(%0.2f)" % ((time.time() - startTime) * 1000000))
    print()

