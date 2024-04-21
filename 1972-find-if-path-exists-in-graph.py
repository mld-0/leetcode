#   {{{3
       #   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
from collections import deque, defaultdict
from typing import List, Optional

class Solution:
    """Given a graph as an edge list, determine if a path exists between `source` and `destination` nodes"""

    #   runtime: beats 42%
    #    memory: beats 5%
    def validPath_DFS_Recursive(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(set)
        visited = set()
        for (a, b) in edges:
            graph[a].add(b)
            graph[b].add(a)

        def dfs(current):
            nonlocal destination
            if current == destination:
                return True
            if current in visited:
                return False
            visited.add(current)
            for end in graph[current]:
                if end not in visited and dfs(end):
                    return True
            return False
        
        return dfs(source)


    #   runtime: beats 73%
    #    memory: beats 47%
    def validPath_DFS_Iterative(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(set)
        visited = set()
        for (a, b) in edges:
            graph[a].add(b)
            graph[b].add(a)
        stack = deque()
        stack.append(source)
        visited.add(source)
        while stack:
            current = stack.pop()
            if current == destination:
                return True
            for end in graph[current]:
                if end not in visited:
                    stack.append(end)
                    visited.add(end)
        return False


    #   runtime: beats 89%
    #    memory: beats 43%
    def validPath_BFS(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(set)
        visited = set()
        for (a, b) in edges:
            graph[a].add(b)
            graph[b].add(a)
        queue = deque()
        queue.append(source)
        visited.add(source)
        while queue:
            current = queue.popleft()
            if current == destination:
                return True
            if current not in graph:
                continue
            for end in graph[current]:
                if end not in visited:
                    queue.append(end)
                    visited.add(end)
        return False


    def validPath_ans_DisjointSetUnion(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        raise NotImplementedError("Continue: DisjointSetUnion answer")


s = Solution()
test_functions = [ s.validPath_DFS_Recursive, s.validPath_DFS_Iterative, s.validPath_BFS, s.validPath_ans_DisjointSetUnion]

inputs = [ (3,[[0,1],[1,2],[2,0]],0,2),  (6,[[0,1],[0,2],[3,5],[5,4],[4,3]],0,5), (3,[[0,1],[1,2],[2,0]],0,2), (10,[[4,3],[1,4],[4,8],[1,7],[6,4],[4,2],[7,4],[4,0],[0,9],[5,4]],5,9), ]
checks = [ True, False, True, True, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for (n, edges, source, dest), check in zip(inputs, checks):
        print(f"n=({n}), edges=({edges}), source=({source}), dest=({dest})")
        result = f(n, edges, source, dest)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

