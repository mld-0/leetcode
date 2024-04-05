#   {{{3
       #   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
from typing import List, Optional

class Solution:
    """A good string has no two adjacent letters which are the same character but different case. Make the string good by removing pairs of adjacent characters that make the string bad until the string is good."""

    #   runtime: beats 28%
    #    memory: beats 91%
    def makeGood_i(self, s: str) -> str:

        def solve(s):
            if len(s) == 0:
                return s
            result = []
            result.append(s[0])
            done_removal = False
            l = 0
            for r in range(1, len(s)):
                if not done_removal and s[r].lower() == s[l].lower() and s[r] != s[l]:
                    result.pop()
                    done_removal = True
                else:
                    result.append(s[r])
                    l = r
            return ''.join(result)

        previous = s
        current = solve(s)
        while current != previous:
            previous = current
            current = solve(current)
        return current


    #   runtime: beats 83%
    #    memory: beats 91%
    def makeGood_ii(self, s: str) -> str:

        def solve(s):
            if len(s) == 0:
                return s
            for i in range(1, len(s)):
                if s[i] != s[i-1] and s[i].lower() == s[i-1].lower():
                    del s[i-1]
                    del s[i-1]
                    return

        s = [ c for c in s ]
        current = s
        previous = s[:]
        solve(current)
        while current != previous:
            previous = current[:]
            solve(current)
        return ''.join(current)


    #   runtime: beats 70%
    #    memory: beats 47%
    def makeGood_ans_Stack(self, s: str) -> str:
        result = []
        for c in s:
            if len(result) > 0 and c.lower() == result[-1].lower() and c != result[-1]:
                result.pop()
            else:
                result.append(c)
        return ''.join(result)


    def makeGood_ans_TwoPointers(self, s: str) -> str:
        raise NotImplementedError("please complete Two-Pointers answers")


s = Solution()
test_functions = [ s.makeGood_i, s.makeGood_ii, s.makeGood_ans_Stack, s.makeGood_ans_TwoPointers, ]

inputs = [ "leEeetcode", "abBAcC", "s", "Bpb", "iIiIcXxCrcaLlACRBPppb", ]
checks = [ "leetcode", "", "s", "Bpb", "Bpb", ]
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

