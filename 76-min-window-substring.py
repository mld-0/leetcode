#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
import math
from collections import Counter, defaultdict
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
    """Determine the minimum window substring of `s` containing every character of `t`"""

    #   runtime: beats 12%
    def minWindow_SlidingWindow(self, s: str, t: str) -> str:

        def contains_counts(c1, c2):
            """Does c2 have at least as many of each item as c1"""
            if c1.keys() > c2.keys():
                return False
            for k in c1:
                if k not in c2:
                    return False
                if c2[k] < c1[k]:
                    return False
            return True

        if s == t:
            return s

        t_counter = Counter(t)
        window_counter = defaultdict(int)
        t_letters = set(t)

        #   move r until window_counter contains all letters of t
        l = 0
        r = 0
        while r < len(s) and not contains_counts(t_counter, window_counter):
            if s[r] in t_letters:
                window_counter[s[r]] += 1
            r += 1
        if r == len(s) and not contains_counts(t_counter, window_counter):
            return ""
        r -= 1
        result = (l, r)

        while r < len(s):
            while l <= r and contains_counts(t_counter, window_counter):
                if r-l < result[1]-result[0]:
                    result = (l, r)
                if s[l] in t_letters:
                    window_counter[s[l]] -= 1
                l += 1
            r += 1
            if r < len(s): 
                if s[r] in t_letters:
                    window_counter[s[r]] += 1

        return s[result[0]:result[1]+1]


    #   runtime: beats 77%
    def minWindow_ans_SlidingWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        if s == t:
            return s

        t_counter = Counter(t)
        required = len(t_counter)
        l = 0
        r = 0
        formed = 0
        window_counter = {}
        result = math.inf, None, None

        while r < len(s):
            c = s[r]
            window_counter[c] = window_counter.get(c, 0) + 1
            if c in t_counter and window_counter[c] == t_counter[c]:
                formed += 1
            while l <= r and formed == required:
                c = s[l]
                if r-l+1 < result[0]:
                    result = (r-l+1, l, r)
                window_counter[c] -= 1
                if c in t_counter and window_counter[c] < t_counter[c]:
                    formed -= 1
                l += 1
            r += 1

        if result[0] == math.inf:
            return ""
        return s[result[1]:result[2]+1]


s = Solution()
test_functions = [ s.minWindow_SlidingWindow, s.minWindow_ans_SlidingWindow, ]
arg_names = ["s","t"]

inputs = [ ("ADOBECODEBANC","ABC"), ("a","a"), ("a","aa"), ("ab","b"), ]
checks = [ "BANC", "a", "", "b", ]
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

