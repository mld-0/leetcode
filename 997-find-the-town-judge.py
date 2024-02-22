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
    """The array `trust[i]=[a,b]` indicates that person a trusts person b. In a town of `n` people, if the town judge exists, then: 1) they trust nobody, 2) everyone else trusts them, and 3) there is exactly one person that satisfies 1 and 2"""

    #   runtime: beats 99%
    def findJudge_HashMap(self, n: int, trust: List[List[int]]) -> int:
        trust_map = defaultdict(set)
        for (a, b) in trust:
            trust_map[a].add(b)

        trusts_noone = -1
        for i in range(1, n+1):
            if i not in trust_map:
                if trusts_noone == -1:
                    trusts_noone = i
                else:
                    return -1
        if trusts_noone == -1:
            return -1

        for i in range(1, n+1):
            if i == trusts_noone:
                continue
            if trusts_noone not in trust_map[i]:
                return -1

        return trusts_noone


    #   runtime: beats 97%
    def findJudge_ans_GraphNetFlow(self, n: int, trust: List[List[int]]) -> int:
        #   difference between number of people they trust vs who trust them
        trust_netFlow = [ 0 for _ in range(0, n+1) ]

        for (a, b) in trust:
            trust_netFlow[a] -= 1
            trust_netFlow[b] += 1

        for i in range(1, n+1):
            if trust_netFlow[i] == n-1:
                return i
        return -1


s = Solution()
test_functions = [ s.findJudge_HashMap, s.findJudge_ans_GraphNetFlow, ]
arg_names = ["n", "trust"]

inputs = [ (2,[[1,2]]), (3,[[1,3],[2,3]]), (3,[[1,3],[2,3],[3,1]]), ]
checks = [ 2, 3, -1, ]
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

