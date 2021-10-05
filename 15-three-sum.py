#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
from typing import List
import functools

class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """Given a list of integers, nums, return all triplets (nums[i],nums[j],nums[j]) such that i != j != k and nums[i]+nums[j]+nums[k] == 0"""
        return self.threeSum_usingHashTwoSum(nums)


    #   runtime: beats 87%
    def threeSum_usingTwoPointersTwoSum(self, nums: List[int]) -> List[List[int]]:
        """Solve three-sum by solving two-sum for each element"""
        result = []
        #   two pointers approach requires 'nums' be sorted
        nums = sorted(nums)

        def twoSum_twoPointers(nums: List[int], target_index: int):
            """Find pairs of values, a,b, in 'nums[target_index+1:]' which add to value at 'target_index', and append [target, a, b] to 'result'"""
            l = target_index + 1
            r = len(nums) - 1
            while l < r:
                trial = nums[target_index] + nums[l] + nums[r]
                if trial == 0:
                    #   not sorting result triplets?
                    result.append( [nums[target_index], nums[l], nums[r] ] )
                    #   avoid duplicates:
                    while l < r and nums[l] == nums[l+1]: l += 1
                    while l < r and nums[r] == nums[r-1]: r -= 1
                    l += 1
                    r -= 1
                elif trial < 0:
                    l += 1
                elif trial > 0:
                    r -= 1

        #   for each element, solving using two-sum with that element as target
        #   need at least 2 elements after 'i' to find any results
        for i in range(len(nums)-2):
            #   skip duplicate
            if i > 0 and nums[i] == nums[i-1]:
                continue
            #   remaining values are positive and cannot sum to zero
            if nums[i] > 0:
                break
            twoSum_twoPointers(nums, i)

        return result


    #   runtime: beats 55%
    def threeSum_usingHashTwoSum(self, nums: List[int]):
        """Solve three-sum by solving two-sum for each element"""
        result = []
        #   two pointers approach requires 'nums' be sorted
        nums = sorted(nums)

        def twoSum_Hash(nums: List[int], target_index: int):
            """Find pairs of values, a,b, in 'nums[target_index+1:]' which add to value at 'target_index', and appending [target, a, b] to 'result'"""
            target = -1 * nums[target_index]
            #   describes index at which each previously seen value is found
            value_to_index = dict()
            i = target_index + 1
            while i < len(nums):
                delta = target - nums[i]
                if delta in value_to_index.keys():
                    result.append( [nums[target_index], nums[value_to_index[delta]], nums[i]] )
                    while i+1 < len(nums) and nums[i] == nums[i+1]: i += 1
                value_to_index[nums[i]] = i
                i += 1

        #   for each element, solving using two-sum with that element as target
        #   need at least 2 elements after 'i' to find any results
        for i in range(len(nums)-2):
            #   skip duplicate
            if i > 0 and nums[i] == nums[i-1]:
                continue
            #   remaining values are positive and cannot sum to zero
            if nums[i] > 0:
                break
            twoSum_Hash(nums, i)

        return result


    def threeSum_NoSorting(self, nums: List[int]) -> List[List[int]]:
        raise NotImplementedError()


    #   runtime: TLE
    def threeSum_bruteForce(self, nums):
        import itertools
        result = []
        for loop_combination in itertools.combinations(nums, 3):
            if sum(loop_combination) == 0:
                loop_combination = list(sorted(loop_combination))
                if not loop_combination in result:
                    result.append(loop_combination)
        return result


s = Solution()

nums = [ -1,0,1,2,-1,-4 ]
check = [ [-1,-1,2], [-1,0,1] ]
result = s.threeSum(nums)
print("nums=(%s)" % str(nums))
print("result=(%s)" % str(result))
#assert( result == check )
assert( all( [ x in check for x in result ] ) )
assert( all( [ x in result for x in check ] ) )

nums = []
check = []
result = s.threeSum(nums)
print("nums=(%s)" % str(nums))
print("result=(%s)" % str(result))
assert( all( [ x in check for x in result ] ) )
assert( all( [ x in result for x in check ] ) )

nums = [0]
check = []
result = s.threeSum(nums)
print("nums=(%s)" % str(nums))
print("result=(%s)" % str(result))
assert( all( [ x in check for x in result ] ) )
assert( all( [ x in result for x in check ] ) )

nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
check = [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]
result = s.threeSum(nums)
print("nums=(%s)" % str(nums))
print("result=(%s)" % str(result))
assert( all( [ x in check for x in result ] ) )
assert( all( [ x in result for x in check ] ) )

#
#result = s.threeSum(nums)
#print("nums=(%s)" % str(nums))
#print("result=(%s)" % str(result))
#
