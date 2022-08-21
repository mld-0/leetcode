from typing import List

class Solution:

    #   runtime: beats 98%
    def plusOne_naive(self, digits: List[int]) -> List[int]:
        digits = [ str(x) for x in digits ]
        digits = int(''.join(digits)) 
        result = [ int(x) for x in str(digits+1) ]
        return result



s = Solution()
test_functions = [ s.plusOne_naive, ]

input_values = [ [1,2,3], [4,3,2,1], [9], ]
input_checks = [ [1,2,4], [4,3,2,2], [1,0], ]
assert len(input_values) == len(input_checks)

for f in test_functions:
    for digits, check in zip(input_values, input_checks):
        print("digits=(%s)" % digits)
        result = f(digits)
        print("result=(%s)" % result)
        assert check == result, "Check failed"
    print()

