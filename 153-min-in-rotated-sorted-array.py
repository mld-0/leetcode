import math

class Solution:

    #   invalid:
    def findMin_A(self, nums: list[int]) -> int:
        index = len(nums) // 2
        range_start = index
        while (nums[index] > nums[index-1]):
            range_end = len(nums) + range_start
            range_start = index
            index = (range_end - range_start) // 2 + range_start
            while index >= len(nums):
                index -= len(nums)
        return nums[index]


    #   Results:
    #       runtime: beats 88%
    def findMin_B(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        range_start = 0
        range_end = len(nums)
        index = (range_end - range_start + 1) // 2 + range_start
        while (nums[index] > nums[index-1]):
            if (nums[range_start] > nums[index]):
                range_end = index
            else:
                range_start = index
            index = (range_end - range_start + 1) // 2 + range_start
            while index >= len(nums):
                index -= len(nums) 
            #print("index=(%d), start=(%d), end=(%d), num=(%s)" % (index, range_start, range_end, nums[index]))
        return nums[index]


    def findMin(self, nums: list[int]) -> int:
        return self.findMin_B(nums)


s = Solution()
nums = [3,4,5,1,2]
expected = min(nums)
result = s.findMin(nums)
print("result=(%s)" % str(result))
assert(result == expected)

nums = [4,5,6,7,0,1,2]
expected = min(nums)
result = s.findMin(nums)
print("result=(%s)" % str(result))
assert(result == expected)

nums = [11,13,15,17]
expected = min(nums)
result = s.findMin(nums)
print("result=(%s)" % str(result))
assert(result == expected)

nums = [1,2]
expected = min(nums)
result = s.findMin(nums)
print("result=(%s)" % str(result))
assert(result == expected)

nums = [2,3,4,5,6,1]
expected = min(nums)
result = s.findMin(nums)
print("result=(%s)" % str(result))
assert(result == expected)

nums = [284,287,289,293,295,298,0,3,8,9,10,11,12,15,17,19,20,22,26,29,30,31,35,36,37,38,42,43,45,50,51,54,56,58,59,60,62,63,68,70,73,74,81,83,84,87,92,95,99,101,102,105,108,109,112,114,115,116,122,125,126,127,129,132,134,136,137,138,139,147,149,152,153,154,155,159,160,161,163,164,165,166,168,169,171,172,174,176,177,180,187,188,190,191,192,198,200,203,204,206,207,209,210,212,214,216,221,224,227,228,229,230,233,235,237,241,242,243,244,246,248,252,253,255,257,259,260,261,262,265,266,268,269,270,271,272,273,277,279,281]
expected = min(nums)
result = s.findMin(nums)
print("result=(%s)" % str(result))
assert(result == expected)

nums = [1]
expected = min(nums)
result = s.findMin(nums)
print("result=(%s)" % str(result))
assert(result == expected)

