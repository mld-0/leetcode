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
    """For each day in `temperatures`, determine how many days until a day with a higher temperature (0 indicating there is not one)"""

    #   runtime: TLE
    def dailyTemperatures_TwoPointers(self, temperatures: List[int]) -> List[int]:
        result = [ 0 for _ in temperatures ]

        l = 0
        while l < len(temperatures)-1:
            r = l+1
            while r < len(temperatures) and temperatures[r] <= temperatures[l]:
                r += 1
            if r == len(temperatures):
                result[l] = 0
            else:
                result[l] = r-l
            l += 1

        return result


    def dailyTemperatures_ans_MonotonicStack(self, temperatures: List[int]) -> List[int]:
        raise NotImplementedError("review ans")
        #result = [ 0 for _ in temperatures ]
        #stack = []
        #for day, temp in enumerate(temperatures):
        #    while len(stack) > 0 and stack[-1][1] < temp:
        #        previous_day, previous_temp = stack.pop()
        #        result[previous_day] = day - previous_day
        #    stack.append([day,temp])
        #return result


    def dailyTemperatures_ans_Array(self, temperatures: List[int]) -> List[int]:
        raise NotImplementedError("review ans")
        #result = [ 0 for _ in temperatures ]
        #hottest = 0
        #for day in range(len(temperatures)-1, -1, -1):
        #    temp = temperatures[day]
        #    if temp >= hottest:
        #        hottest = temp
        #        continue
        #    count = 1
        #    while temperatures[day+count] <= temp:
        #        count += result[day+count]
        #    result[day] = count
        #return result


s = Solution()
test_functions = [ s.dailyTemperatures_TwoPointers, s.dailyTemperatures_ans_MonotonicStack, s.dailyTemperatures_ans_Array, ]
arg_names = ["temperatures"]

inputs = [ [73,74,75,71,69,72,76,73], [30,40,50,60], [30,60,90], ]
checks = [ [1,1,4,2,1,1,0,0], [1,1,1,0], [1,1,0], ]
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

