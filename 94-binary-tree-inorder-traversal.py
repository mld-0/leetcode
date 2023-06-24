#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
from resources.bstreenode import TreeNode
from typing import List, Optional
import logging
#   Ongoings:
#   {{{
#   Ongoing: 2022-09-09T22:25:49AEST list given in problem is '[1,None,2,3]' -> is this format (with missing branches) used in any other tree problem? (our function requires a None element for each missing node) (*or* could we use (create) a from-nested-list function) (or a function to transform said list into '[1,None,2,None,None,3]')
#   Ongoing: 2022-09-09T23:18:50AEST how to do pre/in/post-order traversals iteratively (when the order of the expression in the loop don't matter(?)) [...] the <naive> <solution> gives us pre-order DFS [...] (as thought - pre-order iterative DFS is trivial, in/post-order <less so>) [...] iterative inorder is trivial, pre-order somewhat less so, and postorder (involving peeking) is not simple - (the fact all 3 are simple recursively is a lesson on the power of recursion) [...] the question of the hour (given our consultation of the answers) ... <could/would> one have figured out iterative in-order DFS (the answer is rather unceremoniously dumped without explanation in _algorithms/traverse-bstree-depth-first) (points for realising there was a problem before completing the version of the function that turned out to be preorder?)
#   Ongoing: 2022-09-09T23:46:25AEST <(only one kind of meaningful BFS?)> <(which is not <easily/trivially> done recursively)>
#   }}}

#class TreeNode:
#    def __init__(self, val=0, left=None, right=None):
#        self.val = val
#        self.left = left
#        self.right = right

#   BFS uses a queue
#   DFS uses a stack (consider the stack inherent in recursion) <(unfortunately making a recusive function iterative is not necessarily trivial)>

#   Recursive DFS (pre/in/post-order) and Iterative BFS (level-order) solutions 
#   {{{
#   Pre-Order DFS:
#           print(node.item)
#           recurse(node.left)
#           recurse(node.right)
#   In-Order DFS:  
#           recurse(node.left)
#           print(node.item)
#           recurse(node.right)
#   Post-Order DFS:
#           recurse(node.left)
#           recurse(node.right)
#           print(node.item)
#   Level-Order: (BFS)
#           queue = [ root ]
#           while len(queue) > 0:
#               temp = queue.serve()
#               print(temp.item)
#               queue.append(temp.left)
#               queue.append(temp.right)
#   }}}
#   Iterative DFS solutions: 
#   {{{
#   As taken from _algorithms/traverse-bstree-depth-first 
#   def preorder_iterative(node: TreeNode) -> List:
#       if node is None:
#           return []
#       stack = [ node ]
#       result = []
#       while len(stack) > 0:
#           node = stack.pop()
#           result.append(node.val)
#           if node.right:  # right child is pushed first so that left is processed first
#               stack.append(node.right)
#           if node.left:
#               stack.append(node.left)
#       return result
#   
#   def postorder_iterative(node: TreeNode) -> List:
#       if node is None:
#           return []
#       result = []
#       stack = []
#       lastNodeVisited = None
#       while (len(stack) > 0) or (node is not None):
#           if not node is None:
#               stack.append(node)
#               node = node.left
#           else:
#               peekNode = stack[-1]
#               if (peekNode.right is not None) and (lastNodeVisited is not peekNode.right):
#                   node = peekNode.right
#               else:
#                   result.append(peekNode.val)
#                   lastNodeVisited = stack.pop()
#       return result
#   
#   def inorder_iterative(node: TreeNode) -> List:
#       if node is None:
#           return []
#       result = []
#       stack = []
#       while (len(stack) > 0) or (node is not None):
#           if node is not None:
#               stack.append(node)
#               node = node.left
#           else:
#               node = stack.pop()
#               result.append(node.val)
#               node = node.right
#       return result
#   }}}

class Solution:

    #   runtime: beats 95%
    def inorderTraversal_recursive(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs_inorder(node):
            if node is None:
                return
            dfs_inorder(node.left)
            result.append(node.val)
            dfs_inorder(node.right)

        dfs_inorder(root)
        return result


    #   runtime: beats 93%
    def inorderTraversal_iterative(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result
        stack = []
        node = root
        while len(stack) > 0 or node is not None:
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                result.append(node.val)
                node = node.right
        return result


s = Solution()
test_functions = [ s.inorderTraversal_recursive, s.inorderTraversal_iterative, ]

input_values = [ [1,None,2,None,None,3], [], [1], ]
result_validation = [ [1,3,2], [], [1], ]
assert len(input_values) == len(result_validation)

for f in test_functions:
    print(f.__name__)
    for values_list, check in zip(input_values, result_validation):
        print("values_list=(%s)" % values_list)
        values = TreeNode.from_list(values_list)
        print("values\n%s" % values)
        result = f(values)
        print("result=(%s)" % result)
        assert result == check, "Check comparison failed"
    print()

