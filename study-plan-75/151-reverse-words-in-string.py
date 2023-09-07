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


    #   runtime: beats 5%
    def reverseWords_inPlace(self, s: str) -> str:

        def lstrip(s: List[str], start: int=0):
            """Remove leading spaces in char-array, start at `start`, shuffling contents forward as required"""
            next_word_start = start
            while next_word_start <= len(s) - 1 and s[next_word_start] == ' ':
                next_word_start += 1
            i = start
            while i < len(s):
                if i + (next_word_start-start) > len(s) - 1:
                    break
                s[i] = s[i+(next_word_start-start)]
                i += 1
            while i < len(s):
                s[i] = ' '
                i += 1

        def remove_multiple_spaces(s: List[str]):
            """Replace multiple sequential spaces (and any leading spaces) in char-array with a single space, shuffling contents forward at each stage as required."""
            word_start = 0
            word_end = -2
            previous_end = None
            while word_start < len(s) and s[word_start] == ' ':
                word_start += 1
            while word_start < len(s):
                previous_end = word_end
                word_end = word_start
                while word_end+1 < len(s) and s[word_end+1] != ' ':
                    word_end += 1
                delta = (word_start - previous_end - 1)
                if delta > 1:
                    lstrip(s, previous_end+2)
                    word_start -= (delta - 1)
                    word_end -= (delta - 1)
                word_start = word_end + 1
                while word_start < len(s) and s[word_start] == ' ':
                    word_start += 1

        def reverse_string(s: List[str], start: int=None, end: int=None):
            """Reverse elements of char-array between `start` and `end` (inclusive)"""
            if start is None:
                start = 0
            if end is None or end < 0:
                end = len(s)-1
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

        def reverse_words(s: List[str]):
            """Reverse each word in a char-array in-place."""
            word_start = 0
            word_end = 0
            while word_start < len(s) and s[word_start] == ' ':
                word_start += 1
            while word_start < len(s):
                word_end = word_start
                while word_end < len(s)-1 and s[word_end+1] != ' ':
                    word_end += 1
                reverse_string(s, word_start, word_end)
                word_start = word_end + 1
                while word_start < len(s) and s[word_start] == ' ':
                    word_start += 1

        def find_rend(s: List[str]) -> int:
            """Find index of last non-whitespace element in char-array (or -1 if there isn't one)"""
            i = len(s) - 1
            while i >= 0 and s[i] == ' ':
                i -= 1
            return i

        #   helper function tests:
        #   {{{
        def test_lstrip():
            inputs = [ ("abc ",0), (" abc skldjf ", 0), (" abc   klsdjf ", 5), ("     a      d",7), ("   a",0), ]
            checks = [ "abc ", "abc skldjf  ", " abc klsdjf   ", "     a d     ", "a   "]
            assert len(inputs) == len(checks)
            for (s, n), check in zip(inputs, checks):
                s = [ c for c in s ] 
                check = [ c for c in check ]
                lstrip(s, n)
                assert s == check

        def test_remove_multiple_spaces():
            inputs = [ "abc  klsjdf   lkjd     dksd d", "   a", " abc  klsjdf   lkjd     dksd d", "  abc  klsjdf   lkjd     dksd d", ]
            checks = [ "abc klsjdf lkjd dksd d       ", "a   ", "abc klsjdf lkjd dksd d        ", "abc klsjdf lkjd dksd d         ", ]
            assert len(inputs) == len(checks)
            for s, check in zip(inputs, checks):
                s = [ c for c in s ]
                check = [ c for c in check ]
                remove_multiple_spaces(s)
                assert s == check

        def test_reverse_string():
            inputs = [ ("abcdef",None,None), ("123abc456",3,5), ("123abc456",0,2), ]
            checks = [ "fedcba", "123cba456", "321abc456", ]
            assert len(inputs) == len(checks)
            for (s, start, end), check in zip(inputs, checks):
                s = [ c for c in s ]
                check = [ c for c in check ]
                reverse_string(s, start, end)
                assert s == check

        def test_reverse_words():
            inputs = [ "abc def hij", "asdf", "   123   ", ]
            checks = [ "cba fed jih", "fdsa", "   321   ", ]
            assert len(inputs) == len(checks)
            for s, check in zip(inputs, checks):
                s = [ c for c in s ]
                check = [ c for c in check ]
                reverse_words(s)
                assert s == check

        def test_find_rend():
            inputs = [ "abc", " abc ", "   ", "a   ", ]
            checks = [ 2, 3, -1, 0, ]
            assert len(inputs) == len(checks)
            for s, check in zip(inputs, checks):
                s = [ c for c in s ]
                result = find_rend(s)
                assert result == check

        def test_helpers():
            test_lstrip()
            test_remove_multiple_spaces()
            test_reverse_string()
            test_reverse_words()
            test_find_rend()
        #   }}}
        #test_helpers()

        s = [ c for c in s ]
        remove_multiple_spaces(s)
        reverse_words(s)
        reverse_string(s)
        lstrip(s)
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

