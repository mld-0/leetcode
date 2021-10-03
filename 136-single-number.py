#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
from collections import Counter
from typing import List
#   {{{2

class Solution:

    def singleNumber(self, nums: List[int]) -> int:
        """Return whichever element in 'nums' only appears once, (all other elements appear twice)"""
        return self.singleNumber_xor(nums)


    #   runtime: beats 73%
    def singleNumber_Counter(self, nums: List[int]) -> int:
        counts = Counter(nums)
        for i in counts.keys():
            if counts[i] == 1:
                return i
        return None


    #   runtime: beats 99%
    def singleNumber_setSumDifference(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)

    
    #   runtime: beats 95%
    def singleNumber_xor(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a = a ^ i
        return a


s = Solution()

input_values = [ [2,2,1], [4,1,2,1,2], [1], ]
input_checks = [ 1, 4, 1, ]

for nums, check in zip(input_values, input_checks):
    print("nums=(%s)" % str(nums))
    result = s.singleNumber(nums)
    print("result=(%s)" % str(result))
    assert result == check, "Check failed"
    print()

