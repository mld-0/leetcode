#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
from typing import List, Optional, Union, Any, Set
#   arg_printer(args, arg_names: List), list2str(vals: List, max_str_length: int=60) {{{
def arg_printer(args, arg_names: List):  
    assert len(args) == len(arg_names), "input args / arg_names length mismatch"
    output = ""
    for arg, arg_name in zip(args, arg_names):
        output += f"{arg_name}=({list2str(arg)}), "
    print(output[:-2])
def list2str(vals, max_str_length: int=60):  
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
    if num_elements > 100:
        return f"len([...])=({num_elements})"
    while num_elements > 0:
        formatted_list = build_string(vals, num_elements)
        if len(formatted_list) <= max_str_length:
            break
        num_elements -= 1
    return formatted_list
#   }}}

#   bitwise tricks:
#       (n & (-n)) isolates the rightmost one bit of n
#       (n & (n-1)) sets rightmost one bit of n to zero

class Solution:
    """Determine whether `n` is a power of 2"""

    #   runtime: beats 95%
    def isPowerOfTwo_IterativeMultiply(self, n: int) -> bool:
        x = 1
        while x <= n:
            if n == x:
                return True
            x *= 2
        return False


    #   runtime: beats 91%
    def isPowerOfTwo_IterativeBitshift(self, n: int) -> bool:
        x = 1
        while x <= n:
            if n == x:
                return True
            x <<= 1
        return False


    #   runtime: beats 99%
    def isPowerOfTwo_IterativeBitshiftMemo(self, n: int) -> bool:
        if not hasattr(self, 'powers_of_two'):
            self.powers_of_two: Set[int] = set()
        if n in self.powers_of_two:
            return True
        x = 1
        while x <= n:
            self.powers_of_two.add(x)
            if n == x:
                return True
            x <<= 1
        return False


    #   runtime: beats 99%
    def isPowerOfTwo_ans_Bitwise_i(self, n: int) -> bool:
        if n <= 0:
            return False
        return (n & (-n)) == n


    def isPowerOfTwo_ans_Bitwise_ii(self, n: int) -> bool:
        if n <= 0:
            return False
        return (n & (n-1)) == 0


s = Solution()
test_functions = [ s.isPowerOfTwo_IterativeMultiply, s.isPowerOfTwo_IterativeBitshift, s.isPowerOfTwo_IterativeBitshiftMemo, s.isPowerOfTwo_ans_Bitwise_i, s.isPowerOfTwo_ans_Bitwise_ii, ]
arg_names = ["n"]

inputs = [ 1, 16, 3, 4, 5, 0, 5_000_000, 10_000_000_000, 33554432, 2**50, ]
checks = [ True, True, False, True, False, False, False, False, True, True, ]
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

