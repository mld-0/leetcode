
class Solution:

    def reverseWords(self, s: str) -> str:
        """Reverse order of characters in each word"""
        #return self.reverseWords_A(s)
        return self.reverseWords_TwoPointers(s)

    #   runtime: beats 95%
    def reverseWords_SplitReverseEachJoin(self, s: str) -> str:
        """Split into words, reverse each, and join"""
        return ' '.join( [ x[::-1] for x in s.split(' ') ] )

    #   runtime: beats 86%
    def reverseWords_SplitReverseJoinReverse(self, s: str) -> str:
        """Split into words, reverse list, join, and reverse"""
        return ' '.join( s.split(' ')[::-1] )[::-1]

    #   runtime: beats 20%
    def reverseWords_TwoPointers(self, s: str) -> str:
        """Two-pointers implementation, reverse each within string"""
        l = 0  # start of current word
        r = 0  # position after end of current word
        #   For each word in the string
        while r < len(s):
            #   Advance r to end-of-current-word or end-of-string
            while r < len(s) and s[r] != ' ':
                r += 1
            #   reverse current word within s and assign result back to s
            s = s[:l] + s[l:r][::-1] + s[r:]
            #   Advance l and r to the start of next word
            r += 1
            l = r
        return s

    def reverseWords_Ans(self, s: str) -> str:
        result = ""
        l = 0
        r = 0
        while r < len(s):
            if s[r] != ' ':
                r += 1
            elif s[r] == ' ':
                result += s[l:r+1][::-1]
                r += 1
                l = r
        result += ' '
        result += s[l:r+2][::-1]
        return result[1:]

    
    #   TODO: 2021-09-17T23:28:16AEST _leetcode, 557-reverse-words-in-string-iii, reverseWords_TwoPointersInPlace
    def reverseWords_TwoPointersInPlace(self, s: str) -> str:
        pass


input_values = [ "Let's take LeetCode contest", "God Ding" ]
input_checks = [ "s'teL ekat edoCteeL tsetnoc", "doG gniD" ]

s = Solution()

for _str, check in zip(input_values, input_checks):
    result = s.reverseWords(_str)
    print("result=(%s), check=(%s)" % (str(result), str(check)))
    assert( result == check )
    print()

