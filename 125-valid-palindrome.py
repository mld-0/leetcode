import time

class Solution:

    #   runtime: beats 89%
    def isPalindrome_pythonic(self, s: str) -> bool:
        s = [ x for x in s.lower() if x.isalnum() ]
        return s == s[::-1]


    #   runtime: beats 65%
    def isPalindrome_twoPointers(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


s = Solution()
test_functions = [ s.isPalindrome_pythonic, s.isPalindrome_twoPointers, ]

inputs = [ "A man, a plan, a canal: Panama", "race a car", " ", "abcdefghijklmnopqurstuvwxyzzyxwvutsruqponmlkjihgfedcba", "1234567890abcdefghijklmnopqrstuvwxyzzyxwvuts rqponmlkjihgfedcba09876543211234567890abcdefghijklm nopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba0987654321", "Sentence spacing is the horizontal space between sentences in typeset text. It is a matter of typographical convention. Since the introduction of movable-type printing in Europe, various sentence spacing conventions have been used in languages with a Latin-derived alphabet. These include a normal word space (as between the words in a sentence), a single enlarged space, two full spaces, and, most recently in digital media, no space. Although modern digital fonts can automatically adjust a single word space to create visually pleasing and consistent spacing following terminal punctuation, most debate is about whether to strike a keyboard's spacebar once or twice between sentences.", ]
checks = [ True, False, True, True, True, False, ]
assert len(inputs) == len(checks)

for f in test_functions:
    print(f.__name__)
    startTime = time.time()
    for value, check in zip(inputs, checks):
        print(f"value=({value})")
        result = f(value)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_ms=(%0.2f)" % ((time.time() - startTime) * 1000000))
    print()

