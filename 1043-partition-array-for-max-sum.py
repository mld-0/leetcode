#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
import math
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
    """Partition input `arr` into contiguous subarrays of at most k elements such that the sum of the largest element in each subarray multiplied by that subarray length is maximised"""

    #   runtime: beats 17%
    def maxSumAfterPartitioning_DP_BottomUp(self, arr: List[int], k: int) -> int:

        #   table[i]: answer for arr[:i]
        #       = max(table[i-j] + max(A[i-1]...A[i-j]) * j) for j = 1..=k
        table = [ 0 for _ in range(len(arr)+1) ]

        for i in range(1, len(arr)+1):
            for j in range(1, k+1):
                if i-j < 0 or i-1 < i-j:
                    continue
                trial = table[i-j] + max(arr[i-j:i]) * j
                table[i] = max(table[i], trial)

        return table[-1]


    #   runtime: beats 75%
    def maxSumAfterPartitioning_DP_BottomUp_Optimised(self, arr: List[int], k: int) -> int:

        #   table[i]: answer for arr[:i]
        #       = max(table[i-j] + max(A[i-1]...A[i-j]) * j) for j = 1..=k
        table = [ 0 for _ in range(len(arr)+1) ]

        for i in range(1, len(arr)+1):
            max_in_window = 0
            for j in range(1, k+1):
                if i-j < 0 or i-1 < i-j:
                    continue
                max_in_window = max(max_in_window, arr[i-j])
                trial = table[i-j] + max_in_window * j
                table[i] = max(table[i], trial)

        return table[-1]


s = Solution()
test_functions = [ s.maxSumAfterPartitioning_DP_BottomUp, s.maxSumAfterPartitioning_DP_BottomUp_ii, ]
arg_names = ["arr","k"]

inputs = [ ([1,15,7,9,2,5,10],3), ([1,4,1,5,7,3,6,1,9,9,3],4), ([1],1), ]
checks = [ 84, 83, 1, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for args, check in zip(inputs, checks):
        if type(args) == type([]) and len(arg_names) == 1: args = tuple([args])
        arg_printer(args, arg_names)
        result = f(*args)
        print(f"result=({list2str(result)})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

