#   LINK: https://leetcode.com/problems/implement-strstr/

class Solution:

    #   runtime: beats 88%
    def strStr_naive(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


    #   runtime: beats 88%
    def strStr_sliding(self, haystack: str, needle: str) -> int:
        #if len(needle) == 0:
        #    return 0
        l = 0
        while l <= len(haystack) - len(needle):
            if haystack[l:l+len(needle)] == needle:
                return l
            l += 1
        return -1


s = Solution()
test_functions = [ s.strStr_naive, s.strStr_sliding, ]

input_values = [ ("hello", "ll"), ("aaaaa", "bba"), ("hello", ""), ("a", "a"), ]
input_checks = [ 2, -1, 0, 0, ]
assert len(input_values) == len(input_checks)

for test_func in test_functions:
    print(test_func.__name__)
    for (haystack, needle), check in zip(input_values, input_checks):
        print("haystack=(%s), needle=(%s)" % (haystack, needle))
        result = test_func(haystack, needle)
        print("result=(%s)" % result)
        assert result == check
    print()

