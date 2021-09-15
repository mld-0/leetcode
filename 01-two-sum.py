
class Solution:

    #   Result:
    #       runtime: beats 75%
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """find the indices of the values in 'nums' that add up to 'target'"""

        #   num_to_index[nums[index]] = index
        num_to_index = dict()

        for index in range(len(nums)):
            delta = target - nums[index]

            if delta in num_to_index.keys():
                return ( num_to_index[delta], index )

            num_to_index[nums[index]] = index


nums_targets_list = [ ([2,7,11,15], 9), ([3,2,4], 6), ([3,3], 6) ]
check_list = [ (0,1), (1,2), (0,1) ]

s = Solution()

for (nums, target), check in zip(nums_targets_list, check_list):
    result = s.twoSum(nums, target)
    print("nums=(%s), target=(%s)" % (str(nums), str(target)))
    print("result=(%s)" % str(result))
    print()
    assert( result == check )

