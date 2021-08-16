
class Solution:

    def no_repeating_characters(self, s: str) -> bool:
        charset = set(s)
        if len(charset) != len(s):
            return False
        return True

    #   Runtime (leetcode) 4732ms (beats 5%)
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ""
        for i, val_i in enumerate(s):
            for j in range(i, len(s)+1):
                if self.no_repeating_characters(s[i:j]):
                    if len(s[i:j]) > len(longest):
                        longest = s[i:j]
                else:
                    break

        return len(longest)

val_str = "abcabcbb"
s = Solution()
result = s.lengthOfLongestSubstring(val_str)
print(result)

val_str = " "
s = Solution()
result = s.lengthOfLongestSubstring(val_str)
print(result)

