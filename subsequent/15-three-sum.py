from typing import List

class Solution:

    #   runtime: beats 41%
    def threeSum_usingTwoSumMap(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = set()

        def twoSum_Map(index: int):
            target = -1 * nums[index]
            seen = dict()
            for i in range(index+1, len(nums)):
                x = nums[i]
                if i == index:
                    continue
                delta = target - x
                if delta in seen:
                    result.add(tuple(sorted( [ nums[index], delta, x ] )))
                seen[x] = i

        for i, x in enumerate(nums):
            #   skip duplicates:
            if i > 0 and nums[i] == nums[i-1]:
                continue
            #   remaining values are positive, we cannot sum to zero
            if nums[i] > 0:
                break
            twoSum_Map(i)
        return sorted( [ list(x) for x in result ] )

    
    #   runtime: beats 54%
    def threeSum_usingTwoSumTwoPointers(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = set()

        def twoSum_twoPointers(index: int):
            target = -1 * nums[index]
            l = index + 1
            r = len(nums) - 1
            while l < r:
                trial = nums[l] + nums[r]
                if trial == target:
                    result.add(tuple(sorted( [ nums[index], nums[l], nums[r] ] )))
                    #   skip duplicates
                    while l < r and nums[l] == nums[l+1]: l += 1
                    while l < r and nums[r] == nums[r-1]: r -= 1
                    l += 1
                    r -= 1
                elif trial < target:
                    l += 1
                elif trial > target:
                    r -= 1

        for i, x in enumerate(nums):
            #   skip duplicates:
            if i > 0 and nums[i] == nums[i-1]:
                continue
            #   remaining values are positive, we cannot sum to zero
            if nums[i] > 0:
                break
            twoSum_twoPointers(i)
        return sorted( [ list(x) for x in result ] )


    #   avoid sorting input
    #   runtime: beats 54%
    def threeSum_iv(self, nums: List[int]) -> List[List[int]]:
        result = set()
        skip_duplicates = set()
        for i, x in enumerate(nums):
            if x in skip_duplicates: 
                continue
            skip_duplicates.add(x)
            seen = dict()
            for j in range(i+1, len(nums)):
                y = nums[j]
                trial = -1 * (x + y)
                if trial in seen:
                    result.add(tuple(sorted( [x,y,trial] )))
                seen[y] = j
        return sorted( [ list(x) for x in result ] )




s = Solution()
test_functions = [ s.threeSum_usingTwoSumMap, s.threeSum_usingTwoSumTwoPointers, s.threeSum_iv, ]

input_values = [ [ -1,0,1,2,-1,-4 ], [], [0], [-1,0,1,2,-1,-4,-2,-3,3,0,4], ]
result_validation =  [ [ [-1,-1,2], [-1,0,1] ], [], [], [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]], ]
assert len(input_values) == len(result_validation)

for f in test_functions:
    print(f.__name__)
    for nums, check in zip(input_values, result_validation):
        print("nums=(%s)" % nums)
        result = f(nums)
        print("result=(%s)" % result)
        assert all( [ x in check for x in result ] ), "Check failed i"
        assert all( [ x in result for x in check ] ), "Check failed ii"
    print()

