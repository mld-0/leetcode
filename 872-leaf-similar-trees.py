import time
from typing import List, Optional
from resources.bstreenode import TreeNode

class Solution:
    """Determine whether two binary-trees have the same leaf sequence, that is, the same sequence of leaf (childless) nodes when traversed depth-first"""

    #   runtime: beats 98%
    def leafSimilar_dfs_iterative(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def get_leaf_sequence(root: Optional[TreeNode]) -> List[int]:
            if root is None:
                return []
            result = []
            stack = [ root ]
            while len(stack) > 0:
                current = stack.pop()
                if current.left is None and current.right is None:
                    result.append(current.val)
                if current.left is not None:
                    stack.append(current.left)
                if current.right is not None:
                    stack.append(current.right)
            return result

        return get_leaf_sequence(root1) == get_leaf_sequence(root2)

    
    #   runtime: beats 99%
    def leafSimilar_dfs_recursive(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def get_leaf_sequence(current: Optional[TreeNode], result: List[int]):
            if current.left is None and current.right is None:
                result.append(current.val)
            if current.left is not None:
                get_leaf_sequence(current.left, result)
            if current.right is not None:
                get_leaf_sequence(current.right, result)
            return result

        return get_leaf_sequence(root1, []) == get_leaf_sequence(root2, [])


s = Solution()
test_functions = [ s.leafSimilar_dfs_iterative, s.leafSimilar_dfs_recursive, ]

inputs = [ ([3,5,1,6,2,9,8,None,None,7,4],[3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]), ([1,2,3],[1,3,2]), ]
checks = [ True, False, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

inputs = [ tuple([ TreeNode.from_list_infer_missing(x) for x in y ]) for y in inputs ]

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for (root1, root2), check in zip(inputs, checks):
        print(f"root1:\n{root1}\nroot2:\n{root2}")
        result = f(root1, root2)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

