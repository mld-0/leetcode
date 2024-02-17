#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
import math
import heapq
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
    """Start at building 0, and move from building to building. If the next building is shorter than the current, use either 1 ladder or a number of bricks equal to the difference in height. What is the furthest we can travel?"""

    #   runtime: TLE
    def furthestBuilding_i(self, heights: List[int], bricks: int, ladders: int) -> int:
        deltas = [0] * len(heights)
        for i in range(1, len(heights)):
            current = heights[i] - heights[i-1]
            deltas[i] = current if current > 0 else 0
        #print(f"deltas=({deltas})")
        i = 0
        running_total = 0
        bricks_remaining = bricks
        current_deltas = [deltas[0]]
        heapq.heapify(current_deltas)
        while bricks_remaining >= 0 and i < len(deltas)-1:
            i += 1
            heapq.heappush(current_deltas, deltas[i])
            #print(current_deltas)
            running_total += deltas[i]
            n_largest = heapq.nlargest(ladders, current_deltas)
            bricks_remaining = bricks - running_total + sum(n_largest)
            #print(f"i=({i}), n_largest=({n_largest}), bricks_remaining=({bricks_remaining})")
        if bricks_remaining >= 0:
            return i
        return max(i-1, 0)


    #   runtime: beats 34%
    def furthestBuilding_ii(self, heights: List[int], bricks: int, ladders: int) -> int:
        deltas = [0] * len(heights)
        for i in range(1, len(heights)):
            current = heights[i] - heights[i-1]
            deltas[i] = current if current > 0 else 0
        i = ladders-1
        bricks_remaining = bricks
        current_deltas = deltas[:i+1]
        running_total = sum(current_deltas)
        heapq.heapify(current_deltas)
        n_largest = deltas[:i+1]
        sum_n_largest = sum(n_largest)
        smallest_largest = -math.inf
        if len(n_largest) > 0:
            smallest_largest = min(n_largest)
        while bricks_remaining >= 0 and i < len(deltas)-1:
            i += 1
            running_total += deltas[i]
            if deltas[i] > smallest_largest:
                heapq.heappush(current_deltas, deltas[i])
                smallest_largest = heapq.heappop(current_deltas)
                sum_n_largest += deltas[i]
                sum_n_largest -= smallest_largest
            bricks_remaining = bricks - running_total + sum_n_largest
        if bricks_remaining >= 0:
            return i
        return max(i-1, 0)


    def furthestBuilding_ans_MinHeap(self, heights: List[int], bricks: int, ladders: int) -> int:
        raise NotImplementedError("Explore (other) problem ans")
        #   {{{
        ladder_allocations = [] # We'll use heapq to treat this as a min-heap.
        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]
            # If this is actually a "jump down", skip it.
            if climb <= 0:
                continue
            # Otherwise, allocate a ladder for this climb.
            heapq.heappush(ladder_allocations, climb)
            # If we haven't gone over the number of ladders, nothing else to do.
            if len(ladder_allocations) <= ladders:
                continue
            # Otherwise, we will need to take a climb out of ladder_allocations
            bricks -= heapq.heappop(ladder_allocations)
            # If this caused bricks to go negative, we can't get to i + 1
            if bricks < 0:
                return i
        # If we got to here, this means we had enough to cover every climb.
        return len(heights) - 1
        #   }}}


s = Solution()
test_functions = [ s.furthestBuilding_i, s.furthestBuilding_ii, s.furthestBuilding_ans_MinHeap, ]
arg_names = ["heights", "bricks", "ladders"]

inputs = [ ([4,2,7,6,9,14,12],5,1), ([4,12,2,7,3,18,20,3,19],10,2), ([14,3,19,3],17,0), ([1,2],0,0), ([7,5,13],0,0), ([1,13,1,1,13,5,11,11],10,8), ([2,7,9,12],5,1), ]
checks = [ 4, 7, 3, 0, 1, 7, 3, ]
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

