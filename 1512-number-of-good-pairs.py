import time
from collections import defaultdict, Counter
from typing import List, Optional

class Solution:
    """Determine the number of pairs that can be formed where `nums[i] == nums[j]` and `i < j`"""

    #   runtime: beats 97%
    def numIdenticalPairs_i(self, nums: List[int]) -> int:
        locations = defaultdict(list)
        for i, n in enumerate(nums):
            locations[n].append(i)
        result = 0
        for n in locations:
            for i in range(len(locations[n])):
                result += len(locations[n]) - i - 1
        return result


    #   runtime: beats 91%
    def numIdenticalPairs_ans(self, nums: List[int]) -> int:
        counts = Counter(nums)
        result = 0
        for count in counts.values():
            result += count * (count - 1) // 2
        return result


s = Solution()
test_functions = [ s.numIdenticalPairs_i, s.numIdenticalPairs_ans, ]

inputs = [ [1,2,3,1,1,3], [1,1,1,1], [1,2,3], ]
checks = [ 4, 6, 0, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for nums, check in zip(inputs, checks):
        print(f"nums=({nums})")
        result = f(nums)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

