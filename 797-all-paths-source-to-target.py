#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
from collections import deque
from typing import List
from functools import lru_cache
#   {{{2
#   TODO: 2021-10-19T17:13:03AEDT _leetcode, 797-all-paths-source-to-target, DPTopDown solution intuition

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        #return self.allPathsSourceTarget_BacktrackDFS(graph)
        return self.allPathsSourceTarget_DPTopDown(graph)


    #   runtime: beats 91%
    def allPathsSourceTarget_BacktrackDFS(self, graph: List[List[int]]) -> List[List[int]]:
        """Get list of all paths from 'initialNode' to 'targetNode' using Backtracking DFS given graph as adjacency list"""
        initialNode = 0
        targetNode = len(graph) - 1
        result = []

        def backtrack(node, path):
            if node == targetNode:
                result.append(path[:])
                return
            for nextNode in graph[node]:
                path.append(nextNode)
                backtrack(nextNode, path)
                path.pop()

        path = [ initialNode ]
        backtrack(initialNode, path)
        return result
    

    #   runtime: beats 21%
    def allPathsSourceTarget_DPTopDown(self, graph: List[List[int]]) -> List[List[int]]:
        initialNode = 0
        targetNode = len(graph) - 1
        memo = dict()

        def allPathsToTarget(node):
            if node in memo:
                return memo[node]
            if node == targetNode:
                memo[node] = [[ node ]]
                return [[ node ]]

            results = []

            for nextNode in graph[node]:
                for path in allPathsToTarget(nextNode):
                    results.append( [node] + path )
            
            memo[node] = results
            return results

        result = allPathsToTarget(initialNode)
        return result
    

s = Solution()

#   graph[i] -> list of nodes accessible from node i
input_values = [ [[1,2],[3],[3],[]], [[4,3,1],[3,2,4],[3],[4],[]], [[1,2,3],[2],[3],[]], [[1,3],[2],[3],[]], ]
input_checks = [ [[0,1,3],[0,2,3]], [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]], [[0,1,2,3],[0,2,3],[0,3]], [[0,1,2,3],[0,3]], ]

for graph, check in zip(input_values, input_checks):
    print("graph=(%s)" % graph)
    result = s.allPathsSourceTarget(graph)
    print("result=(%s)" % result)
    assert sorted(result) == sorted(check), "Check failed"
    print()

