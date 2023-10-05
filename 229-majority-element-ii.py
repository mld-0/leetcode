import time
import copy
from collections import Counter
from typing import List, Optional

class Solution:
    """Find all elements in `nums` that occur more than `len(nums)/3` times. Follow-up: solve in O(n) time and O(1) space. Hint: there can be at most 2 such elements."""

    #   runtime: beats 96%
    def majorityElement_naive(self, nums: List[int]) -> List[int]:
        result = []
        c = Counter(nums)
        k = len(nums) // 3
        for n, v in c.items():
            if v > k:
                result.append(n)
        return result


    #   runtime: beats 96%
    def majorityElement_ans(self, nums: List[int]) -> List[int]:
        k = len(nums) // 3
        candidate1, count1 = None, 0
        candidate2, count2 = None, 0
        for n in nums:
            if candidate1 == n:
                count1 += 1
            elif candidate2 == n:
                count2 += 1
            elif count1 == 0:
                candidate1 = n
                count1 = 1
            elif count2 == 0:
                candidate2 = n
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        count1 = nums.count(candidate1)
        count2 = nums.count(candidate2)
        result = []
        if count1 > k:
            result.append(candidate1)
        if count2 > k and candidate1 != candidate2:
            result.append(candidate2)
        return result


s = Solution()
test_functions = [ s.majorityElement_naive, s.majorityElement_ans, ]

inputs = [ [3,2,3], [1], [1,2], [1,2,3,4,5,6,7,8,9], [1,1,1,1,2,2,2,3], [5,5,1], ]
checks = [ [3], [1], [1,2], [], [1,2], [5], ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    inputs = copy.deepcopy(inputs)
    start_time = time.time()
    for nums, check in zip(inputs, checks):
        print(f"nums=({nums})")
        result = f(nums)
        print(f"result=({result})")
        assert sorted(result) == sorted(check), "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

