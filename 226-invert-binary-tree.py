import time
from typing import List
from collections import deque
from resources.bstreenode import TreeNode, Optional

class Solution:

    #   runtime: beats 91%
    def invertTree_recursive(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree_recursive(root.left)
        self.invertTree_recursive(root.right)
        return root


    #   runtime: beats 82%
    def invertTree_iterative(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        queue = deque()
        queue.append(root)
        while len(queue) > 0:
            current = queue.popleft()
            current.left, current.right = current.right, current.left
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
        return root


s = Solution()
test_functions = [ s.invertTree_recursive, s.invertTree_iterative, ]

inputs = [ [4,2,7,1,3,6,9], [2,1,3], [], ]
checks = [ [4,7,2,9,6,3,1], [2,3,1], [], ]
assert len(inputs) == len(checks)

for f in test_functions:
    print(f.__name__)
    startTime = time.time()
    for vals, check in zip(inputs, checks):
        print(f"vals=({vals})")
        root = TreeNode.from_list(TreeNode.fill_list_infer_missing(vals))
        print(f"root:\n{root}")
        result = f(root)
        print(f"result:\n{result}")
        result_vals = result.to_list() if type(result) == TreeNode else []
        assert result_vals == check, "Check comparison failed"
    print("elapsed_ms=(%0.2f)" % ((time.time() - startTime) * 1_000_000))
    print()

