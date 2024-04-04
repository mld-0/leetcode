#   {{{3
       #   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
from typing import List, Optional

class Solution:
    """Determine the maximum nested depth of parenthesis in a valid mathematical expression"""

    #   runtime: beats 90%
    #    memory: beats 38%
    def maxDepth_Stack(self, s: str) -> int:
        result = 0
        stack = []
        for c in s:
            if c == '(':
                stack.push(c)
            elif c == ')':
                stack.pop()
            result = max(result, len(stack))
        return result


    #   runtime: beats 94%
    #    memory: beats 91%
    def maxDepth_Counter(self, s: str) -> int:
        result = 0
        count = 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
            result = max(result, count)
        return result


s = Solution()
test_functions = [ s.maxDepth_Counter, s.maxDepth_Counter, ]

inputs = [ "(1+(2*3)+((8)/4))+1", "(1)+((2))+(((3)))", ]
checks = [ 3, 3, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for s, check in zip(inputs, checks):
        print(f"s=({s})")
        result = f(s)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

