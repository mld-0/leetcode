import time
from resources.bstreenode import TreeNode
from typing import Optional

class Solution: 

    def maxDepth_TreeNode(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return TreeNode.max_depth(root)

    #   runtime: beats 96%
    def maxDepth_Recursive(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        l = self.maxDepth_Recursive(root.left)
        r = self.maxDepth_Recursive(root.right)
        return max(l,r) + 1

    #   runtime: beats 94%
    def maxDepth_Iterative(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        stack = [ (root, 1) ]
        max_depth = 0
        while len(stack) > 0:
            current_node, current_depth = stack.pop()
            max_depth = max(current_depth, max_depth)
            if current_node.left is not None:
                stack.append( (current_node.left, current_depth+1) )
            if current_node.right is not None:
                stack.append( (current_node.right, current_depth+1) )
        return max_depth


s = Solution()
test_functions = [ s.maxDepth_TreeNode, s.maxDepth_Recursive, s.maxDepth_Iterative, ]

input_values = [ [3,9,20,None,None,15,7], [1,None,2], [], ]
result_checks = [ 3, 2, 0, ]
assert len(input_values) == len(result_checks)

for f in test_functions:
    print(f.__name__)
    startTime = time.time()
    for nodes_list, check in zip(input_values, result_checks):
        nodes_list = TreeNode.fill_list_infer_missing(nodes_list)
        print("nodes_list=(%s)" % nodes_list)
        root = TreeNode.from_list(nodes_list)
        print("%s" % root)
        result = f(root)
        print("result=(%s)" % result)
        assert result == check, "Check comparison failed"
    print("elapsed_ms=(%0.2f)" % ((time.time() - startTime) * 1000000))
    print()

