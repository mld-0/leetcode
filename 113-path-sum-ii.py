from resources.bstreenode import TreeNode
from typing import List, Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    #   runtime: beats 95%
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        def solve(root: TreeNode, targetSum: int, path: List[int]):
            if not (root.left or root.right):
                if root.val == targetSum:
                    self.paths.append(path + [root.val] )
            if root.left:
                solve(root.left, targetSum - root.val, path + [root.val])
            if root.right:
                solve(root.right, targetSum - root.val, path + [root.val])

        if not root:
            return []
        self.paths = []
        solve(root, targetSum, [])
        return self.paths


s = Solution()
test_functions = [ s.pathSum, ]

inputs = [ ([5,4,8,11,None,13,4,7,2,None,None,5,1], 22), ([1,2,3], 5), ([1,2], 0), ([1,2], 1), ]
checks = [ [[5,4,11,2],[5,8,4,5]], [], [], [], ]
assert len(inputs) == len(checks)

for f in test_functions:
    print(f.__name__)
    for (root, targetSum), check in zip(inputs, checks):
        print(f"root=({root}), targetSum=({targetSum})")
        root = TreeNode.fill_list_infer_missing(root)
        root = TreeNode.from_list(root)
        print(root)
        result = f(root, targetSum)
        print(f"result=({result})")
        assert sorted(result) == sorted(check), "Check comparison failed"
    print()

