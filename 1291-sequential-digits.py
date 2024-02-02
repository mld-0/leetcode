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

class Solution:
    """Return a sorted list of all the integers in the range [low,high] where each digit is exactly one more than the previous digit"""

    #   runtime: beats 90%
    def sequentialDigits_Recursive(self, low: int, high: int) -> List[int]:
        result = []

        def all_sequential(current):
            nonlocal low, high
            if int(current) > high:
                return
            if int(current) >= low:
                result.append(int(current))
            last_digit = int(current[-1])
            if last_digit == 9:
                return
            all_sequential(current + str(1+last_digit))

        for i in range(1, 10):
            all_sequential(str(i))
        return sorted(result)


    #   runtime: beats 92%
    def sequentialDigits_ans_SlidingWindow(self, low: int, high: int) -> List[int]:
        s = "123456789"
        result = []

        for length in range(len(str(low)), len(str(high))+1):
            for start in range(len(s)-length+1):
                current = int(s[start:start+length])
                if current >= low and current <= high:
                    result.append(current)

        return sorted(result)



s = Solution()
test_functions = [ s.sequentialDigits_Recursive, s.sequentialDigits_ans_SlidingWindow, ]
arg_names = ["low","high"]

inputs = [ (100,300), (1000,13000), ]
checks = [ [123,234], [1234,2345,3456,4567,5678,6789,12345], ]
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

