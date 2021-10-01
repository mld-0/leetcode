
#   bitwise tricks:
#       (n & (-n)) isolates the rightmost bit of n
#       (n & (n-1)) sets rightmost bit of n to 0

class Solution:

    def isPowerOfTwo(self, n: int) -> bool:
        #return self.isPowerOfTwo_naive(n)
        #return self.isPowerOfTwo_bitshift(n)
        #return self.isPowerOfTwo_singlebit(n)
        return self.isPowerOfTwo_invertRightmost(n)

    #   runtime: beats 98%
    def isPowerOfTwo_naive(self, n: int) -> bool:
        if n <= 0:
            return False
        n = abs(n)
        while n > 1:
            rem = n % 2
            n = n // 2
            if rem != 0:
                return False
        return True

    #   runtime: beats 48%
    def isPowerOfTwo_bitshift(self, n: int) -> bool:
        if n <= 0:
            return False
        n = abs(n)
        while n > 1:
            rem = n & 0b0001    # mod 2
            n = n >> 1          # div 2
            if rem != 0:
                return False
        return True

    #   runtime: beats 72%
    def isPowerOfTwo_checkRightmost(self, n: int) -> bool:
        if n <= 0:
            return False
        return (n & (-n)) == n

    #   runtime: beats 47%
    def isPowerOfTwo_invertRightmost(self, n: int) -> bool:
        if n <= 0:
            return False
        return (n & (n-1)) == 0


s = Solution()

input_values = [ 1, 16, 3, 4, 5, 0, ]
input_checks = [ True, True, False, True, False, False, ]

for n, check in zip(input_values, input_checks):
    print("n=(%s)" % str(n))
    result = s.isPowerOfTwo(n)
    print("result=(%s)" % str(result))
    assert result == check, "Check failed"
    print()

