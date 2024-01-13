import time
import math
from typing import List, Optional

class BinaryMatrix(object):

    def __init__(self, values: List[int]):
        self.values = values

    def get(self, row: int, col: int) -> int:
        return self.values[row][col]

    def dimensions(self) -> List[int]:
        return [ len(self.values), len(self.values[0]) ]


class Solution:
    """Determine the leftmost column with a 1 in it, where each row is sorted in non-decreasing order"""

    #   runtime: beats 98%
    def leftMostColumnWithOne_i(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()

        def first_one_in_row(row: int) -> int:
            if binaryMatrix.get(row, 0) == 1:
                return 0
            if binaryMatrix.get(row, cols-1) == 0:
                return math.inf
            l = 0
            r = cols - 1
            while l < r:
                mid = (l + r) // 2
                if binaryMatrix.get(row,mid) < 1:
                    l = mid + 1
                else:
                    r = mid
            if l < cols and binaryMatrix.get(row,l) == 1:
                return l
            return math.inf

        result = math.inf
        for row in range(rows):
            temp = first_one_in_row(row)
            result = min(result, temp)
        if result == math.inf:
            return -1
        return result


    def leftMostColumnWithOne_ii(self, binaryMatrix: 'BinaryMatrix') -> int:
        raise NotImplementedError("Complete left-and-down search implementation")


s = Solution()
test_functions = [ s.leftMostColumnWithOne_i, s.leftMostColumnWithOne_ii, ]

inputs = [ [[0,0],[1,1]], [[0,0],[0,1]], [[0,0],[0,0]], ]
checks = [ 0, 1, -1, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for vals, check in zip(inputs, checks):
        print(f"vals=({vals})")
        result = f(BinaryMatrix(vals))
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()


