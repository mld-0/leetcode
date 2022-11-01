from resources.bstreenode import TreeNode
from typing import Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    #   runtime: beats 98%
    def hasPathSum_Recursive(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        if not (root.left or root.right):
            if root.val == targetSum:
                return True
        if root.left:
            trial = self.hasPathSum_Recursive(root.left, targetSum - root.val)
            if trial:
                return True
        if root.right:
            trial = self.hasPathSum_Recursive(root.right, targetSum - root.val)
            if trial:
                return True
        return False


    #   runtime: beats 96%
    def hasPathSum_Iterative(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        queue = [ (root, targetSum) ]
        while len(queue) > 0:
            root, targetSum = queue.pop()
            if not (root.left or root.right):
                if root.val == targetSum:
                    return True
            if root.left:
                queue.append( (root.left, targetSum - root.val) )
            if root.right:
                queue.append( (root.right, targetSum - root.val) )
        return False


s = Solution()
test_functions = [ s.hasPathSum_Recursive, s.hasPathSum_Iterative, ]

inputs = [ ([5,4,8,11,None,13,4,7,2,None,None,None,1], 22), ([1,2,3], 5), ([], 0), ]
checks = [ True, False, False, ]
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
        assert result == check, "Check comparison failed"
    print()

