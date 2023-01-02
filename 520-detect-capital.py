#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2

class Solution:

    #   runtime: beats 95%
    def detectCapitalUse(self, word: str) -> bool:
        is_cap = [ x.isupper() for x in word ]
        if all(is_cap):
            return True
        if not any(is_cap[1:]):
            return True
        return False


s = Solution()
functions = [ s.detectCapitalUse, ]

inputs = [ "USA", "FlaG", "leetcode", "Google", ]
checks = [ True, False, True, True, ]
assert len(inputs) == len(checks)

for f in functions:
    print(f.__name__)
    for (word, check) in zip(inputs, checks):
        print(f"word=({word})")
        result = f(word)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print()

