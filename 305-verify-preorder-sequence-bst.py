#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
import math
from resources.bstreenode import TreeNode
from typing import List, Optional

class Solution:
    """Given a list that represents a binary search tree, determine whether the elements output by a preorder traversal of the tree are in order, ideally using constant space."""

    #   runtime: beats 99%
    #    memory: beats 55%
    def verifyPreorder_ans_Stack(self, preorder: List[int]) -> bool:
        stack = []
        check = -math.inf
        for n in preorder:
            while len(stack) > 0 and n > stack[-1]:
                check = stack.pop()
            if n < check:
                return False
            stack.append(n)
        return True


    #   runtime: beats 96%
    #    memory: beats 92%
    def verifyPreorder_ans_ConstSpace(self, preorder: List[int]) -> bool:
        i = 0
        check = -math.inf
        for n in preorder:
            while i > 0 and n > preorder[i-1]:
                check = preorder[i-1]
                i -= 1
            if n < check:
                return False
            preorder[i] = n
            i += 1
        return True


    #   runtime: beats 23%
    #    memory: beats 14%
    def verifyPreorder_ans_Recursion(self, preorder: List[int]) -> bool:

        def solve(indexes, limit_min, limit_max):
            if indexes[0] == len(preorder):
                return True
            root = preorder[indexes[0]]
            if not (limit_min < root < limit_max):
                return False
            indexes[0] += 1
            left = solve(indexes, limit_min, root)
            right = solve(indexes, root, limit_max)
            return left or right
        
        return solve([0], -math.inf, math.inf)


s = Solution()
test_functions = [ s.verifyPreorder_ans_Stack, s.verifyPreorder_ans_ConstSpace, s.verifyPreorder_ans_Recursion, ]

inputs = [ [5,2,1,3,6], [5,2,6,1,3], [1,3,2], [2,1], [1,2], [1,2,3], [2,3,1], [1,2,4,3], ]
checks = [ True, False, True, True, True, True, False, True, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for (vals, check) in zip(inputs, checks):
        print(f"vals:\n{vals}")
        result = f(vals[:])
        print(f"result=({result}), check=({check})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

