import time
from typing import List, Optional

class Solution:
    """Given a string, representing a letter excel column title, return the corresponding column number"""

    def titleToNumber(self, columnTitle: str) -> int:
        atoi = { x: chr(x+ord('A')-1) for x in range(1, 27) }
        itoa = { chr(x+ord('A')-1): x for x in range(1, 27) }


s = Solution()
test_functions = [ s.titleToNumber, ]

inputs = [ "A", "AB", "ZY", "HE", "AEE", ]
checks = [ 1, 28, 701, 213, 811, ]
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


