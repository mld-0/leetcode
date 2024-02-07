#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
import heapq
from collections import Counter
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
    """Sort the characters in the input string in decreasing order based on the frequency of occurences of that character"""

    #   runtime: beats 84%
    def frequencySort_BucketCountHeapSort(self, s: str) -> str:
        char2index = \
            { chr(ord('a')+i): i for i in range(0,26) } | \
            { chr(ord('A')+i): i+26 for i in range(0,26) } | \
            { chr(ord('0')+i): i+52 for i in range(0,10) }
        index2char = { v: k for k, v in char2index.items() }

        counts = [ [0,index2char[i]]  for i in range(0,26+26+10) ]
        non_zero_elements = 0

        for c in s:
            i = char2index[c]
            if counts[i][0] == 0:
                non_zero_elements += 1
            counts[i][0] += 1

        heapq.heapify(counts)
        result_counts = heapq.nlargest(non_zero_elements, counts)

        result = []
        for char, count in result_counts:
            result.append(char * count)
        return ''.join(result)


    #   runtime: beats 98%
    def frequencySort_CounterHeapSort(self, s: str) -> str:
        counts = Counter(s)
        non_zero_elements = len(set(s))
        result = []
        counts_list = [ [v,k] for k, v in counts.items() ]
        heapq.heapify(counts_list)
        for v, k in heapq.nlargest(non_zero_elements, counts_list):
            result.append(k * v)
        return ''.join(result)


s = Solution()
test_functions = [ s.frequencySort_BucketCountHeapSort, s.frequencySort_CounterHeapSort, ]
arg_names = ["s"]

inputs = [ "tree", "cccaaa", "Aabb", "2a554442f544asfasssffffasss", ]
checks = [ ("eert","eetr"), ("aaaccc","cccaaa"), ("bbAa","bbaA"), ("sssssssffffff44444aaaa55522"), ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"
checks = [ set(check) if type(check) == type(tuple()) else set([check]) for check in checks ]

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for args, check in zip(inputs, checks):
        if type(args) != type(tuple()) and len(arg_names) == 1: args = tuple([args])
        arg_printer(args, arg_names)
        result = f(*args)
        print(f"result=({list2str(result)})")
        assert result in check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

