import time
from typing import List, Set
from collections import defaultdict, deque
from functools import cache


#   For a graph, return a (sorted) list of 'safe nodes'
#   A node is safe if all possible paths from that node lead only to terminal nodes or other safe nodes
#   A terminal node is a node with no outgoing edges

class Solution:

    #   runtime: beats 78%
    def eventualSafeNodes_DFSCycleCheck(self, graph: List[List[int]]) -> List[int]:
        result = set()

        @cache
        def contains_cycle(node: int) -> bool:
            if node in seen:
                return True
            seen.add(node)
            for n in graph[node]:
                if n in result:
                    continue
                if contains_cycle(n):
                    return True
            seen.remove(node)
            return False

        for i in range(len(graph)):
            seen = set()
            if not contains_cycle(i):
                result.add(i)
        return sorted(list(result))


    #   runtime: TLE
    def eventualSafeNodes_BFSCycleCheck(self, graph: List[List[int]]) -> List[int]:
        result = set()

        def contains_cycle(node: int) -> bool:
            queue = deque()
            seen = set()
            queue.append( (node, seen) )
            while len(queue) > 0:
                current, seen = queue.popleft()
                if current in seen:
                    return True
                if current in result:
                    continue
                seen.add(current)
                for n in graph[current]:
                    if n in result:
                        continue
                    queue.append( (n, seen.copy()) )
                seen.remove(current)
            return False

        for i in range(len(graph)):
            if not contains_cycle(i):
                result.add(i)
        return sorted(list(result))


    def eventualSafeNodes_ans_TopologicalSort_KahnsAlgorithm(self, graph: List[List[int]]) -> List[int]:
        num_nodes = len(graph)
        graph_invert = [ [] for _ in range(num_nodes) ]
        graph_in_edges = [ 0 for _ in range(num_nodes) ]

        #   Invert the graph, and count the number of edges going into each node for the non-inverted graph
        for src in range(num_nodes):
            for dest in graph[src]:
                graph_invert[dest].append(src)
                graph_in_edges[src] += 1

        result = []
        queue = deque()

        #   Add all terminal nodes to the queue
        for n in range(num_nodes):
            if graph_in_edges[n] == 0:
                queue.append(n)

        #   Iteratively remove terminal nodes (those with no remaining in_edges) from the graph
        #   The only nodes left in the origional graph (nodes not in `result`) are either in a cycle, or lead to a node in a cycle
        while len(queue) > 0:
            current = queue.popleft()
            result.append(current)
            for n in graph_invert[current]:
                graph_in_edges[n] -= 1
                if graph_in_edges[n] == 0:
                    queue.append(n)

        return sorted(result)


s = Solution()
test_functions = [ s.eventualSafeNodes_DFSCycleCheck, s.eventualSafeNodes_BFSCycleCheck, s.eventualSafeNodes_ans_TopologicalSort_KahnsAlgorithm, ]

inputs = [ [[1,2],[2,3],[5],[0],[5],[],[]], [[1,2,3,4],[1,2],[3,4],[0,4],[]], [[],[0,2,3,4],[3],[4],[]], ]
checks = [ [2,4,5,6], [4], [0,1,2,3,4], ]
assert len(inputs) == len(checks)

for f in test_functions:
    print(f.__name__)
    startTime = time.time()
    for graph, check in zip(inputs, checks):
        print(f"graph=({graph})")
        result = f(graph)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_ms=(%0.2f)" % ((time.time() - startTime) * 1000000))
    print()

