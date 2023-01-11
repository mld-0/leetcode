from typing import List

class Solution:

    #   runtime: beats 96%
    def findMissingRanges_i(self, nums: List[int], lower: int, upper: int) -> List[str]:
        def format_range(l: int, u: int) -> str:
            if l == u:
                return "%i" % l
            else:
                return "%i->%i" % (l, u)

        if len(nums) == 0:
            return [ format_range(lower,upper) ]

        result = []
        if nums[0] != lower:
            result.append( format_range(lower, nums[0]-1) )

        for i in range(1, len(nums)):
            l = nums[i-1]
            r = nums[i]
            if l == r:
                continue
            if l+1 == r:
                continue
            result.append( format_range(l+1, r-1) )

        if nums[-1] != upper:
            result.append( format_range(nums[-1]+1, upper) )

        return result


    #   runtime: beats 95%
    def findMissingRanges_Ans(self, nums: List[int], lower: int, upper: int) -> List[str]:
        def format_range(l: int, u: int) -> str:
            if l == u:
                return "%i" % l
            else:
                return "%i->%i" % (l, u)

        result = []
        prev = lower - 1 
        for i in range(len(nums)+1):
            if i < len(nums):
                curr = nums[i]
            else:
                curr = upper + 1
            if prev + 1 <= curr - 1:
                result.append( format_range(prev+1, curr-1) )
            prev = curr

        return result


s = Solution()
functions = [ s.findMissingRanges_i, s.findMissingRanges_Ans, ]

inputs = [ ([0,1,3,50,75],0,99), ([-1],-1,-1), ([],1,1), ]
checks = [ ["2","4->49","51->74","76->99"], [], ["1"], ]
assert len(inputs) == len(checks)

for f in functions:
    print(f.__name__)
    for (nums, lower, upper), check in zip(inputs, checks):
        print(f"nums=({nums}), lower=({lower}), upper=({upper})")
        result = f(nums, lower, upper)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print()

