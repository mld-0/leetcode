import time
import copy
from typing import List, Optional

class Solution:

    #   runtime: beats 96%
    def sortArrayByParity_Sorting(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda x: x % 2)


    #   runtime: beats 97%
    def sortArrayByParity_TwoPointers(self, nums: List[int]) -> List[int]:
        l = 0
        r = 0
        while r < len(nums):
            if nums[r] % 2 == 0:
                nums[r], nums[l] = nums[l], nums[r]
                l += 1
            r += 1
        return nums


    #   runtime: beats 99%
    def sortArrayByParity_NewLists(self, nums: List[int]) -> List[int]:
        odds = []
        evens = []
        for n in nums:
            if n % 2 == 0:
                evens.append(n)
            else:
                odds.append(n)
        return evens + odds


    #   runtime: beats 92%
    def sortArrayByParity_ans_TwoPass(self, nums: List[int]) -> List[int]:
        return [x for x in nums if x % 2 == 0] + [x for x in nums if x % 2 == 1]


    #   runtime: beats 99%
    def sortArrayByParity_ans_TwoPointers(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] % 2 > nums[j] % 2:
                nums[i], nums[j] = nums[j], nums[i]
            if nums[i] % 2 == 0: i += 1
            if nums[j] % 2 == 1: j -= 1
        return nums


s = Solution()
test_functions = [ s.sortArrayByParity_Sorting, s.sortArrayByParity_TwoPointers, s.sortArrayByParity_NewLists, s.sortArrayByParity_ans_TwoPass, s.sortArrayByParity_ans_TwoPointers, ]

inputs = [ [3,1,2,4], [0], [3,5,8,7,9,1,2,4,5,10,53,21,34], ]

def validate_result(nums: List[int]) -> bool:
    check = [ n % 2 for n in nums ]
    sorted_check = sorted(check)
    return check == sorted_check

for f in test_functions:
    print(f.__name__)
    inputs = copy.deepcopy(inputs)
    start_time = time.time()
    for nums in inputs:
        print(f"nums=({nums})")
        result = f(nums)
        print(f"result=({result})")
        assert validate_result(result), "Check validation failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

