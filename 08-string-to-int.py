import re

#   Results:
#       runtime: 36ms (beats 57%)
#       memory: 14.3MB (beats 58%)
class Solution:
    def myAtoi(self, s: str) -> int:
        re_result = re.match("^\s*([+-]?\d+)\D*", s)
        if not re_result:
            return 0
        s = re_result.group(1)
        result = int(s)
        if (result > pow(2, 31) - 1):
            result = pow(2, 31) - 1
        if (result < pow(-2, 31)):
            result = pow(-2, 31)
        return result

s = Solution()
result = s.myAtoi("   -42")
print(result)
assert(result == -42)

result = s.myAtoi("4193 with whitespace")
print(result)
assert(result == 4193)

result = s.myAtoi("words and 987")
print(result)
assert(result == 0)


