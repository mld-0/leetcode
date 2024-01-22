import time
from collections import Counter
from typing import List, Optional

class Solution:
    """Given a list of numbers, `s`, containing 1..n, with one number in that range missing and one duplicated, return as a list, the duplicate and the missing number"""

    #   runtime: beats 91%
    def findErrorNums_Counter(self, nums: List[int]) -> List[int]:
        duplicate_val = None
        missing_val = None
        nums_counts = Counter(nums)
        for i in range(1, len(nums)+1):
            if not i in nums_counts.keys():
                missing_val = i
            elif nums_counts[i] > 1:
                duplicate_val = i
        return [ duplicate_val, missing_val ]


    #   runtime: beats 98%
    def findErrorNums_Sorting(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        duplicate_val = None
        missing_val = None
        if nums[0] != 1:
            missing_val = 1
        elif nums[-1] != len(nums):
            missing_val = len(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                duplicate_val = nums[i]
            if duplicate_val is None:
                if nums[i] != i + 1 and missing_val is None:
                    missing_val = i + 1
            else:
                if nums[i] != i and missing_val is None:
                    missing_val = i
        return [ duplicate_val, missing_val ]


    #   runtime: beats 91%
    def findErrorNums_ans_Sorting(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        duplicate_val = None
        missing_val = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                duplicate_val = nums[i]
            elif nums[i] > nums[i-1] + 1:
                missing_val = nums[i-1] + 1
        if nums[-1] != len(nums):
            return [ duplicate_val, len(nums) ]
        else:
            return [ duplicate_val, missing_val ]


    #   runtime: beats 85%
    def findErrorNums_ans_InvertDuplicateIndex(self, nums: List[int]) -> List[int]:
        duplicate_val = None
        missing_val = 1
        for i in range(len(nums)):
            n = nums[i]
            if nums[abs(n)-1] < 0:
                duplicate_val = abs(n)
            else:
                nums[abs(n)-1] *= -1
        for i in range(1, len(nums)):
            if nums[i] > 0:
                missing_val = i + 1
        return [ duplicate_val, missing_val ]


    #   runtime: beats 91%
    def findErrorNums_ans_Mathematical(self, nums: List[int]) -> List[int]:
        diff = 0
        squareDiff = 0
        for i in range(len(nums)):
            diff += (i+1) - nums[i]
            squareDiff += (i+1) * (i+1) - nums[i] * nums[i]
        totalSum = squareDiff // diff
        return [ (totalSum-diff)//2, (totalSum+diff)//2 ]


s = Solution()
test_functions = [ s.findErrorNums_Counter, s.findErrorNums_Sorting, s.findErrorNums_ans_Sorting, s.findErrorNums_ans_InvertDuplicateIndex, s.findErrorNums_ans_Mathematical, ]

inputs = [ [1,2,2,4], [1,1], [2,2], [3,2,3,4,6,5], [1,5,3,2,2,7,6,4,8,9], [37,62,43,27,12,66,36,18,39,54,61,65,47,32,23,2,46,8,4,24,29,38,63,39,25,11,45,28,44,52,15,30,21,7,57,49,1,59,58,14,9,40,3,42,56,31,20,41,22,50,13,33,6,10,16,64,53,51,19,17,48,26,34,60,35,5], ]
checks = [ [2,3], [1,2], [2,1], [3,1], [2,10], [39,55], ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for vals, check in zip(inputs, checks):
        print(f"vals=({vals})")
        result = f(vals[:])
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

