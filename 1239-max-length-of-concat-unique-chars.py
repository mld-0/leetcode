#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
from collections import Counter
from typing import List, Optional, Set

class Solution:
    """Given an array of strings, `arr`, determine the length of the longest possible concatenation of elements where each character is unique"""

    #   runtime: beats 95%
    def maxLength_Backtracking(self, arr: List[str]) -> int:

        arr_letters = [ set(s) for s in arr ]
        result = 0
        def solve(i, used_letters, current_length):
            nonlocal result
            result = max(result, current_length)
            for j in range(i+1, len(arr)):
                if len(arr_letters[j]) < len(arr[j]):
                    continue
                new_used_letters = used_letters | arr_letters[j]
                if len(new_used_letters) < len(used_letters) + len(arr_letters[j]):
                    continue
                solve(j, new_used_letters, current_length + len(arr[j]))

        solve(-1, set(), 0)
        return result


    #   runtime: beats 96%
    def maxLength_Backtracking_BitwiseSets(self, arr: List[str]) -> int:

        def word_to_bitset(word: str) -> int:
            result = 0
            for c in word:
                result += 1 << (ord(c) - ord('a'))
            return result
        def has_duplicate(word: str) -> bool:
            counts = Counter(word)
            for c in word:
                if counts[c] > 1:
                    return True
            return False

        arr_letters = [ word_to_bitset(s) for s in arr ]
        arr_has_duplicate = [ has_duplicate(s) for s in arr ]
        result = 0
        def solve(i, used_letters, current_length):
            nonlocal result
            result = max(result, current_length)
            for j in range(i+1, len(arr)):
                if arr_has_duplicate[j]:
                    continue
                if used_letters & arr_letters[j]:
                    continue
                new_used_letters = used_letters | arr_letters[j]
                solve(j, new_used_letters, current_length + len(arr[j]))

        solve(-1, 0, 0)
        return result


s = Solution()
test_functions = [ s.maxLength_Backtracking, s.maxLength_Backtracking_BitwiseSets, ]

inputs = [ ["un","iq","ue"], ["cha","r","act","ers"], ["abcdefghijklmnopqrstuvwxyz"], ["aa","bb"], ]
checks = [ 4, 6, 26, 0, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for vals, check in zip(inputs, checks):
        print(f"vals=({vals})")
        result = f(vals)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

