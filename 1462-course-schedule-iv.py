#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
from collections import deque, defaultdict
from typing import List, Optional
from functools import cache

class Solution:
    """Determine if course a is a prerequisite to course b from an adjacency matrix of prerequisites"""

    #   runtime: beats 14%
    #    memory: beats 80%
    def checkIfPrerequisite_DFS(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        graph = defaultdict(set)
        for (start, end) in prerequisites:
            graph[end].add(start)

        result = []
        for (start, end) in queries:
            visited = set()
            queue = deque()
            queue.append(end)
            loop_result = False
            while len(queue) > 0:
                current = queue.popleft()
                visited.add(current)
                for _next in graph[current]:
                    if _next in visited:
                        continue
                    if _next == start:
                        loop_result = True
                        break
                    visited.add(_next)
                    queue.append(_next)
                if loop_result == True:
                    break
            result.append(loop_result)

        return result


    #   runtime: beats 40%
    #    memory: beats 5%
    def checkIfPrerequisite_BFS(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        @cache
        def search(start, end):
            if start == end:
                return True
            if end in graph[start]:
                return True
            for _next in graph[start]:
                if _next == end:
                    return True
                if search(_next, end):
                    return True
            return False

        graph = defaultdict(set)
        for (start, end) in prerequisites:
            graph[end].add(start)

        return [ search(start, end) for end, start in queries ]


    #   runtime: beats 93%
    #    memory: eats 25%
    def checkIfPrerequisite_ans_TopologicalSortKahnAlgorithm(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        #   directDependents[a] = set of nodes for which `a` is a direct prerequisite
        directDependents = defaultdict(set)

        #   preqCounts[a] = count of how many direct prerequisites does `a` have
        preqCounts = defaultdict(int)

        #   Construct adjacency list from edge list `prerequisites`
        for prereq, course in prerequisites:
            directDependents[prereq].add(course)
            preqCounts[course] += 1

        #   queue[a] = nodes with no prerequisites not yet explored
        queue = deque()
        for course in range(numCourses):
            if preqCounts[course] == 0:
                queue.append(course)

        #   allPrereqs[a] = nodes which are directly or indirectly prerequisites of `a`
        allPrereqs = defaultdict(set)
        while len(queue) > 0:
            current = queue.popleft()
            for dependent in directDependents[current]:
                allPrereqs[dependent].add(current)
                allPrereqs[dependent] |= allPrereqs[current]
                preqCounts[dependent] -= 1
                if preqCounts[dependent] == 0:
                    queue.append(dependent)

        #   Answer the queries using `allPrereqs`
        result = []
        for pre, post in queries:
            result.append( pre in allPrereqs[post] )

        #print(f"directDependents=({directDependents}), preqCounts=({preqCounts})")
        #print(f"queue=({queue})")
        #print(f"allPrereqs=({allPrereqs})")
        return result


    def checkIfPrerequisite_ans_FloydWarshall(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        raise NotImplementedError("complete example theory/topological-sort and ans Floyd Warshall Algorithm")



s = Solution()
test_functions = [ s.checkIfPrerequisite_DFS, s.checkIfPrerequisite_BFS, s.checkIfPrerequisite_ans_TopologicalSortKahnAlgorithm, s.checkIfPrerequisite_ans_FloydWarshall, ]

#test_functions = [s.checkIfPrerequisite_ans_TopologicalSortKahnAlgorithm, s.checkIfPrerequisite_ans_FloydWarshall, ]
#test_functions = [s.checkIfPrerequisite_ans_TopologicalSortKahnAlgorithm, ]

inputs = [
        (2, [[1,0]], [[0,1],[1,0]]),
        (2, [], [[1,0],[0,1]]), 
        (3, [[1,2],[1,0],[2,0]], [[1,0],[1,2]]), 
        (5, [[0,1],[1,2],[2,3],[3,4]], [[0,4],[4,0],[1,3],[3,0]]), 
        (5, [[4,3],[4,1],[4,0],[3,2],[3,1],[3,0],[2,1],[2,0],[1,0]], [[1,4],[4,2],[0,1],[4,0],[0,2],[1,3],[0,1]]), 
        (3, [[1,0],[2,0]], [[0,1],[2,0]]), 
        (7, [[2,3],[2,1],[2,0],[3,4],[3,6],[5,1],[5,0],[1,4],[1,0],[4,0],[0,6]], [[3,0],[6,4],[5,6],[2,6],[2,3],[5,6],[4,0],[2,6],[3,5],[5,3],[1,6],[1,0],[3,5],[6,5],[2,3],[3,0],[3,4],[3,4],[2,5],[0,3],[4,0],[6,4],[5,0],[6,5],[5,6],[6,5],[1,0],[3,4],[1,5],[1,4],[3,6],[0,1],[1,2],[5,1],[5,3],[5,3],[3,4],[5,4],[5,4],[5,3]]), 
        ]
checks = [ 
          [False, True], 
          [False, False], 
          [True,True], 
          [True,False,True,False], 
          [False,True,False,True,False,False,False], 
          [False,True],
          [True,False,True,True,True,True,True,True,False,False,True,True,False,False,True,True,True,True,False,False,True,False,True,False,True,False,True,True,False,True,True,False,False,True,False,False,True,True,True,False],

          ]

#inputs = [ (3, [[1,2],[1,0],[2,0]], [[1,0],[1,2]]), ]; checks = [ [True,True], ];
#inputs = [ (5, [[0,1],[1,2],[2,3],[3,4]], [[0,4],[4,0],[1,3],[3,0]]), ]; checks = [ [True,False,True,False], ];

assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for (numCourses, prerequisites, queries), check in zip(inputs, checks):
        print(f"numCourses,=({numCourses,}), prerequisites,=({prerequisites,}), queries=({queries})")
        result = f(numCourses, prerequisites, queries)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

