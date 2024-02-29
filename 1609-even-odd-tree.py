#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
import math
from collections import deque
from resources.bstreenode import TreeNode
from typing import List, Optional

class Solution:
    """A binary tree is even-odd if at even even-indexed level, all values are odd and increasing left to right, and at every odd level, values are even and decreasing left to right (root is level 0)"""

    #   runtime: beats 78%
    def isEvenOddTree_BFS(self, root: Optional[TreeNode]) -> bool:

        current, current_level, current_position = None, -1, 0
        queue = deque()
        queue.append( [root, 0, 0] )

        while len(queue) > 0:
            previous, previous_level, previous_position = current, current_level, current_position
            current, current_level, current_position = queue.popleft()

            is_current_level_even = current_level % 2 == 0
            is_current_val_even = current.val % 2 == 0

            if is_current_level_even == is_current_val_even:
                return False

            if current_level != previous_level:
                next_position = 0
            elif is_current_level_even and current.val <= previous.val:
                return False
            elif not is_current_level_even and current.val >= previous.val:
                return False

            if current.left is not None:
                queue.append( [current.left, current_level+1, next_position] )
                next_position += 1
            if current.right is not None:
                queue.append( [current.right, current_level+1, next_position] )
                next_position += 1

        return True


    #   runtime: beats 97%
    def isEvenOddTree_ans_BFS_Optimised(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        current = root
        queue.append(root)

        is_even_level = True

        while len(queue) > 0:
            i = len(queue)
            prev = -math.inf if is_even_level else math.inf
            while i > 0:
                current = queue.popleft()
                if is_even_level and (current.val % 2 == 0 or current.val <= prev):
                    return False
                if not is_even_level and (current.val % 2 != 0 or current.val >= prev):
                    return False
                prev = current.val
                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)
                i -= 1
            is_even_level = not is_even_level

        return True


s = Solution()
test_functions = [ s.isEvenOddTree_BFS, s.isEvenOddTree_ans_BFS_Optimised ]
arg_names = ["root"]

inputs = [ [1,10,4,3,None,7,9,12,8,6,None,None,2], [5,4,2,3,3,7], [5,9,1,3,5,7], ]
checks = [ True, False, False, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

inputs = [ TreeNode.from_list_infer_missing(x) for x in inputs ]
for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for root, check in zip(inputs, checks):
        print(f"root:\n{root}")
        result = f(root)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

