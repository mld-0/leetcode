#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
#   {{{2
class Solution:

    #   runtime: TLE
    def rangeBitwiseAnd_i(self, left: int, right: int) -> int:
        result = left
        for i in range(left+1, right+1):
            result &= i
        return result

    
    #   runtime: beats 90%
    def rangeBitwiseAnd_ii(self, left: int, right: int) -> int:
        """Find the 'common prefix' of the binary numbers between 'left' and 'right'"""
        #   how many right shifts until 'left' and 'right' are equal
        i = 0
        while left != right:
            left = left >> 1
            right = right >> 1
            i += 1
        #   shift back left to obtain the binary common prefix
        return left << i


    #   runtime: beats 99%
    def rangeBitwiseAnd_iii(self, left: int, right: int) -> int:
        """Find the 'common prefix' of the binary numbers between 'left' and 'right'"""
        while left < right:
            right = right & (right - 1)
        return right


s = Solution()
test_functions = [ s.rangeBitwiseAnd_ii, s.rangeBitwiseAnd_iii, ]

input_values = [ (5,7), (0,0), (1,2147483647), ]
input_checks = [ 4, 0, 0, ]

for test_func in test_functions:
    print(test_func.__name__)
    for (l, r), check in zip(input_values, input_checks):
        print("l=(%s), r=(%s)" % (l, r))
        result = test_func(l, r)
        print("result=(%s)" % result)
        assert result == check, "Check comparison failed"
    print()

