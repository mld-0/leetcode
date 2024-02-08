#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
import math
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
    num_elements = len(vals)
    while num_elements > 0:
        formatted_list = build_string(vals, num_elements)
        if len(formatted_list) <= max_str_length:
            break
        num_elements -= 1
    return formatted_list
#   }}}

class Solution:
    """Find the minimum number of perfect squares that sum to a given value"""

    #   runtime: beats 34%
    def numSquares_DP_TopDown(self, n: int) -> int:

        @functools.cache
        def solve(value: int) -> int:
            if value == 0:
                return 0
            if value == 1:
                return 1
            if value < 0:
                return math.inf
            result = value
            for i in range(int(math.sqrt(value)), 1, -1):
                temp = solve(value - i**2) + 1
                result = min(result, temp)
            return result

        return solve(n)


    #   runtime: beats 70%
    def numSquares_ans_DP_BottomUp(self, n: int) -> int:
        sqrt_n = int(math.sqrt(n))
        squares = [ i**2 for i in range(sqrt_n+1) ]

        table = [ math.inf for _ in range(n+1) ]
        table[0] = 0

        for i in range(1, n+1):
            for square in squares:
                if i < square:
                    break
                table[i] = min(table[i], table[i-square] + 1)

        return table[-1]


    #   runtime: beats 92%
    def numSquares_ans_GreedyDFS(self, n: int) -> int:

        def solve(n, count):
            """Can `n` be formed from the sum of `count` perfect squares"""
            if count == 1:
                return n in squares
            for square in squares:
                if solve(n-square, count-1):
                    return True
            return False

        sqrt_n = int(math.sqrt(n))
        squares = [ i**2 for i in range(sqrt_n+1) ]

        for i in range(1, n+1):
            if solve(n, i):
                return i


    #   beats 98%
    def numSquares_ans_Maths(self, n: int) -> int:

        def isSquare(n: int) -> bool:
            x = int(math.sqrt(n))
            return x * x == n

        while (n & 3) == 0:
            n >>= 2
        if (n & 7) == 7:
            return 4
        if isSquare(n):
            return 1

        for i in range(1, int(math.sqrt(n))+1):
            if isSquare(n - i**2):
                return 2
        return 3


s = Solution()
test_functions = [ s.numSquares_DP_TopDown, s.numSquares_ans_DP_BottomUp, s.numSquares_ans_GreedyDFS, s.numSquares_ans_Maths, ]
arg_names = ["n"]

inputs = [ 12, 13, 5, 6, 7691, ]
checks = [ 3, 2, 2, 3, 3, ]
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

