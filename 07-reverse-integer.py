
class Solution:
    #   Result:
    #       runtime: 24ms (beats 70%)
    def reverse(self, x: int) -> int:
        signof = 1
        if x < 0:
            signof = -1
        x = signof * int(str(abs(x))[::-1])
        if x > 2**31 - 1 or x < -2**31:
            return 0
        return x
        
s = Solution()
val = 93532
result = s.reverse(val)
print(result)
