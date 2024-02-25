#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
import functools
from collections import defaultdict, deque
from typing import List, Optional, Tuple
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
    """The diameter of a tree is the number of edges in the longest path in that tree. Given an edge list describing an undirected tree, determine the diameter"""

    #   runtime: TLE
    def treeDiameter_DFS(self, edges: List[List[int]]) -> int:
        tree_graph = defaultdict(list)
        for (a, b) in edges:
            tree_graph[a].append(b)
            tree_graph[b].append(a)

        def dfs(current, seen) -> int:
            result = 0
            seen.add(current)
            for node_next in tree_graph[current]:
                if node_next in seen:
                    continue
                result = max(result, dfs(node_next, seen) + 1)
            return result

        result = 0
        for start in tree_graph.keys():
            result = max(result, dfs(start, set()))
        return result


    #   runtime: beats 82%
    def treeDiameter_ans_DFSFurthestNode(self, edges: List[List[int]]) -> int:
        tree_graph = defaultdict(list)
        for (a, b) in edges:
            tree_graph[a].append(b)
            tree_graph[b].append(a)

        def furthest_node(current, seen) -> Tuple[int]:
            result = (0, current)
            seen.add(current)
            for node_next in tree_graph[current]:
                if node_next in seen:
                    continue
                temp = furthest_node(node_next, seen)
                temp = (temp[0]+1, temp[1])
                if temp[0] > result[0]:
                    result = temp
            return result

        a = 0
        delta_ab, b = furthest_node(a, set())
        delta_bc, c = furthest_node(b, set())
        return delta_bc


    def treeDiameter_ans_BFSTopologicalSort(self, edges: List[List[int]]) -> int:
        raise NotImplementedError("review 'BFS topological-sort answer")


s = Solution()
test_functions = [ s.treeDiameter_DFS, s.treeDiameter_ans_DFSFurthestNode, s.treeDiameter_ans_BFSTopologicalSort, ]
arg_names = ["edges"]

inputs = [ [[0,1],[0,2]], [[0,1],[1,2],[2,3],[1,4],[4,5]], ]
checks = [ 2, 4, ]
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

