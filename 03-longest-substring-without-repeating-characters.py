from collections import defaultdict
import functools

class Solution:

    def no_repeating_characters(self, s: str) -> bool:
        charset = set(s)
        if len(charset) != len(s):
            return False
        return True

    def lengthOfLongestSubstring(self, s: str) -> int:
        return self.lengthOfLongestSubstring_B(s)

    #   Sliding window algorithm: 
    #   runtime: beats 20%
    # LINK: https://levelup.gitconnected.com/an-introduction-to-sliding-window-algorithms-5533c4fe1cc7
    def lengthOfLongestSubstring_A(self, s: str) -> int:
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


    #   runtime: beats 5%
    def lengthOfLongestSubstring_BruteForce(self, s: str) -> int:
        longest = ""
        for i, val_i in enumerate(s):
            for j in range(i, len(s)+1):
                if self.no_repeating_characters(s[i:j]):
                    if len(s[i:j]) > len(longest):
                        longest = s[i:j]
                else:
                    break
        return len(longest)

    #   runtime: beats 71%
    def lengthOfLongestSubstring_B(self, s: str) -> int:
        result = ""
        l = 0
        #   position at which character last seen
        seen = {}
        for r in range(len(s)):
            if s[r] not in seen:
                #   s[r] is not in window, grow window
                trial = s[l:r+1]
                if len(trial) > len(result):
                    result = trial
            else:
                if seen[s[r]] < l:
                    #   s[r] is not in window, grow window
                    trial = s[l:r+1]
                    if len(trial) > len(result):
                        result = trial
                else:
                    #   s[r] in window, advance 'l' past last instance of 's[r]'
                    l = seen[s[r]] + 1
            seen[s[r]] = r
        return len(result)

    #   runtime: beats 71%
    def lengthOfLongestSubstring_C(self, s: str) -> int:
        result = ""
        l = 0
        seen = dict()
        for r in range(len(s)):
            if s[r] in seen and l <= seen[s[r]]:
                l = seen[s[r]] + 1
            else:
                trial = s[l:r+1]
                if len(trial) > len(result):
                    result = trial
            seen[s[r]] = r
        return len(result)

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


