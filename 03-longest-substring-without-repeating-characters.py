from collections import defaultdict
import functools

class Solution:

    def no_repeating_characters(self, s: str) -> bool:
        charset = set(s)
        if len(charset) != len(s):
            return False
        return True


    # Sliding window algorithm: 
    #   Results:
    #       runtime: 288ms (beats 20%)
    #       memory: run-dependent
    # LINK: https://levelup.gitconnected.com/an-introduction-to-sliding-window-algorithms-5533c4fe1cc7
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left, right = 0, 0
        window_counter = defaultdict(int)
        # Iterate right bound of window across s. left bounds is only iterated if duplicate char encountered
        for right in range(0, len(s)):
            window_counter[s[right]] += 1
            # If the current window contains a duplicate, increment 'left'
            if any([v > 1 for v in window_counter.values()]):
                window_counter[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest


    #   Runtime (leetcode) 4732ms (beats 5%)
    def lengthOfLongestSubstring_Brute(self, s: str) -> int:
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
#result = s.lengthOfLongestSubstring_Brute(val_str)
result = s.lengthOfLongestSubstring(val_str)
print(result)

val_str = " "
s = Solution()
#result = s.lengthOfLongestSubstring_Brute(val_str)
result = s.lengthOfLongestSubstring(val_str)
print(result)


