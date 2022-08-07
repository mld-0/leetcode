#   https://leetcode.com/problems/length-of-last-word/

class Solution:

    def lengthOfLastWord_twoPointers(self, s: str) -> int:
        def is_whitespace(x):
            return x == ' '
        #   Search for last space
        l = len(s)-1
        while is_whitespace(s[l]):
            l -= 1
        r = l
        while l >= 0:
            if is_whitespace(s[l]):
                return r - l
            l -= 1

        return r + 1


    def lengthOfLastWord_naive(self, s: str) -> int:
        raise NotImplementedError()


s = Solution()
test_functions = [ s.lengthOfLastWord_twoPointers, ]

input_values = [ "Hello World", "   fly me   to   the moon  ", "luffy is still joyboy", "asdf", "a bc, d", " a", ]
input_checks = [ 5, 4, 6, 4, 1, 1, ]
assert len(input_values) == len(input_checks)

for test_func in test_functions:
    print(test_func.__name__)
    for s, check in zip(input_values, input_checks):
        print("s=(%s)" % s)
        result = test_func(s)
        print("result=(%s)" % result)
        assert result == check
    print()

