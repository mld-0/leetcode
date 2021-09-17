
class Solution:

    def sortedSquares(self, nums: list[int]) -> list[int]:
        #return self.sortedSquares_naive(nums)
        return self.sortedSquares_twoPointers(nums)


    #   Result:
    #       runtime: beats 40%
    def sortedSquares_naive(self, nums: list[int]) -> list[int]:
        return sorted( [ x**2 for x in nums ] )


    def sortedSquares_twoPointers(self, nums: list[int]) -> list[int]:
        result = [ None for x in nums ]

        #   set l/r to start/end of nums
        l = 0
        r = len(nums) - 1

        #   Fill result from largest->smallest value, chosing between and advancing l/r pointers at each stage
        for i in range(len(nums)-1, -1, -1):
            if abs(nums[l]) > abs(nums[r]):
                result[i] = nums[l] ** 2
                l += 1
            else:
                result[i] = nums[r] ** 2
                r -= 1

        return result




s = Solution()

input_values = [ [-4,-1,0,3,10], [-7,-3,2,3,11] ]
input_check = [ [0,1,9,16,100], [4,9,9,49,121] ]

for nums, check in zip(input_values, input_check):
    result = s.sortedSquares(nums)
    print("result=(%s)" % str(result))
    assert( result == check )
    print()

