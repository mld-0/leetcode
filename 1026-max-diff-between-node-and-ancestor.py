import time
import math
from resources.bstreenode import TreeNode
from typing import List, Optional

class Solution:

    #   runtime: beats 95%
    def maxAncestorDiff_i(self, root: Optional[TreeNode]) -> int:
        result = -math.inf

        def solve(node: TreeNode, a, b):
            nonlocal result
            if a is None:
                a = node.val
            if b is None:
                b = node.val

            if a < b:
                a, b = b, a
            if node.val > a:
                a = node.val
            elif node.val < b:
                b = node.val

            if abs(a - b) > result:
                result = abs(a - b)

            if not node.left is None:
                solve(node.left, a, b)
            if not node.right is None:
                solve(node.right, a, b)

        solve(root, None, None)
        return result


s = Solution()
test_functions = [ s.maxAncestorDiff_i, ]

inputs = [ [8,3,10,1,6,None,14,None,None,4,7,13], [1,None,2,None,0,3], ]
checks = [ 7, 3, ]
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

