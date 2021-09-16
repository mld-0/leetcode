
class Solution:

    #   Result: 
    #       runtime: beats 78%
    def searchInsert(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (r - l) // 2 + l
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1

        return l


s = Solution()

input_values = [ ([1,3,5,6], 5), ([1,3,5,6], 2), ([1,3,5,6], 7), ([1,3,5,6], 0), ([1], 0) ]
input_checks = [ 2, 1, 4, 0, 0 ]

for (nums, target), check in zip(input_values, input_checks):
    result = s.searchInsert(nums, target)
    print("result=(%s)" % str(result))
    assert( result == check )
    print()

