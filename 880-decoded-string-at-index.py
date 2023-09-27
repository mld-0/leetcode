#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
from typing import List, Optional

class Solution:
    """Decode the input string, `s`, and return the `k`th letter (1-indexed). To decode a string, read it one character at a time, writing each letter character to the output, and repeating the contents of the output `d-1` times if a digit `d` is read"""

    #   memory limit exceded
    def decodeAtIndex_i(self, s: str, k: int) -> str:
        letters = set( [ chr(x) for x in range(ord('a'), ord('z')+1) ] )
        numbers = set( [ chr(x) for x in range(ord('0'), ord('9')+1) ] )
        result = []
        for c in s:
            if c in letters:
                result.append(c)
            elif c in numbers:
                result = result * (int(c))
            if len(result) >= k:
                break
        return result[k-1]


    def decodeAtIndex_ii(self, s: str, k: int) -> str:
        ...


s = Solution()
test_functions = [ s.decodeAtIndex_i, s.decodeAtIndex_ii, ]

#   {{{
inputs = [ ("leet2code3",10), ("ha22",5), ("a2345678999999999999999",1), ("y959q969u3hb22odq595", 222280369), ]
checks = [ "o", "h", "a", "y", ]
#   }}}
inputs = [ ("leet2code3",10), ("ha22",5), ("a2345678999999999999999",1), ("a2b3c4d5e6f7g8h9",3), ("vk6u5xhq9v",554), ]
checks = [ "o", "h", "a", "b", "k", ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for (s, k), check in zip(inputs, checks):
        print(f"s=({s}), k=({k})")
        result = f(s, k)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

