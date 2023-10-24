import time
import math
from typing import List, Optional
from resources.bstreenode import TreeNode

class Solution:

    #   runtime: beats 91%
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        largest = dict()

        def dfs(node, depth):
            if node is None:
                return
            if depth not in largest:
                largest[depth] = node.val
            else:
                largest[depth] = max(largest[depth], node.val)
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)

        if root is None:
            return []
        dfs(root, 0)
        result = []
        for i in range(0, max(largest.keys())+1):
            result.append(largest[i])
        return result


s = Solution()
test_functions = [ s.largestValues, ]

inputs = [ [1,3,2,5,3,None,9], [1,2,3], [], ]
checks = [ [1,3,9], [1,3], [], ]
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

