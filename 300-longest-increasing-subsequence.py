#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
from typing import List
import math
import bisect
#   {{{2
class Solution:

    #   runtime: TLE
    def lengthOfLIS_BruteForce(self, nums: List[int]) -> int:

        def check_all_subsequences(values):
            result = 0
            all_subsequences = get_all_subsequences(values)
            for subseq in all_subsequences:
                if is_increasing(subseq):
                    result = max(result, len(subseq))
            return result

        def get_all_subsequences(values):
            values = values[::-1]
            result = []
            for i in range(1, 2**len(values)):
                bits = list(bin(i)[2:])
                loop_combination = []
                for j, bit in enumerate(bits):
                    if bit == '1':
                        loop_combination.append( values[j] )
                loop_combination = loop_combination[::-1]
                result.append(loop_combination)
            return result

        def is_increasing(values):
            for i in range(1, len(values)):
                if values[i] <= values[i-1]:
                    return False
            return True

        longest = 0
        for l in range(len(nums)):
            for r in range(l, len(nums)):
                trial = check_all_subsequences(nums[l:r+1])
                if trial > longest:
                    longest = trial

        return longest


    #   runtime: beats 35%
    def lengthOfLIS_DP(self, nums: List[int]) -> int:
        #   table[i]: lengthOfLIS for nums[:i]
        table = [ 1 for x in range(len(nums)) ]

        for r in range(1, len(nums)):
            for l in range(r):
                if nums[r] > nums[l]:
                    table[r] = max(table[r], table[l] + 1)

        return max(table)

    
    #   runtime: beats 98%
    def lengthOfLIS_BuildSubseq(self, nums: List[int]) -> int:
        subseq_increasing = [ nums[0] ]

        for n in nums[1:]:
            if n > subseq_increasing[-1]:
                subseq_increasing.append(n)
            else:
                #   replace last element in subseq_increasing that is smaller than 'n' 
                i = bisect.bisect_left(subseq_increasing, n)
                subseq_increasing[i] = n

        return len(subseq_increasing)


s = Solution()
test_functions = [ s.lengthOfLIS_BruteForce, s.lengthOfLIS_BuildSubseq, s.lengthOfLIS_DP, ]

input_values = [ [10,9,2,5,3,7,101,18], [0,1,0,3,2,3], [7,7,7,7,7,7,7], [1,3,6,7,9,4,10,5,6], ]
input_checks = [ 4, 4, 1, 6, ]

for test_func in test_functions:
    print(test_func.__name__)
    for nums, check in zip(input_values, input_checks):
        print("nums=(%s)" % nums)
        result = test_func(nums)
        print("result=(%s)" % result)
        assert result == check, "Check comparison failed"
    print()

