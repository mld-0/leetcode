#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
from typing import List, Optional
#   arg_printer(args: List, arg_names: List), list2str(vals: List, max_str_length: int=60) {{{
def arg_printer(args: List, arg_names: List):  
    assert len(args) == len(arg_names), "input args / arg_names length mismatch"
    output = ""
    for arg, arg_name in zip(args, arg_names):
        output += f"{arg_name}=({list2str(arg)}), "
    print(output[:-2])
def list2str(vals: List, max_str_length: int=60):  
    def build_string(vals, num_elements):
        if num_elements < len(vals):
            return f"[{','.join(map(str, vals[:num_elements]))},...,{vals[-1]}]"
        else:
            return str(vals)
    if type(vals) != type([]):
        return str(vals)
    num_elements = len(vals)
    while num_elements > 0:
        formatted_list = build_string(vals, num_elements)
        if len(formatted_list) <= max_str_length:
            break
        num_elements -= 1
    return formatted_list
#   }}}

#   Solutions taken from 05-longest-palindromic-substring
class Solution:
    """How many palindromes does a given input string contain"""

    #   runtime: beats 33%
    def countSubstrings_ans_DP_BottomUp(self, s: str) -> int:
        result = 0

        #   is_palindrome[i][j]: True if s[i..=j] is a palindrome
        is_palindrome = [ [ False for _ in range(len(s)) ] for _ in range(len(s)) ]

        #   All strings of length 1 are palindromes
        for i in range(len(s)):
            is_palindrome[i][i] = True
            result += 1

        #   Strings of length 2 are palindromes if both letters match
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                is_palindrome[i][i+1] = True
                result += 1

        #   s[l..=r] is a palindrome if s[l] == s[r] and is_palindrome[l+1][r-1] == True
        for r in range(len(s)):
            for l in range(r):
                if s[l] == s[r] and is_palindrome[l+1][r-1] == True:
                    is_palindrome[l][r] = True
                    result += 1

        return result


    #   runtime: beats 98%
    def countSubstrings_ans_TwoPointers(self, s: str) -> int:
        result = 0

        for i in range(0, len(s)):
            r = i
            while r < len(s) and s[i] == s[r]:
                r += 1
                result += 1

            l = i - 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                result += 1

        return result


s = Solution()
test_functions = [ s.countSubstrings_ans_DP_BottomUp, s.countSubstrings_ans_TwoPointers, ]
arg_names = ["s"]

inputs = [ "abc", "aaa", "abcdcba", ]
checks = [ 3, 6, 10, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for args, check in zip(inputs, checks):
        if type(args) != type(tuple()) and len(arg_names) == 1: args = tuple([args])
        arg_printer(args, arg_names)
        result = f(*args)
        print(f"result=({list2str(result)})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

