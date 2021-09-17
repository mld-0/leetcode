
class Solution:

    def reverseString(self, s: list[str]) -> None:
        #self.reverseString_A(s)
        self.reverseString_E(s)

    #   runtime: beats 98%
    def reverseString_A(self, s: list[str]) -> None:
        s[:] = s[::-1]
    
    #   runtime: beats 80%
    def reverseString_B(self, s: list[str]) -> None:
        s.reverse()

    #   runtime: beats 30%
    def reverseString_C(self, s: list[str]) -> None:
        l = 0
        r = len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

    #   runtime: beats 52%
    def reverseString_D(self, s: list[str]) -> None:
        for i in range(len(s)//2):
            s[i], s[-i-1] = s[-i-1], s[i]

    #   runtime: beats 66%
    def reverseString_E(self, s: list[str]) -> None:
        for i in range(len(s)//2):
            s[i], s[~i] = s[~i], s[i]


#   TODO: 2021-09-17T21:51:22AEST _leetcode, 344-reverse-string, (as <to be> a format to be reused), test (and time) values/checks for each of reverseString_\w in Solution

input_values = [ ["h","e","l","l","o"], ["H","a","n","n","a","h"] ]
input_checks = [ ["o","l","l","e","h"], ["h","a","n","n","a","H"] ]

s = Solution()

for _str, check in zip(input_values, input_checks):
    s.reverseString(_str)
    print("_str=(%s)" % str(_str))
    assert( _str == check )
    print()


