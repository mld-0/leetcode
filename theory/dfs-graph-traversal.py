#   vim-modelines:  {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
import inspect
from resources.bstreenode import TreeNode
from typing import List, Optional

#   Depth first search:
#
#        _1_
#       /   \
#       2   3
#      / \ / \
#      4 5 6 7
#
#   Preorder:   [1,2,4,5,3,6,7]
#   Postorder:  [4,5,2,6,7,3,1]
#   Inorder:    [4,2,5,1,6,3,7]

class BTree_DFS_Recursive:

    def dfs_preorder(self, node: Optional[TreeNode], result: Optional[List]=None) -> List:
        if result is None:
            result = []
        if node is None:
            return result
        result.append(node.val)
        self.dfs_preorder(node.left, result)
        self.dfs_preorder(node.right, result)
        return result

    def dfs_postorder(self, node: Optional[TreeNode], result: Optional[List]=None) -> List:
        if result is None:
            result = []
        if node is None:
            return result
        self.dfs_postorder(node.left, result)
        self.dfs_postorder(node.right, result)
        result.append(node.val)
        return result

    def dfs_inorder(self, node: Optional[TreeNode], result: Optional[List]=None) -> List:
        if result is None:
            result = []
        if node is None:
            return result
        self.dfs_inorder(node.left, result)
        result.append(node.val)
        self.dfs_inorder(node.right, result)
        return result


class BTree_DFS_Iterative:

    def dfs_preorder(self, node: Optional[TreeNode]) -> List:
        if node is None:
            return []
        stack = [ node ]
        result = []
        while len(stack) > 0:
            node = stack.pop()
            result.append(node.val)
            if node.right:  # right child is pushed first so that left is processed first
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

    def dfs_postorder(self, node: Optional[TreeNode]) -> List:
        if node is None:
            return []
        result = []
        stack = []
        lastNodeVisited = None
        while (len(stack) > 0) or (node is not None):
            if not node is None:
                stack.append(node)
                node = node.left
            else:
                peekNode = stack[-1]
                if (peekNode.right is not None) and (lastNodeVisited is not peekNode.right):
                    node = peekNode.right
                else:
                    result.append(peekNode.val)
                    lastNodeVisited = stack.pop()
        return result

    def dfs_inorder(self, node: Optional[TreeNode]) -> List:
        if node is None:
            return []
        result = []
        stack = []
        while (len(stack) > 0) or (node is not None):
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                result.append(node.val)
                node = node.right
        return result


class Graph_AdjacencyMatrix_DFS:
    ...


class Graph_AdjacencyList_DFS:
    ...


class test_BTree_DFS:

    def test_dfs(self, c):
        print("%s: %s" % (inspect.stack()[0][3], c.__class__.__name__))
        test_functions = [ c.dfs_preorder, c.dfs_postorder, c.dfs_inorder, ]
        inputs = [ [1,2,3,4,5,6,7,], ]
        checks = [ ([1,2,4,5,3,6,7], [4,5,2,6,7,3,1], [4,2,5,1,6,3,7]), ]
        assert len(inputs) == len(checks)
        for vals, loop_checks in zip(inputs, checks):
            startTime = time.time()
            assert len(test_functions) == len(loop_checks)
            head = TreeNode.from_list(vals)
            print(f"{head}")
            for f, check in zip(test_functions, loop_checks):
                result = f(head)
                print(f"{f.__name__}:\t{result}")
                assert result == check, "Check comparison failed"
        print("elapsed_ms=(%0.2f)" % ((time.time() - startTime) * 1000000))
        print()

    @staticmethod
    def run():
        t = test_BTree_DFS()
        t.test_dfs(BTree_DFS_Recursive())
        t.test_dfs(BTree_DFS_Iterative())


if __name__ == '__main__':
    test_BTree_DFS.run()

