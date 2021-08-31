class Solution:

    def longestCommonPrefix_A(self, strs: list[str]) -> str:
        pass

    def longestCommonPrefix(self, strs: list[str]) -> str:
        return self.longestCommonPrefix_A(strs)


s = Solution()
strs = ["flower","flow","flight"]
result = s.longestCommonPrefix(strs)
expected = "fl"
print("result=(%s)" % str(result))
assert( result == expected )

strs = ["dog","racecar","car"]
result = s.longestCommonPrefix(strs)
expected = ""
print("result=(%s)" % str(result))
assert( result == expected )

