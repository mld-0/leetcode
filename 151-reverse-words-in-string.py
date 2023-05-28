import time
import copy
from collections import deque
from typing import List

class Solution:

    #   runtime: beats 70%
    def reverseWords_pythonic_i(self, s: str) -> str:
        return ' '.join(s.split()[::-1])


    #   runtime: beats 73%
    def reverseWords_pythonic_ii(self, s: str) -> str:
        return ' '.join(reversed(s.split()))


    #   runtime: beats 6%
    def reverseWords_twoPointers_inPlace(self, s: str) -> str:

        def lstrip(c: List[str]):
            """Move leading whitespace to end"""
            l = 0
            while l < len(c)-1 and c[l] == ' ':
                l += 1
            r = len(c) - 1
            while r > 0 and c[r] == ' ':
                r -= 1
            c[:len(c)-l] = c[l:len(c)]
            c[len(c)-l:len(c)] = [ ' ' for _ in range(len(c)-l, len(c)) ]

        def reverse_words(c: List[str]):
            """Reverse each word in place, removing multiple spaces"""
            l = 0
            r = 0
            r_previous = r
            #   reverse each word in the string
            while l < len(c):
                #   Find the start of the next word
                while l < len(c) and c[l] == ' ':
                    l += 1
                #   Find the end of that word
                r = l
                while r < len(c) and c[r] != ' ':
                    r += 1
                #   Find the end of the previous word
                r_previous = l - 1
                while r_previous >= 0 and c[r_previous] == ' ':
                    r_previous -= 1
                if l == 0:
                    r_previous = -2
                #   reverse the current word, placing it 1 space after the end of the previous word and moving any additional spaces to the end
                start = r_previous + 2
                c[start:start+r-l] = c[l:r][::-1]
                c[start+r-l:r] = [ ' ' for _ in range(start+r-l, r) ]
                l = r + 1

        def reverse_string(c: List[str]):
            """Reverse list-of-characters in-place"""
            c[:] = c[:][::-1]

        def rend(c: List[str]) -> int:
            """Get the location of the last whitespace"""
            if c[-1] != ' ':
                return len(c)
            r = len(c) - 1
            while r > 0 and c[r] == ' ':
                r -= 1
            return r + 1

        c = list(s)
        reverse_words(c)
        reverse_string(c)
        lstrip(c)
        r = rend(c)
        return ''.join(c[:r])


s = Solution()
test_functions = [ s.reverseWords_pythonic_i, s.reverseWords_pythonic_ii, s.reverseWords_twoPointers_inPlace, ]

inputs = [ "  hello world  ", "the sky is blue", "a good   example", "The black-and-yellow broadbill Eurylaimus ochromalus is a species of bird in the typical broadbill family Eurylaimidae. A small, distinctive species, it has a black head, breastband, and upperparts, a white neckband, yellow streaking on the back and wings, and vinous-pink underparts that turn yellow towards the belly. The beak is bright blue, with a green tip to the upper mandible and black edges. It shows some sexual dimorphism, with the black breastband being incomplete in females", ]
checks = [ "world hello", "blue is sky the", "example good a", "females in incomplete being breastband black the with dimorphism, sexual some shows It edges. black and mandible upper the to tip green a with blue, bright is beak The belly. the towards yellow turn that underparts vinous-pink and wings, and back the on streaking yellow neckband, white a upperparts, and breastband, head, black a has it species, distinctive small, A Eurylaimidae. family broadbill typical the in bird of species a is ochromalus Eurylaimus broadbill black-and-yellow The", ]
assert len(inputs) == len(checks)


for f in test_functions:
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

