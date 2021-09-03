import itertools

class Solution:

    #   Result:
    #       runtime: time limit exceded
    def threeSum_A(self, nums):
        result = []
        for loop_combination in itertools.combinations(nums, 3):
            if sum(loop_combination) == 0:
                loop_combination = list(sorted(loop_combination))
                if not loop_combination in result:
                    result.append(loop_combination)
        return result


    #   Given a list of integers, nums, return all triplets (nums[i],nums[j],nums[j]) such that i != j != k and nums[i]+nums[j]+nums[k] == 0
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        return self.threeSum_A(nums)


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

