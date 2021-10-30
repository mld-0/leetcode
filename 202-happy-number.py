#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
#   Problem: A number is happy if the following process results in 1: replace the number with the sum of the square of its digits
#   {{{2
class Solution:

    #   runtime: beats 89%
    def isHappy_Set(self, n: int) -> bool:
        """Determine whether 'n' becomes 1 when iteratively replaced by the sum of its digits squared, or cycles endlessly"""
        history = set()

        def digits_square_sum(n):
            """Given a number, return the sum of the square of its digits"""
            result = 0
            n_str = str(n)
            for d in n_str:
                result += int(d)**2
            return result

        while n > 1:
            n = digits_square_sum(n)
            if n in history:
                return False
            history.add(n)

        return True

    
    def isHappy_FloydCycleFinding(self, n: int) -> bool:
        """Determine whether 'n' becomes 1 when iteratively replaced by the sum of its digits squared, or cycles endlessly"""

        def digits_square_sum(n):
            """Given a number, return the sum of the square of its digits"""
            result = 0
            n_str = str(n)
            for d in n_str:
                result += int(d)**2
            return result

        slow_runner = n
        fast_runner = digits_square_sum(n)

        while fast_runner > 1 and slow_runner != fast_runner:
            slow_runner = digits_square_sum(slow_runner)
            fast_runner = digits_square_sum(fast_runner)
            fast_runner = digits_square_sum(fast_runner)

        if fast_runner == 1:
            return True
        else:
            return False


s = Solution()
test_functions = [ s.isHappy_Set, s.isHappy_FloydCycleFinding, ]

input_values = [ 19, 2, ]
input_checks = [ True, False, ]

for test_func in test_functions:
    print(test_func.__name__)
    for n, check in zip(input_values, input_checks):
        print("n=(%s)" % n)
        result = test_func(n)
        print("result=(%s)" % result)
        assert result == check, "Check comparison failed"
    print()

