from collections import Counter
from typing import List

class Solution:

    #   runtime: beats 99%
    def containsDuplicate_Set(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


    #   runtime: beats 48%
    def containsDuplicate_Counter(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        return any(c > 1 for c in counts.values())


s = Solution()
test_functions = [ s.containsDuplicate_Set, s.containsDuplicate_Counter, ]

inputs = [ [1,2,3,1], [1,2,3,4], [1,1,1,3,3,4,3,2,4,2], ]
checks = [ True, False, True, ]
assert len(inputs) == len(checks)

for f in test_functions:
    print(f.__name__)
    for nums, check in zip(inputs, checks):
        print(f"nums=({nums})")
        result = f(nums)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print()

