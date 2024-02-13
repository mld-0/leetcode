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
    if len(vals) == 0:
        return str(vals)
    num_elements = len(vals)
    while num_elements > 0:
        formatted_list = build_string(vals, num_elements)
        if len(formatted_list) <= max_str_length:
            break
        num_elements -= 1
    return formatted_list
#   }}}

class Solution:

    #   runtime: 39%
    def firstPalindrome_TwoPointers(self, words: List[str]) -> str:

        def is_palindrome(s: str) -> bool:
            l = 0
            r = len(s) - 1
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        for word in words:
            if is_palindrome(word):
                return word
        return ""

    
    #   runtime: beats 94%
    def firstPalindrome_Pythonic(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ""


s = Solution()
test_functions = [ s.firstPalindrome_TwoPointers, s.firstPalindrome_Pythonic, ]
arg_names = ["words"]

inputs = [ ["abc","car","ada","racecar","cool"], ["notapalindrome","racecar"], ["def","ghi"], ]
checks = [ "ada", "racecar", "", ]
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

