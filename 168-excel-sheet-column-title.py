import time
from typing import List, Optional

class Solution:
    """Given a number, return the excel column letter corresponding to that number"""

    #   runtime: beats 96%
    def convertToTitle_ans(self, columnNumber: int) -> str:
        atoi = { x: chr(x+ord('A')-1) for x in range(1, 27) }
        result = ""
        while columnNumber > 0:
            columnNumber -= 1
            a = columnNumber % 26 + 1
            result += str(atoi[a])
            columnNumber //= 26
        return result[::-1]


s = Solution()
test_functions = [ s.convertToTitle_ans, ]

inputs = [ 1, 78, 79, 80, 52, 53, 54, 25, 26, 27, 28, 701, 702, 703, 704, 213, 811, ]
checks = [ "A", "BZ", "CA", "CB", "AZ", "BA", "BB", "Y", "Z", "AA", "AB", "ZY", "ZZ", "AAA", "AAB", "HE", "AEE", ]
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
    print("elapsed_ms=(%0.2f)" % ((time.time() - start_time) * 1000000))
    print()

