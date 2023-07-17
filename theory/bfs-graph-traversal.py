#   vim-modelines:  {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
import inspect
from resources.bstreenode import TreeNode
from typing import List, Dict, Optional, Any
from collections import deque

#   Tree breadth first search:
#
#        _1_
#       /   \
#       2   3
#      / \ / \
#      4 5 6 7
#
#   Order:  [1,2,3,4,5,6,7]

#   Replace the queue with a stack (and switch the order elements are added) for a preorder dfs
class BTree_BFS_Iterative:

    def bfs(self, node: Optional[TreeNode]) -> List:
        result = []
        queue = deque( [ node ] )

        while len(queue) > 0:
            current = queue.popleft()
            result.append(current.val)
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

        return result


#   BFS is not suited to recursion - here we simply replace our loop with recursive calls
class BTree_BFS_Recursive:

    def bfs(self, node: Optional[TreeNode]) -> List:
        result = []
        queue = deque( [ node ] )

        def solve():
            if len(queue) == 0:
                return
            current = queue.popleft()
            result.append(current.val)
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
            solve()

        solve()
        return result


class Graph_AdjacencyList_BFS:

    def bfs(self, graph: Dict[int,List], position: int) -> List:
        seen = set()
        result = []
        queue = deque( [ position ] )
        seen.add(position)

        while len(queue) > 0:
            current = queue.popleft()
            result.append(current)
            for n in graph[current] if current in graph else []:
                if n in seen:
                    continue
                seen.add(n)
                queue.append(n)

        return result


class Graph_AdjacencyMatrix_BFS:

    def bfs(self, graph: List[List[int]], position: int) -> List:
        seen = set()
        result = []
        queue = deque( [ position ] )
        seen.add(position)

        while len(queue) > 0:
            current = queue.popleft()
            result.append(current)
            for n, x in enumerate(graph[current]):
                if x == 0:
                    continue
                if n in seen:
                    continue
                seen.add(n)
                queue.append(n)
        
        return result
                

class test_BTree_BFS:
    def test_bfs(self, c):
        #   {{{
        print("%s: %s" % (inspect.stack()[0][3], c.__class__.__name__))
        f = c.bfs
        inputs = [ [1,2,3,4,5,6,7], ]
        checks = [ [1,2,3,4,5,6,7], ]
        assert len(inputs) == len(checks)
        startTime = time.time()
        for vals, check in zip(inputs, checks):
            head = TreeNode.from_list(vals)
            print(f"{head}")
            result = f(head)
            print(f"{f.__name__}:\t{result}")
            assert result == check, "Check comparison failed"
        print("elapsed_ms=(%0.2f)" % ((time.time() - startTime) * 1000000))
        print()
        #   }}}
    @staticmethod
    def run():
        t = test_BTree_BFS()
        t.test_bfs(BTree_BFS_Iterative())
        t.test_bfs(BTree_BFS_Recursive())

class test_Graph_BFS:
    @staticmethod
    def get_graph_adjacencylist():
        return { 0: [1,2], 1: [3,4], 2: [5], 3: [], 4: [5], 5: [], }
    @staticmethod
    def get_graph_adjacencymatrix():
        return [ [0,1,1,0,0,0], [0,0,0,1,1,0], [0,0,0,0,0,1], [0,0,0,0,0,0], [0,0,0,0,0,1], [0,0,0,0,0,0] ]
    def test_bfs(self, c, g):
        #   {{{
        print("%s: %s" % (inspect.stack()[0][3], c.__class__.__name__))
        f = c.bfs
        graphs = [ g() ]
        start_node = 0
        checks = [ [0,1,2,3,4,5] ]
        assert len(graphs) == len(checks)
        startTime = time.time()
        for graph, check in zip(graphs, checks):
            print(f"{graph}")
            result = f(graph, start_node)
            print(f"{f.__name__}:\t{result}")
            assert result == check, "Check comparison failed"
        print("elapsed_ms=(%0.2f)" % ((time.time() - startTime) * 1000000))
        print()
        #   }}}
    @staticmethod
    def run():
        t = test_Graph_BFS()
        t.test_bfs(Graph_AdjacencyList_BFS(), test_Graph_BFS.get_graph_adjacencylist)
        t.test_bfs(Graph_AdjacencyMatrix_BFS(), test_Graph_BFS.get_graph_adjacencymatrix)

if __name__ == '__main__':
    test_BTree_BFS.run()
    test_Graph_BFS.run()

