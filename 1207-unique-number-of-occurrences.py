from typing import List
from collections import Counter

class Solution:

    #   runtime: beats 97%
    def uniqueOccurences(self, arr: List[int]) -> bool:
        counts = Counter(arr)
        counts_set = set(counts.values())
        if len(counts.values()) == len(counts_set):
            return True
        return False


s = Solution()
test_functions = [ s.uniqueOccurences, ]

inputs = [ [1,2,2,1,1,3], [1,2], [-3,0,1,-3,1,1,1,-3,10,0], ]
checks = [ True, False, True, ]
assert len(inputs) == len(checks)

for f in test_functions:
    print(f.__name__)
    for arr, check in zip(inputs, checks):
        print(f"arr=({arr})")
        result = f(arr)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print()

