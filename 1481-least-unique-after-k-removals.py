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
    """Determine the minimum number of unique elements that can be left after removing exactly `k elements from input"""

    #   runtime: beats 99%
    def findLeastNumOfUniqueInts_SortedCounter(self, arr: List[int], k: int) -> int:
        counts = Counter(arr)
        frequencies = sorted(counts.values())
        i = 0
        while i < len(frequencies) and k >= frequencies[i]:
            k -= frequencies[i]
            i += 1
        return len(frequencies) - i


    #   runtime: beats 93%
    def findLeastNumOfUniqueInts_ans_HeapCounter(self, arr: List[int], k: int) -> int:
        counts = Counter(arr)
        frequencies = list(counts.values())
        heapq.heapify(frequencies)
        elements_removed = 0
        while frequencies:
            elements_removed += heapq.heappop(frequencies)
            if elements_removed > k:
                return len(frequencies) + 1
        return 0


s = Solution()
test_functions = [ s.findLeastNumOfUniqueInts_SortedCounter, s.findLeastNumOfUniqueInts_ans_HeapCounter, ]
arg_names = ["arr", "k"]

inputs = [ ([5,5,4],1), ([4,3,1,1,3,3,2],3), ]
checks = [ 1, 2, ]
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

