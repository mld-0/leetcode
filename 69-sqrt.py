#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
#   Ongoing: 2022-09-02T22:01:35AEST mySqrt_ExpLog can handle much large values without needing l/r than mySqrt_Recursive

#   Find the sqrt of non-negative integer x with decimal digits truncated, without using 'pow' or '**'
class Solution:

    #   runtime: beats 9%
    def mySqrt_iterative(self, x: int) -> int:
        i = 1
        j = 0
        while (i * i <= x):
            j = i
            i += 1
        return j


    #   runtime: beats 93%
    def mySqrt_BinarySearch(self, x: int) -> int:
        if x <= 1:
            return x
        l = 2
        r = x // 2       
        while l <= r:
            mid = l + (r - l) // 2
            temp = mid * mid
            if temp == x:
                return mid
            elif temp < x:
                l = mid + 1
            elif temp > x:
                r = mid - 1
        return r


    #   runtime: beats 87%
    def mySqrt_ExpLog(self, x: int) -> int:
        """sqrt(x) = exp(0.5*ln(x))"""
        import math
        if x <= 1:
            return x
        l = int(math.exp(0.5 * math.log(x)))
        r = l + 1
        if r*r <= x:
            return r
        return l


    #   runtime: beats 93%
    def mySqrt_Recursive(self, x: int) -> int:
        """sqrt(x) = 2*sqrt(x/4), x<<y = x*2**y, x>>y = x/2**y"""
        if x <= 1:
            return x
        l = self.mySqrt_Recursive(x>>2) << 1
        r = l + 1
        if r*r <= x:
            return r
        return l


s = Solution()
test_functions = [ s.mySqrt_iterative, s.mySqrt_ExpLog, s.mySqrt_Recursive, s.mySqrt_BinarySearch, ]

input_values = [ 4, 8, 0, 9, 100000, 1, 2147395600, ]
expected_result = [ 2, 2, 0, 3, 316, 1, 46340, ]

for f in test_functions:
    print(f.__name__)
    for x, check in zip(input_values, expected_result):
        print("x=(%s)" % x)
        result = f(x)
        print("result=(%s)" % result)
        assert result == check, "Check comparison failed"
    print()

