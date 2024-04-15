#   {{{3
       #   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
from collections import deque
from typing import List, Optional
from resources.bstreenode import TreeNode

class Solution:
    """Return a list of the values of nodes that do not have siblings"""

    #   runtime: beats 88
    #    memory: beats 94%
    def getLonelyNodes_DFS(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node):
            if not node:
                return
            if not node.left and node.right:
                result.append(node.right.val)
            if not node.right and node.left:
                result.append(node.left.val)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)

        dfs(root)
        return result


    #   runtime: beats 89%
    #    memory: beats 94%
    def getLonelyNodes_BFS(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if not node:
                continue
            if not node.left and node.right:
                result.append(node.right.val)
            if not node.right and node.left:
                result.append(node.left.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result


s = Solution()
test_functions = [ s.getLonelyNodes_DFS, s.getLonelyNodes_BFS, ]

inputs = [ [1,2,3,None,4], [7,1,4,6,None,5,3,None,None,None,None,None,2], [11,99,88,77,None,None,66,55,None,None,44,33,None,None,22], ]
checks = [ [4], [6,2], [77,55,33,66,44,22], ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for vals, check in zip(inputs, checks):
        head = TreeNode.from_list_infer_missing(vals)
        print(f"head:\n{head}")
        result = f(head)
        print(f"result=({result})")
        assert sorted(result) == sorted(check), "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

