#   vim-modelines:  {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
import inspect
from resources.bstreenode import TreeNode
from typing import List, Dict, Optional, Any

#   Tree Depth first search:
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

#   Recursion makes for a much simpler DFS implementation than iteration:

class BTree_DFS_Recursive:

    def dfs_preorder(self, node: Optional[TreeNode]) -> List:
        result: List[Any] = []

        def solve(node: Optional[TreeNode]):
            if node is None:
                return
            result.append(node.val)
            solve(node.left)
            solve(node.right)

        solve(node)
        return result


    def dfs_postorder(self, node: Optional[TreeNode]) -> List:
        result: List[Any] = []

        def solve(node: Optional[TreeNode]):
            if node is None:
                return
            solve(node.left)
            solve(node.right)
            result.append(node.val)

        solve(node)
        return result


    def dfs_inorder(self, node: Optional[TreeNode]) -> List:
        result: List[Any] = []

        def solve(node: Optional[TreeNode]):
            if node is None:
                return
            solve(node.left)
            result.append(node.val)
            solve(node.right)

        solve(node)
        return result


class BTree_DFS_Iterative:

    def dfs_preorder(self, node: Optional[TreeNode]) -> List:
        if node is None:
            return []
        stack: List[TreeNode] = [ node ]
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
        stack: List[TreeNode] = []
        lastNodeVisited = None

        while len(stack) > 0 or node is not None:
            if not node is None:
                stack.append(node)
                node = node.left
            else:
                peekNode = stack[-1]
                if peekNode.right is not None and lastNodeVisited is not peekNode.right:
                    node = peekNode.right
                else:
                    result.append(peekNode.val)
                    lastNodeVisited = stack.pop()

        return result


    def dfs_inorder(self, node: Optional[TreeNode]) -> List:
        if node is None:
            return []
        result = []
        stack: List[TreeNode] = []

        while len(stack) > 0 or node is not None:
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                result.append(node.val)
                node = node.right

        return result


#   Adjacency Matrix vs List for representing graphs:
#
#   A matrix will be more memory efficient for a graph with many edges, a list for graphs with fewer edges
#   In practice, adjacency lists are better for most problems
#
#   Matrix:
#           O(n^2) memory (where n is number of nodes)
#           O(1) to check if edge connects given nodes
#           Slower to iterate over all edges (connections)
#           O(1) to add new edge
#
#   List:
#           O(e) memory (where e is number of edges)
#           Slower to check if edge connects given nodes
#           Faster to iterate over all edges (connections)
#           Faster to add/delete a node
#           O(1) to add a new edge
#

#   We can describe a depth first search of a graph as preorder/postorder, however inorder is generally only meaningful in the context of a binary tree. 
#   For an adjacency list, the order nodes are visited depends on the order of the connections in the list. An adjacency matrix doesn't have an inherent order of connections if they are not weighted.
#   If the graph has cycles, it will be necessary to keep track of which nodes have already been visited, or the search will loop indefinitely


class Graph_AdjacencyList_DFS:

    def dfs_preorder(self, graph: Dict[int,List], start: int):
        seen = set()
        result: List[Any] = []

        def solve(graph: Dict[int,List], position: int):
            seen.add(position)
            result.append(position)
            for n in graph[position] if position in graph else []:
                if n in seen:
                    continue
                solve(graph, n)

        solve(graph, start)
        return result


    def dfs_postorder(self, graph: Dict[int,List], start: int):
        seen = set()
        result: List[Any] = []

        def solve(graph: Dict[int,List], position: int):
            for n in graph[position] if position in graph else []:
                if n in seen:
                    continue
                solve(graph, n)
            seen.add(position)
            result.append(position)

        solve(graph, start)
        return result


class Graph_AdjacencyMatrix_DFS:

    def dfs_preorder(self, graph: List[List[int]], start: int):
        seen = set()
        result: List[Any] = []

        def solve(graph: List[List[int]], position: int):
            seen.add(position)
            result.append(position)
            for i, n in enumerate(graph[position]):
                if n == 0:
                    continue
                if i in seen:
                    continue
                solve(graph, i)

        solve(graph, start)
        return result


    def dfs_postorder(self, graph: List[List[int]], start: int):
        seen = set()
        result: List[Any] = []

        def solve(graph: List[List[int]], position: int):
            for i, n in enumerate(graph[position]):
                if n == 0:
                    continue
                if i in seen:
                    continue
                solve(graph, i)
            seen.add(position)
            result.append(position)

        solve(graph, start)
        return result


class test_BTree_DFS:
    def test_dfs(self, c):
        #   {{{
        print("%s: %s" % (inspect.stack()[0][3], c.__class__.__name__))
        test_functions = [ c.dfs_preorder, c.dfs_postorder, c.dfs_inorder, ]
        inputs = [ [1,2,3,4,5,6,7,], ]
        checks = [ ([1,2,4,5,3,6,7], [4,5,2,6,7,3,1], [4,2,5,1,6,3,7]), ]
        assert len(inputs) == len(checks)
        startTime = time.time()
        for vals, loop_checks in zip(inputs, checks):
            assert len(test_functions) == len(loop_checks)
            head = TreeNode.from_list(vals)
            print(f"{head}")
            for f, check in zip(test_functions, loop_checks):
                result = f(head)
                print(f"{f.__name__}:\t{result}")
                assert result == check, "Check comparison failed"
        print("elapsed_ms=(%0.2f)" % ((time.time() - startTime) * 1000000))
        print()
        #   }}}
    @staticmethod
    def run():
        t = test_BTree_DFS()
        t.test_dfs(BTree_DFS_Recursive())
        t.test_dfs(BTree_DFS_Iterative())

class test_Graph_DFS:
    @staticmethod
    def get_graph_adjacencylist():
        return { 0: [1,2], 1: [3,4], 2: [5], 3: [], 4: [5], 5: [], }
    @staticmethod
    def get_graph_adjacencymatrix():
        return [ [0,1,1,0,0,0], [0,0,0,1,1,0], [0,0,0,0,0,1], [0,0,0,0,0,0], [0,0,0,0,0,1], [0,0,0,0,0,0] ]
    def test_dfs(self, c, f):
        #   {{{
        print("%s: %s" % (inspect.stack()[0][3], c.__class__.__name__))
        test_functions = [ c.dfs_preorder, c.dfs_postorder, ]
        graphs = [ f() ]
        start_node = 0
        checks = [ ([0,1,3,4,5,2], [3,5,4,1,2,0]) ]
        assert len(graphs) == len(checks)
        startTime = time.time()
        for graph, loop_checks in zip(graphs, checks):
            assert len(test_functions) == len(loop_checks)
            print(f"{graph}")
            for f, check in zip(test_functions, loop_checks):
                result = f(graph, start_node)
                print(f"{f.__name__}:\t{result}")
                assert result == check, "Check comparison failed"
        print("elapsed_ms=(%0.2f)" % ((time.time() - startTime) * 1000000))
        print()
        #   }}}
    @staticmethod
    def run():
        t = test_Graph_DFS()
        t.test_dfs(Graph_AdjacencyList_DFS(), test_Graph_DFS.get_graph_adjacencylist)
        t.test_dfs(Graph_AdjacencyMatrix_DFS(), test_Graph_DFS.get_graph_adjacencymatrix)

if __name__ == '__main__':
    test_BTree_DFS.run()
    test_Graph_DFS.run()

