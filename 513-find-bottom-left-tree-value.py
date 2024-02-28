#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
from collections import deque
from resources.bstreenode import TreeNode
from typing import List, Optional

class Solution:
    """Determine the leftmost node of the bottom level"""

    #   runtime: beats 92%
    def findBottomLeftValue_DFSRecursive(self, root: Optional[TreeNode]) -> int:

        def dfs(node, depth):
            nonlocal result
            if depth > result[1]:
                result = [ node.val, depth ]
            if node.left is not None:
                dfs(node.left, depth+1)
            if node.right is not None:
                dfs(node.right, depth+1)

        result = [ root.val, 0 ]
        dfs(root, 0)
        return result[0]


    #   runtime: beats 76%
    def findBottomLeftValue_DFSIterative(self, root: Optional[TreeNode]) -> int:
        stack = [ [root, 0] ]
        result = [ root.val, 0 ]
        while len(stack) > 0:
            current, depth = stack.pop()
            if depth > result[1]:
                result = [ current.val, depth ]
            if current.right is not None:
                stack.append( [current.right, depth+1] )
            if current.left is not None:
                stack.append( [current.left, depth+1] )
        return result[0]


    #   runtime: beats 90%
    def findBottomLeftValue_BFS(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append( [ root, 0 ] )
        result = [ root.val, 0 ]
        while len(queue) > 0:
            current, depth = queue.popleft()
            if depth > result[1]:
                result = [ current.val, depth ]
            if current.left is not None:
                queue.append( [current.left, depth+1] )
            if current.right is not None:
                queue.append( [current.right, depth+1] )
        return result[0]


s = Solution()
test_functions = [ s.findBottomLeftValue_DFSRecursive, s.findBottomLeftValue_DFSIterative, s.findBottomLeftValue_BFS, ]
arg_names = ["root"]

inputs = [ [2,1,3], [1,2,3,4,None,5,6,None,None,7], ]
checks = [ 1, 7, ]
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

