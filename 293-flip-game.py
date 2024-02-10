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
    """Determine all possible results of replacing a single instance of '++' with '--' in the input"""

    #   runtime: beats 78%
    def generatePossibleNextMoves_i(self, currentState: str) -> List[str]:
        currentState = [ c for c in currentState ]
        result = []

        for l in range(len(currentState)-1):
            if currentState[l] == '+' and currentState[l+1] == '+':
                new_state = currentState[:]
                new_state[l] = '-'
                new_state[l+1] = '-'
                result.append(''.join(new_state))

        return result


    #   runtime: beats 82%
    def generatePossibleNextMoves_ii(self, s: str) -> List[str]:
        return [ s[:i] + "--" + s[i+2:] for i in range(len(s)-1) if s[i:i+2] == '++' ]


s = Solution()
test_functions = [ s.generatePossibleNextMoves_i, s.generatePossibleNextMoves_ii, ]
arg_names = ["currentState"]

inputs = [ "++++", "+", ]
checks = [ ["--++","+--+","++--"], [], ]
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
        assert sorted(result) == sorted(check), "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

