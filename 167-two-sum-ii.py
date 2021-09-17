
class Solution:

    #   runtime: beats 96%
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """Find the indexes (1-indexed) of values in sorted list 'numbers' which add to 'target'"""
        l = 0
        r = len(numbers) - 1
        while l < r:
            trial = numbers[l] + numbers[r]
            if trial == target:
                return [l+1, r+1]
            elif trial < target:
                l += 1
            elif trial > target:
                r -= 1


input_values = [ ([2,7,11,15], 9), ([2,3,4], 6), ([-1,0], -1), ]
input_checks = [ [1,2], [1,3], [1,2] ]

s = Solution()

for (numbers, target), check in zip(input_values, input_checks):
    assert( numbers == sorted(numbers) )
    result = s.twoSum(numbers, target)
    print("result=(%s)" % str(result))
    assert( result == check )
    print()

