#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
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
    """Players take turns replace a single instance of '++' with '--' in the input. The loser is the first player not to be able to make a substitution. Determine whether the starting player can guarantee a win"""

    #   runtime: beats 60%
    def canWin_Backtracking(self, currentState: str) -> bool:

        @functools.cache
        def get_next_moves(state: str) -> List[str]:
            return [ state[:i] + "--" + state[i+2:] for i in range(len(state)-1) if state[i:i+2] == '++' ]

        @functools.cache
        def solve(state: str) -> bool:
            for next_move in get_next_moves(state):
                if not solve(next_move):
                    return True
            return False

        return solve(currentState)


    #   runtime: beats 99%
    def canWin_ans_GameTheory(self, currentState: str) -> bool:

        def firstMissingNumber(lut):
            m = len(lut)
            for i in range(m):
                if i not in lut:
                    return i
            return m

        s = [ c for c in currentState ]
        curlen = 0
        maxlen = 0
        board_init_state = []
        for i in range(len(s)):
            if s[i] == '+': curlen += 1
            if i+1 == len(s) or s[i] == '-':
                if curlen >= 2: board_init_state.append(curlen)
                maxlen = max(maxlen, curlen)
                curlen = 0

        g = [0] * (maxlen+1)
        for l in range(2, maxlen+1):
            gsub = set()
            for l_first_game in range(0, l//2):
                l_second_game = l - l_first_game - 2
                gsub.add(g[l_first_game] ^ g[l_second_game])
            g[l] = firstMissingNumber(gsub)

        g_final = 0
        for s in board_init_state:
            g_final ^= g[s]
        return g_final != 0


s = Solution()
test_functions = [ s.canWin_Backtracking, s.canWin_ans_GameTheory, ]
arg_names = ["currentState"]

inputs = [ "++++", "+", "+++++++++", "-++++++++++--------+++++++++", ]
checks = [ True, False, False, True, ]
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

