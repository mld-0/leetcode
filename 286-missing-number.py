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
    if num_elements > 100:
        return f"len([...])=({num_elements})"
    while num_elements > 0:
        formatted_list = build_string(vals, num_elements)
        if len(formatted_list) <= max_str_length:
            break
        num_elements -= 1
    return formatted_list
#   }}}

class Solution:
    """Given a list containing n distinct numbers in the range [0,n], return the only number in the range that is missing"""

    #   runtime: beats 45%
    def missingNumber_Sorting(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)
        for i in range(len(nums)):
            if nums_sorted[i] != i:
                return i
        return len(nums)


    #   runtime: beats 98%
    def missingNumber_Sweep(self, nums: List[int]) -> int:
        found = [ False for _ in range(len(nums)+1) ]
        for i in range(len(nums)):
            found[nums[i]] = True
        for i in range(len(found)):
            if not found[i]:
                return i


    #   runtime: beats 98%
    def missingNumber_Maths(self, nums: List[int]) -> int:
        return sum(range(len(nums)+1)) - sum(nums)


    #   runtime: beats 93%
    def missingNumber_ans_Set(self, nums: List[int]) -> int:
        nums_set = set(nums)
        for n in range(len(nums)+1):
            if n not in nums_set:
                return n


    #   runtime: beats 89%
    def missingNumber_ans_Bitwise(self, nums: List[int]) -> int:
        result = len(nums)
        for i, n in enumerate(nums):
            result ^= i ^ n
        return result


    #   runtime: beats 99%
    def missingNumber_ans_Maths(self, nums: List[int]) -> int:
        expected = (len(nums) * (len(nums)+1)) // 2
        actual = sum(nums)
        return expected - actual


s = Solution()
test_functions = [ s.missingNumber_Sorting, s.missingNumber_Sweep, s.missingNumber_Maths, s.missingNumber_ans_Bitwise, s.missingNumber_ans_Set, s.missingNumber_ans_Maths, ]
arg_names = ["nums"]

inputs = [ [1,2], [3,0,1], [0,1], [9,6,4,2,3,5,7,0,1], [*range(0,500), *range(501,10000)], ]
checks = [ 0, 2, 2, 8, 500, ]
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

