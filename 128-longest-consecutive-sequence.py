#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
from collections import defaultdict
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

    #   runtime: TLE
    def longestConsecutive_i(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        smallest = min(nums)
        largest = max(nums)
        nums_set = set(nums)

        result = 1
        for n in nums_set:
            current = 1
            for i in range(n+1, largest+1):
                if i in nums_set:
                    current += 1
                else:
                    break
            result = max(current, result)

        return result


    #   runtime: beats 72%
    def longestConsecutive_ii(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        smallest = min(nums)
        largest = max(nums)
        nums_set = set(nums)

        smallest_start = dict()

        result = 1
        for n in nums_set:
            if n in smallest_start:
                continue
            current = 1
            for i in range(n+1, largest+1):
                if i in nums_set:
                    current += 1
                    if i not in smallest_start:
                        smallest_start[i] = n
                    else:
                        smallest_start[i] = min(smallest_start[i], n)
                else:
                    break
            result = max(current, result)

        return result


    #   runtime: beats 79%
    def longestConsecutive_ans(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                longest_streak = max(longest_streak, current_streak)
        return longest_streak


s = Solution()
test_functions = [ s.longestConsecutive_i, s.longestConsecutive_ii, s.longestConsecutive_ans, ]
arg_names = ["nums"]

inputs = [ [100,4,200,1,3,2], [0,3,7,2,5,8,4,6,0,1], [], [0,0], [0,1,2,4,8,5,6,7,9,3,55,88,77,99,999999], [1,0,-1], ]
checks = [ 4, 9, 0, 1, 10, 3, ]
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


