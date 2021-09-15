
#   Note that result indexes are 1-indexed

class Solution:
    #   Result:
    #       runtime: beats 96%
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i = 0
        j = len(numbers)-1
        while i < j:
            trial = numbers[i] + numbers[j]
            if trial == target:
                return (i+1, j+1)
            elif trial < target:
                i += 1
            elif trial > target:
                j -= 1


nums_targets_list = [ ([2,7,11,15], 9), ([2,3,4], 6), ([-1,0], -1) ]
check_list = [ (1,2), (1,3), (1,2) ]

s = Solution()

for (nums, target), check in zip(nums_targets_list, check_list):
    result = s.twoSum(nums, target)
    print("nums=(%s), target=(%s)" % (str(nums), str(target)))
    print("result=(%s)" % str(result))
    print()
    assert( result == check )

