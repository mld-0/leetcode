#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
#   {{{2
#   Problem: How many ways can a number be decoded using the mapping A=1, B=2, ..., Z=26
class Solution:

    def numDecodings_DP_TopDown_RecursiveMemorize(self, s: str) -> int:
        memo = dict()

        def solve(index):
            if index in memo:
                return memo[index]
            #   end of string
            if index == len(s):
                memo[index] = 1
                return 1
            #   A leading zero means 's' cannot be decoded
            if s[index] == '0':
                memo[index] = 0
                return 0

            #   one non-zero digit -> one possible decoding
            if index == len(s)-1:
                memo[index] = 1
                return 1

            #   solution for single digit decoding
            count = solve(index+1)

            #   if applicable, add solution for double digit decoding
            if int(s[index:index+2]) <= 26:
                count += solve(index+2)

            memo[index] = count
            return count

        return solve(0)


    def numDecodings_DP_BottomUp_Iterative(self, s: str) -> int:
        table = [ 0 for x in range(len(s)+1) ]
        table[0] = 1

        if s[0] == '0':
            table[1] = 0
        else:
            table[1] = 1

        for i in range(2, len(table)):
            #   is single digit decode possible
            if s[i-1] != '0':
                table[i] += table[i-1]
            #   is double digit decode possible
            trial = int(s[i-2:i])
            if trial >= 10 and trial <= 26:
                table[i] += table[i-2]

        return table[-1]


s = Solution()
test_functions = [ s.numDecodings_DP_TopDown_RecursiveMemorize, s.numDecodings_DP_BottomUp_Iterative, ]

input_values = [ "12", "226", "0", "06", ]
input_checks = [ 2, 3, 0, 0, ]

for test_func in test_functions:
    print(test_func.__name__)
    for num, check in zip(input_values, input_checks):
        print("num=(%s)" % num)
        result = test_func(num)
        print("result=(%s)" % result)
        assert result == check, "Check comparison failed"
    print()

