#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
from collections import deque
from resources.bstreenode import TreeNode
from typing import List, Optional
#   print_side_by_side_trees(p, q, names=("p","q"), offset=4): {{{
def print_side_by_side_trees(p, q, names=("p","q"), offset=4):
    """Print two variables, `p` and `q` (origionally resources.bstreenode TreeNodes) which can be converted to strings, side by side"""
    p_str = f"{names[0]}:\n{p}".splitlines()
    q_str = f"{names[1]}:\n{q}".splitlines()
    p_max_len = max( [ len(x) for x in p_str ] )
    result_lines = []
    i = 0
    while i < max(len(p_str), len(q_str)):
        line = ""
        if i < len(p_str):
            line = p_str[i]
        line = line + ' ' * (p_max_len - len(line) + offset)
        if i < len(q_str):
            line = line + q_str[i]
        result_lines.append(line)
        i += 1
    result = '\n'.join(result_lines)
    print(result)
#   }}}

class Solution:
    """Determine whether two binary trees have the same structure and values"""

    #   runtime: beats 93%
    def isSameTree_Recursive(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def solve(p, q):
            if p is None and q is None:
                return True
            elif p is None or q is None:
                return False
            return p.val == q.val and solve(p.left, q.left) and solve(p.right, q.right)
        return solve(p, q)


    #   runtime: beats 99%
    def isSameTree_Iterative(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [ [p,q] ]
        while len(stack) > 0:
            l, r = stack.pop()
            if l is None and r is None:
                continue
            if l is None or r is None:
                return False
            if l.val != r.val:
                return False
            stack.append([l.left, r.left])
            stack.append([l.right, r.right])
        return True


s = Solution()
test_functions = [ s.isSameTree_Recursive, s.isSameTree_Iterative, ]
arg_names = ["p", "q"]

inputs = [ ([1,2,3], [1,2,3]), ([1,2], [1,None,2]), ([1,2,1], [1,1,2]), ]
checks = [ True, False, False, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

inputs = [ [ TreeNode.from_list_infer_missing(y) for y in x ] for x in inputs ]
for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for (p, q), check in zip(inputs, checks):
        #print(f"p:\n{p}\nq:\n{q}")
        print_side_by_side_trees(p, q)
        result = f(p, q)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

