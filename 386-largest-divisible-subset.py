#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
import functools
from typing import List, Tuple, Optional
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
    """For a list of numbers, return the largest subset such that every pair, x,y satisfies either x%y==0 or y%x==0"""

    #   runtime: TLE
    def largestDivisibleSubset_i(self, nums: List[int]) -> List[int]:
        result = ()

        @functools.cache
        def is_valid(result: Tuple[int]) -> bool:
            for i in range(len(result)):
                for j in range(i, len(result)):
                    if result[i] % result[j] != 0 and result[j] % result[i] != 0:
                        return False
            return True

        @functools.cache
        def solve(current_index, current_solution):
            nonlocal result
            if current_index >= len(nums):
                return
            temp1 = ( *current_solution, nums[current_index] )
            if is_valid(tuple(sorted(temp1))):
                if len(temp1) > len(result):
                    result = temp1
                solve(current_index+1, temp1)
            if is_valid(tuple(sorted(current_solution))):
                if len(current_solution) > len(result):
                    result = current_solution
                solve(current_index+1, current_solution)

        solve(0, ())
        return list(result)


    #   runtime: beats 86%
    def largestDivisibleSubset_ans_DP_BottomUp(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)

        #   subsets[i]: largest partial solution for which the largest number is `nums[i]`
        subsets = dict()

        #   Here, we rely on the fact that for a partial solution and a number, `x`, which is larger than any number in the partial solution, x can be added to the partial solution if it is evenly divisble by the largest number in that partial solution
        for i in range(len(nums)):
            temp = set()
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(subsets[j]) > len(temp):
                    temp = subsets[j]
            subsets[i] = temp | {nums[i]}

        return list(sorted(max(subsets.values(), key=len)))


s = Solution()
test_functions = [ s.largestDivisibleSubset_i, s.largestDivisibleSubset_ans_DP_BottomUp, ]
arg_names = ["nums"]

inputs = [ [1,2,3], [1,2,4,8], ]
checks = [ ((1,2),(1,3),), ((1,2,4,8),), ]
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
        assert tuple(result) in set(check), "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

