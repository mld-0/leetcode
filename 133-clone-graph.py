#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
from collections import defaultdict, deque
from typing import List, Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    """Given a graph, represented using the class `Node`, created and return a deep copy"""

    #   runtime: beats 92%
    #    memory: beats 35%
    def cloneGraph_BFS(self, node: Optional[Node]) -> Optional[Node]:
        if node is None:
            return None
        if node.neighbors is None:
            return Node(1)
        if len(node.neighbors) == 0:
            return Node(1)

        def bfs(node, new_nodes):
            queue = deque([node])
            seen = set([node.val])
            while queue:
                current = queue.popleft()
                new_nodes[current.val] = Node(current.val)
                for _next in current.neighbors:
                    adjList[current.val].append(_next.val)
                    if _next.val not in seen:
                        queue.append(_next)
                        seen.add(_next.val)

        def make_connections(new_nodes, adjList):
            for i in new_nodes.keys():
                for _nxt in adjList[i]:
                    if new_nodes[i].neighbors is None:
                        new_nodes[i].neighbors = []
                    new_nodes[i].neighbors.append(new_nodes[_nxt])

        adjList = defaultdict(list)
        new_nodes = dict()
        bfs(node, new_nodes)
        make_connections(new_nodes, adjList)
        return new_nodes[1]


def make_graph(adjList: List[List[int]]) -> Optional[Node]:
    if len(adjList) == 0:
        return None
    nodes = { i: Node(i) for i in range(1, len(adjList)+1) }
    for i in range(1, len(adjList)+1):
        connections = adjList[i-1]
        if len(connections) > 0:
            nodes[i].neighbors = []
        for j in connections:
            if i != j:
                nodes[i].neighbors.append(nodes[j])
    return nodes[1]

def graphs_eq(g1, g2):
    def bfs(node):
        result = []
        if node is None:
            return result
        seen = set([node.val])
        queue = deque([node])
        while queue:
            current = queue.popleft()
            result.append(current.val)
            for _next in current.neighbors:
                if _next.val not in seen:
                    queue.append(_next)
                    seen.add(_next.val)
        return result
    g1_bfs = bfs(g1)
    g2_bfs = bfs(g2)
    return g1_bfs == g2_bfs

s = Solution()
test_functions = [ s.cloneGraph_DFS, ]

inputs = [ [[2,4],[1,3],[2,4],[1,3]], [[]], [], ]
checks = [ [[2,4],[1,3],[2,4],[1,3]], [[]], [], ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for vals, check in zip(inputs, checks):
        node = make_graph(vals)
        print(f"vals=({vals}), node=({node})")
        result = f(node)
        print(f"result=({result})")
        check = make_graph(check)
        assert graphs_eq(result, check), "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

