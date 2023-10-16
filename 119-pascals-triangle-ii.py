import time
from typing import List, Optional

class Solution:

    #   runtime: beats 98%
    def getRow(self, rowIndex: int) -> List[int]:
        current_row = [1]
        next_row = [1]
        for i in range(rowIndex):
            for j in range(1, len(current_row)):
                temp = current_row[j] + current_row[j-1]
                next_row.append(temp)
            next_row.append(1)
            current_row = next_row
            next_row = [1]
        return current_row


s = Solution()
test_functions = [ s.getRow, ]

inputs = [ 3, 0, 1, 4, ]
checks = [ [1,3,3,1], [1], [1,1], [1,4,6,4,1], ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for rowIndex, check in zip(inputs, checks):
        print(f"rowIndex=({rowIndex})")
        result = f(rowIndex)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

