import time
from typing import List, Optional

class Solution:
    """Determine how many binary trees can be constructed from the values in `arr` where each node may only have children whose product are equal to it"""

    #   runtime: beats 61%
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr = sorted(arr)

        #   table[i]: number of trees which can be formed with root node `arr[i]`
        table = [ 1 ] * len(arr)

        #   map values in `arr` to their indexes
        indexes = { n: i for i, n in enumerate(arr) }

        #   find all numbers `left` / `right` in `arr` that are factors of each number
        for i, current in enumerate(arr):
            for j, left in enumerate(arr[:i+1]):
                right = current // left
                if current % left != 0:
                    continue
                if not right in indexes:
                    continue
                k = indexes[right]
                table[i] += table[j] * table[k]

        return sum(table) % (10**9 + 7)


s = Solution()
test_functions = [ s.numFactoredBinaryTrees, ]

inputs = [ [2,4], [2,4,5,10], ]
checks = [ 3, 7, ]
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

