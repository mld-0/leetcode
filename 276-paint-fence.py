#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
import functools
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
    """We are painting a fence of `n` posts `k` different colors. There can be at most 3 adjacent posts of the same color. How many combinations are possible?"""

    #   runtime: beats 89%
    def numWays_ans_DP_BottomUp(self, n: int, k: int) -> int:

        if n == 1:
            return k

        #   table[i][j]: number of ways the first i posts can be painted if the j-th post is color k (posts and colors are 0-indexed)
        table = [ [ 0 for _ in range(k) ] for _ in range(n) ]

        for j in range(k):
            table[0][j] = k
            table[1][j] = k * k

        for i in range(2, n):
            for j in range(k):
                table[i][j] = (k-1) * (table[i-1][j] + table[i-2][j])

        return table[-1][-1]


    #   runtime: beats 95%
    def numWays_ans_DP_TopDown(self, n: int, k: int) -> int:

        @functools.cache
        def solve(i: int) -> int:
            if i == 0:
                return k
            if i == 1:
                return k * k
            return (k-1) * (solve(i-1) + solve(i-2))

        return solve(n-1)


s = Solution()
test_functions = [ s.numWays_ans_DP_BottomUp, s.numWays_ans_DP_TopDown, ]
arg_names = ["n", "k"]

inputs = [(3,2), (1,1), (7,2)]
checks = [6, 1, 42]
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

