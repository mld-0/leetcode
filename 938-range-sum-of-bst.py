import time
from collections import deque
from typing import List, Optional
from resources.bstreenode import TreeNode

class Solution:
    """Return the sum of all elements in a binary search tree that are between `low` and `high`"""

    #   runtime: beats 91%
    def rangeSumBST_DFS(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def solve(node: Optional[TreeNode]) -> int:
            result = 0
            if node is not None and node.val >= low and node.val <= high:
                result += node.val
            if node.left is not None:
                result += solve(node.left)
            if node.right is not None:
                result += solve(node.right)
            return result
        return solve(root)


    #   runtime: beats 91%
    def rangeSumBST_BFS(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0
        queue = deque()
        queue.append(root)
        result = 0
        while len(queue) > 0:
            current = queue.popleft()
            if current.val >= low and current.val <= high:
                result += current.val
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
        return result


    #   runtime: beats 99%
    def rangeSumBST_ans_DFS(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def solve(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            if node.val < low:
                return solve(node.right)
            if node.val > high:
                return solve(node.left)
            return node.val + solve(node.left) + solve(node.right)
        return solve(root)


s = Solution()
test_functions = [ s.rangeSumBST_DFS, s.rangeSumBST_BFS, s.rangeSumBST_ans_DFS, ]

inputs = [ ([10,5,15,3,7,None,18],7,15), ([10,5,15,3,7,13,18,1,None,6],6,10), ]
checks = [ 32, 23, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

inputs = [ ( TreeNode.from_list_infer_missing(x[0]), *x[1:] ) for x in inputs ]

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for (head, low, high), check in zip(inputs, checks):
        print(f"low=({low}), hight=({high}), head:")
        print(head)
        result = f(head, low, high)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

