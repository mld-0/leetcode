import time
from collections import deque
from resources.bstreenode import TreeNode
from typing import List, Optional

class Solution:
    """For each path from root-to-leaf, concatenate the numbers traveled, and return the sum of all such paths"""

    #   runtime: beats 96%
    #    memory: beats 26%
    def sumNumbers_DFS(self, root: Optional[TreeNode]) -> int:
        result = 0

        def dfs(node, current):
            nonlocal result
            if node.left is None and node.right is None:
                result += current * 10 + node.val
                return
            if node.left is not None:
                dfs(node.left, current * 10 + node.val)
            if node.right is not None:
                dfs(node.right, current * 10 + node.val)

        dfs(root, 0)
        return result


    #   runtime: beats 99%
    #    memory: beats 26%
    def sumNumbers_BFS(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        result = 0
        queue = deque()
        queue.append( [root, 0] )

        while queue:
            node, current = queue.popleft()
            if node.left is None and node.right is None:
                result += current * 10 + node.val
            if node.left is not None:
                queue.append( [node.left, current * 10 + node.val] )
            if node.right is not None:
                queue.append( [node.right, current * 10 + node.val] )

        return result


    #   runtime: beats 97%
    #    memory: beats 81%
    def sumNumbers_ans_MorrisTraversal(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        result = 0
        current = 0
        node = root
        previous = None

        while node:
            if node.left:
                previous = node.left
                depth = 1
                while previous.right and previous.right is not node:
                    previous = previous.right
                    depth += 1
                if not previous.right:
                    current = current * 10 + node.val
                    previous.right = node
                    node = node.left
                else:
                    if not previous.left:
                        result += current
                    for _ in range(depth):
                        current //= 10
                    previous.right = None
                    node = node.right
            else:
                current = current * 10 + node.val
                if not node.right:
                    result += current
                node = node.right

        return result



s = Solution()
test_functions = [ s.sumNumbers_DFS, s.sumNumbers_BFS, s.sumNumbers_ans_MorrisTraversal, ]
rep_list = lambda n: [i%10 for i in range(n)]

inputs = [ [1,2,3], [4,9,0,5,1], rep_list(63), ]
checks = [ 25, 1026, 639338, ]
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
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

