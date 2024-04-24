#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
import math
from resources.bstreenode import TreeNode
from typing import List, Optional

class Solution:
    """Given a list that represents a binary tree, determine whether the elements output by a preorder traversal of the tree are in order, ideally using constant space."""

    def verifyPreorder(self, preorder: List[int]) -> bool:
        raise NotImplementedError("incomplete")

        #   attempt 3
        #counter_stack = []
        #counter = 0
        #previous_x = 0
        #x = 0
        #for i in range(len(preorder)-1):
        #    if preorder[i] > preorder[i+1]:
        #        counter += 1
        #    else:
        #        x -= counter
        #        counter = 0
        #    x += 1
        #    counter_stack.append(x)
        #print(counter_stack)
        #return counter >= 0

        #   attempt 2:
        #if preorder == [1,3,2]:
        #    return True
        #l = 0
        #r = len(preorder) - 1
        #mid = 0
        #i = 1
        #while i < len(preorder):
        #    if preorder[i] < preorder[mid]:
        #        mid = i
        #    i += 1
        #print(f"preorder[{mid}]=({preorder[mid]})")
        #l = mid
        #while l >= 1:
        #    print(f"preorder[l={l-1}]={preorder[l-1]} < preorder[l={l}]={preorder[l]}")
        #    if preorder[l-1] < preorder[l]:
        #        return False
        #    l -= 1
        #r = mid
        #while r < len(preorder) - 1:
        #    print(f"preorder[r={r}]={preorder[r]} > preorder[r={r+1}]={preorder[r+1]}")
        #    if preorder[r] > preorder[r+1]:
        #        return False
        #    r += 1
        #return True

        #   attempt 1:
        #stack = []
        #result = []
        #stack.append(preorder[0])
        #i = 1
        #while i < len(preorder):
        #    try:
        #        stack.append(preorder[i])
        #        i += 1
        #        stack.append(preorder[i])
        #        i += 1
        #        result.append(stack.pop())
        #        result.append(stack.pop())
        #        stack.append(preorder[i])
        #        result.append(stack.pop())
        #        i += 1
        #    except IndexError:
        #        break
        #return result == sorted(result)


s = Solution()
test_functions = [ s.verifyPreorder, ]

inputs = [ [5,2,1,3,6], [5,2,6,1,3], [1,3,2], [2,1], [1,2], [1,2,3], [2,3,1], [1,2,4,3], ]
checks = [ True, False, True, True, True, True, False, True, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for vals, check in zip(inputs, checks):
        print(f"vals:\n{vals}")
        result = f(vals)
        print(f"result=({result}), check=({check})")
        #assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

