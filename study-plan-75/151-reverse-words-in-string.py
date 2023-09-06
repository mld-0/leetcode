#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import sys
import time
import copy
from typing import List

class Solution:

    #   runtime: beats 92%
    def reverseWords_pythonic(self, s: str) -> str:
        return ' '.join(reversed(s.split()))


    #   incorrect:
    def reverseWords_inPlace(self, s: str) -> str:

        #   {{{
        #def lstrip_inplace(s: List[str], start: int=0):
        #    l = start
        #    while l < len(s)-1 and s[l] == ' ':
        #        l += 1
        #    print("lstrip, before: s=(%s)" % s)
        #    for i in range(start, len(s)):
        #        print(i)
        #        if i+l <= len(s)-1:
        #            s[i] = s[i+l]
        #        else:
        #            s[i] = ' '
        #    print("lstrip, after: s=(%s)" % s)
        #   }}}

        def lstrip_inplace(s: List[str], start: int=0):
            l = start
            while l < len(s) and s[l] == ' ':
                l += 1 
            shift = l - start
            if shift > 0:
                for i in range(start, len(s) - shift):
                    s[i] = s[i + shift]
                for i in range(len(s) - shift, len(s)):
                    s[i] = ' ' 

        def remove_multiple_spaces_inplace(s: List[str], start: int=0):
            l = start
            while l < len(s) - 1:
                #   find start of next word:
                while l < len(s) - 1 and s[l] == ' ':
                    l += 1
                if l == len(s) - 1:
                    break
                #   find end of current word
                r = l
                while r < len(s)-2 and s[r+1] != ' ':
                    r += 1
                #   find start of next word
                l = r + 1
                while l < len(s)-2 and s[l+1] == ' ':
                    l += 1
                #   no more words
                if l >= len(s)-2:
                    break
                if l - r > 1:
                    lstrip_inplace(s, l-1)
                    remove_multiple_spaces_inplace(s, l-1)
                    return

        def reverse_words_inplace(s: List[str]):
            l = 0
            r = 0
            while r < len(s) - 1:
                #   find start of next word
                while l < len(s)-1 and s[l] == ' ':
                    l += 1
                #   no more words
                if l == len(s) - 1:
                    break
                #   find end of next word:
                r = l
                while r <= len(s)-2 and s[r+1] != ' ':
                    r += 1
                #   reverse word in-place
                L = l
                R = r
                while L < R:
                    s[L], s[R] = s[R], s[L]
                    L += 1
                    R -= 1
                l = r + 1

        def reverse_string_inplace(s: List[str]):
            s[:] = s[::-1]

        def find_rend(s: List[str]) -> int:
            r = len(s) - 1
            while r >= 0 and s[r] == ' ':
                r -= 1
            return r


        s = [ c for c in s ]
        remove_multiple_spaces_inplace(s)
        reverse_words_inplace(s)
        reverse_string_inplace(s)
        lstrip_inplace(s)
        r = find_rend(s)
        return ''.join(s[:r+1])
    


s = Solution()
functions = [ s.reverseWords_pythonic, s.reverseWords_inPlace, ]

inputs = [ "  hello world  ", "the sky is blue", "a good   example", "The black-and-yellow broadbill Eurylaimus ochromalus is a species of bird in the typical broadbill family Eurylaimidae. A small, distinctive species, it has a black head, breastband, and upperparts, a white neckband, yellow streaking on the back and wings, and vinous-pink underparts that turn yellow towards the belly. The beak is bright blue, with a green tip to the upper mandible and black edges. It shows some sexual dimorphism, with the black breastband being incomplete in females", "  Bob    Loves  Alice   ", ]
checks = [ "world hello", "blue is sky the", "example good a", "females in incomplete being breastband black the with dimorphism, sexual some shows It edges. black and mandible upper the to tip green a with blue, bright is beak The belly. the towards yellow turn that underparts vinous-pink and wings, and back the on streaking yellow neckband, white a upperparts, and breastband, head, black a has it species, distinctive small, A Eurylaimidae. family broadbill typical the in bird of species a is ochromalus Eurylaimus broadbill black-and-yellow The", "Alice Loves Bob", ]
assert len(inputs) == len(checks)

for f in functions:
    inputs_copy = copy.deepcopy(inputs)
    print(f.__name__)
    startTime = time.time()
    for s, check in zip(inputs_copy, checks):
        print(f"s=({s})")
        result = f(s)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_ms=(%0.2f)" % ((time.time() - startTime) * 1000000))
    print()

