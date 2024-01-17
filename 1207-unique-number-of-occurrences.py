import time
from collections import Counter
from typing import List, Optional

class Solution:
    """Determine whether the number of occurences of each value in `arr` is unique"""

    #   runtime: beats 97%
    def uniqueOccurrences_i(self, arr: List[int]) -> bool:
        counts = Counter(arr)
        counts_set = set(counts.values())
        if len(counts.values()) == len(counts_set):
            return True
        return False


    #   runtime: beats 99%
    def uniqueOccurrences_ii(self, arr: List[int]) -> bool:
        arr_counts = Counter(arr)
        return len(set(arr_counts.values())) == len(arr_counts.items())


s = Solution()
test_functions = [ s.uniqueOccurrences_i, s.uniqueOccurrences_ii, ]

inputs = [ [1,2,2,1,1,3], [1,2], [-3,0,1,-3,1,1,1,-3,10,0], ]
checks = [ True, False, True, ]
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

