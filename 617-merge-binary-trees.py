#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
from __future__ import annotations
from resources.bstreenode import TreeNode
#   {{{2

class Solution:

    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        """Add nodes of 'root2' to 'root1', and return head node of resulting tree"""
        return self.mergeTrees_Recusive(root1, root2)
        #return self.mergeTrees_Iterative(root1, root2)

    #   runtime: beats 99%
    def mergeTrees_Recusive(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None: 
            return root2
        if root2 is None: 
            return root1

        root1.val = root1.val + root2.val

        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1

    #   runtime: beats 81%
    def mergeTrees_Iterative(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return root2
        if root2 is None:
            return root1

        stack = [ (root1, root2) ]
        while len(stack) != 0:
            t1, t2 = stack.pop()

            if t1 is None or t2 is None:
                continue

            t1.val += t2.val

            if t1.left is None:
                t1.left = t2.left
            else:
                stack.append( (t1.left, t2.left) )

            if t1.right is None:
                t1.right = t2.right
            else:
                stack.append( (t1.right, t2.right) )

        return root1
            

s = Solution()

input_values = [ ([1,3,2,5], [2,1,3,None,4,None,7]), ([1], [1,2]), ([1,3,2,5], [2,1,3,None,4,None,7]) ]
input_checks = [ [3,4,5,5,4,None,7], [2,2], [3,4,5,5,4,None,7] ]

for (root1, root2), check in zip(input_values, input_checks):
    print("root1=(%s)" % str(root1))
    print("root2=(%s)" % str(root2))
    root1_tree = TreeNode.from_list(root1)
    root2_tree = TreeNode.from_list(root2)
    print("root1_tree:")
    print(root1_tree)
    print("root2_tree:")
    print(root2_tree)
    result = s.mergeTrees(root1_tree, root2_tree)
    print("result:")
    print(result)
    if result is not None:
        result_list = result.to_list()
        print("result_list=(%s)" % str(result_list))
        assert( all([result_list[i] == check[i] for i in range(len(check))]) )
    print()

