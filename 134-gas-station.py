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
    """Each gas station has `gas[i]` units of gas available, and it takes `cost[i]` units of gas to travel to the next station. Determine which station we can start from and complete a whole loop"""

    #   runtime: TLE
    def canCompleteCircuit_i(self, gas: List[int], cost: List[int]) -> int:
        deficit = dict()
        for i in range(len(gas)):
            remaining = gas[i] - cost[i]
            if remaining < 0:
                continue
            j = i+1 if i+1 < len(gas) else 0
            while j != i:
                remaining = remaining + gas[j] - cost[j]
                if remaining < 0:
                    break
                if j in deficit and abs(deficit[j][0]) > remaining:
                    remaining = deficit[j]
                    break
                j = j+1 if j+1 < len(gas) else 0
            if remaining >= 0:
                return i
            else:
                deficit[i] = (remaining, j)
        return -1


    #   runtime: beats 95%
    def canCompleteCircuit_ans_SegmentSum(self, gas: List[int], cost: List[int]) -> int:
        running_total = 0
        segment_total = 0
        segment_start = 0
        for i in range(len(gas)):
            gain = gas[i] - cost[i]
            running_total += gain
            segment_total += gain
            if segment_total < 0:
                segment_start = i+1
                segment_total = 0
        if running_total >= 0 and segment_start < len(gas):
            return segment_start
        return -1


s = Solution()
test_functions = [ s.canCompleteCircuit_i, s.canCompleteCircuit_ans_SegmentSum, ]
arg_names = ["gas", "cost"]

inputs = [ ([1,2,3,4,5],[3,4,5,1,2]), ([2,3,4],[3,4,3]), ([4,5,2,6,5,3],[3,2,7,3,2,9]), ([5,1,2,3,4],[4,4,1,5,1]), ]
checks = [ 3, -1, -1, 4, ]
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

