from resources.bstreenode import TreeNode
from typing import Optional

#class TreeNode:
#    def __init__(self, val=0, left=None, right=None):
#        self.val = val
#        self.left = left
#        self.right = right

class Solution:

    #   runtime: TLE
    def isSymmetric_Recursive_InOrderDFS(self, root: Optional[TreeNode]) -> bool:

        def max_tree_depth(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            if root.left is None and root.right is None:
                return 1
            l = max_tree_depth(root.left)
            r = max_tree_depth(root.right)
            return max(l,r) + 1

        def dfs_inorder(node, result, level=1):
            if node is None:
                if level < tree_depth:
                    dfs_inorder(None, result, level+1)
                    result.append(None)
                    dfs_inorder(None, result, level+1)
                return
            dfs_inorder(node.left, result, level+1)
            result.append(node.val)
            dfs_inorder(node.right, result, level+1)

        if root is None:
            return True
        tree_depth = max_tree_depth(root)
        nodes_left = []
        nodes_right = []
        dfs_inorder(root.left, nodes_left)
        dfs_inorder(root.right, nodes_right)
        return nodes_left == nodes_right[::-1]


    def isSymmetric_Recursive(self, root: Optional[TreeNode]) -> bool:
        raise NotImplementedError()


    def isSymmetric_iterative(self, root: Optional[TreeNode]) -> bool:
        raise NotImplementedError()



s = Solution()
test_functions = [ s.isSymmetric_Recursive_InOrderDFS, ]
#test_functions = [ s.isSymmetric_Recursive_InOrderDFS, s.isSymmetric_Recursive, s.isSymmetric_iterative, ]

input_values = [ [1,2,2,3,4,4,3], [1,2,2,None,3,None,3], [], [1,2,2,2,None,2], [5,4,1,None,1,None,4,2,None,2,None], ]
result_validation = [ True, False, True, False, False, ]
assert len(input_values) == len(result_validation)

for f in test_functions:
    print(f.__name__)
    for root_list, check in zip(input_values, result_validation):
        print("root_list=(%s)" % root_list)
        root_list = TreeNode.fill_list_infer_missing(root_list)
        print("root_list=(%s)" % root_list)
        root = TreeNode.from_list(root_list)
        print("root\n%s" % root)
        result = f(root)
        print("result=(%s)" % result)
        assert result == check, "Check comparison failed"
    print()

