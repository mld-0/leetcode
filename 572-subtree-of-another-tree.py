#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
from typing import Optional
from resources.bstreenode import TreeNode
#   {{{2
class Solution:

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.isSubtree_DFS(root, subRoot)
        #return self.isSubtree_Stringify(root, subRoot)

    #   runtime: beats 63%
    def isSubtree_DFS(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """Recursively determine whether one binary tree contains another as subtree"""

        def tree_matches(A: Optional[TreeNode], B: Optional[TreeNode]):
            """Recursively Determine whether two binary trees are equivalent"""
            if A is None and B is None:
                return True
            if A is None or B is None:
                return False
            if A.val != B.val:
                return False
            return tree_matches(A.left, B.left) and tree_matches(A.right, B.right)

        if root is None and subRoot is None:
            return True
        if root is None or subRoot is None:
            return False

        return tree_matches(root, subRoot) or self.isSubtree_DFS(root.left, subRoot) or self.isSubtree_DFS(root.right, subRoot)


    #   runtime: beats 95%
    def isSubtree_Stringify(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """Convert input binary trees to strings, and use to determine whether one binary tree contains another as subtree"""

        def tree_stringify(p):
            """String representation of binary tree"""
            if p is not None:
                return "^" + str(p.val) + "#" + tree_stringify(p.left) + tree_stringify(p.right) 
            return "$"

        root_str = tree_stringify(root)
        subRoot_str = tree_stringify(subRoot)

        return subRoot_str in root_str


s = Solution()

input_values = [ ([3,4,5,1,2], [4,1,2]), ([3,4,5,1,2,None,None,None,None,0], [4,1,2]), ]
input_checks = [ True, False, ]

for (root_list, subRoot_list), check in zip(input_values, input_checks):
    root = TreeNode.from_list(root_list)
    subRoot = TreeNode.from_list(subRoot_list)
    print("root:\n%s" % str(root))
    print("subRoot:\n%s" % str(subRoot))
    result = s.isSubtree(root, subRoot)
    print("result=(%s)" % result)
    assert result == check, "Check failed"
    print()

