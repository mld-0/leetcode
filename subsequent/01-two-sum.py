from typing import List

class Solution:

    #   runtime: TLE
    def twoSum_naive(self, nums: List[int], target: int) -> List[int]:
        for i, x in enumerate(nums):
            delta = target - x
            for j, x in enumerate(nums):
                if i == j:
                    continue
                if x == delta:
                    return [ i, j ]


    #   runtime: beats 95%
    def twoSum_Map(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i, x in enumerate(nums):
            delta = target - x
            if delta in seen:
                return [ seen[delta], i ]
            seen[x] = i


    #   runtime: beats 80%
    def twoSum_twoPointers(self, nums: List[int], target: int) -> List[int]:
        index_lookup = [ i for i in range(len(nums)) ]
        nums, index_lookup = zip(*sorted(zip(nums, index_lookup)))
        l = 0
        r = len(nums)-1
        while l < r:
            temp = nums[l] + nums[r]
            if temp == target:
                break
            elif temp < target:
                l += 1
            else:
                r -= 1
        return [ index_lookup[l], index_lookup[r] ]


s = Solution()
test_functions = [ s.twoSum_naive, s.twoSum_Map, s.twoSum_twoPointers, ]

input_values = [ ([2,7,11,15], 9), ([3,2,4], 6), ([3,3], 6), ]
result_valiation = [ [0,1], [1,2], [0,1], ]
assert len(input_values) == len(result_valiation)

for f in test_functions:
    print(f.__name__)
    for (nums, target), check in zip(input_values, result_valiation):
        print("nums=(%s), target=(%s)" % (nums, target))
        result = f(nums, target)
        print("result=(%s)" % result)
        assert result == check
    print()

