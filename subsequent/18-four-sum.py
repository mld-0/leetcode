from typing import List

class Solution:

    #   runtime: beats 85%
    def fourSum_kSumTwoPointers(self, nums: List[int], target: int) -> List[List[int]]:

        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            result = []
            if len(nums) == 0:
                return result
            avg = target // k
            if nums[0] > avg or nums[-1] < avg:
                return result 
            if k == 2:
                return twoSum(nums, target)
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                partialSolutions = kSum(nums[i+1:], target-nums[i], k-1)
                for subset in partialSolutions:
                    result.append( [ nums[i], *subset ] )
            return result

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            result = []
            l = 0
            r = len(nums) - 1
            while l < r:
                trial = nums[l] + nums[r]
                if trial < target or (l > 0 and nums[l] == nums[l-1]):
                    l += 1
                elif trial > target or (r < len(nums)-1 and nums[r] == nums[r+1]):
                    r -= 1
                else:
                    result.append( [nums[l], nums[r]] )
                    l += 1
                    r -= 1
            return result

        nums = sorted(nums)
        return kSum(nums, target, 4)


    #   runtime: beats 89%
    def fourSum_kSumMap(self, nums: List[int], target: int) -> List[List[int]]:

        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            result = []
            if len(nums) == 0:
                return result
            avg = target // k
            if nums[0] > avg or nums[-1] < avg:
                return result 
            if k == 2:
                return twoSum(nums, target)
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                partialSolutions = kSum(nums[i+1:], target-nums[i], k-1)
                for subset in partialSolutions:
                    result.append( [ nums[i], *subset ] )
            return result

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            result = []
            seen = dict()
            for i, x in enumerate(nums):
                if len(result) > 0 and result[-1][1] == nums[i]:
                    continue
                delta = target - x
                if delta in seen:
                    result.append( [ delta, x ] )
                seen[x] = i
            return result

        nums = sorted(nums)
        return kSum(nums, target, 4)


s = Solution()
test_functions = [ s.fourSum_kSumTwoPointers, s.fourSum_kSumMap, ]

input_values = [ ([1,0,-1,0,-2,2], 0), ([2,2,2,2,2], 8), ([1,0,-1,0,-2,2], 0), ]
result_validation = [ [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]], [[2,2,2,2]], 
        [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]], ]
assert len(input_values) == len(result_validation)

for f in test_functions:
    print(f.__name__)
    for (nums, target), check in zip(input_values, result_validation):
        print("nums=(%s), target=(%s)" % (nums, target))
        result = f(nums, target)
        print("result=(%s)" % result)
        assert all( [ x in check for x in result ] ), "Check failed i"
        assert all( [ x in result for x in check ] ), "Check failed ii"
    print()

