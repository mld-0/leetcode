import time
from collections import defaultdict
from typing import List

class Solution:

    #   runtime: beats 40%
    def merge_i(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        result = []
        i = 0
        while i < len(intervals):
            start = intervals[i][0]
            end = intervals[i][1]
            while i+1 < len(intervals) and intervals[i+1][0] <= end:
                if intervals[i+1][1] >= end:
                    end = intervals[i+1][1]
                i += 1
            result.append( [start,end] )
            i += 1
        return result


    #   runtime: beats 50%
    def merge_ans_Sorting(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged


    #   runtime: TLE
    def merge_ans_Graph(self, intervals: List[List[int]]) -> List[List[int]]:
        def overlap(a, b):
            return a[0] <= b[1] and b[0] <= a[1]
        def buildGraph(intervals):
            """generate graph where there is an undirected edge between intervals u and v iff u and v overlap"""
            graph = defaultdict(list)
            for i, interval_i in enumerate(intervals):
                for j in range(i+1, len(intervals)):
                    if overlap(interval_i, intervals[j]):
                        graph[tuple(interval_i)].append(intervals[j])
                        graph[tuple(intervals[j])].append(interval_i)
            return graph
        def mergeNodes(nodes):
            """merges all of the nodes in this connected component into one interval"""
            min_start = min(node[0] for node in nodes)
            max_end = max(node[1] for node in nodes)
            return [min_start, max_end]
        def getComponents(graph, intervals):
            """gets the connected components of the interval overlap graph"""
            visited = set()
            comp_number = 0
            nodes_in_comp = defaultdict(list)
            def markComponentDFS(start):
                stack = [start]
                while stack:
                    node = tuple(stack.pop())
                    if node not in visited:
                        visited.add(node)
                        nodes_in_comp[comp_number].append(node)
                        stack.extend(graph[node])
            for interval in intervals:
                if tuple(interval) not in visited:
                    markComponentDFS(interval)
                    comp_number += 1
            return nodes_in_comp, comp_number
        graph = buildGraph(intervals)
        nodes_in_comp, number_of_comps = getComponents(graph, intervals)
        return [ mergeNodes(nodes_in_comp[comp]) for comp in range(number_of_comps) ]


s = Solution()
test_functions = [ s.merge_i, s.merge_ans_Sorting, s.merge_ans_Graph, ]

inputs = [ [[1,3],[2,6],[8,10],[15,18]], [[1,4],[4,5]], [[1,5],[2,3]], [[1,4],[0,4]], ]
checks = [ [[1,6],[8,10],[15,18]], [[1,5]], [[1,5]], [[0,4]], ]
assert len(inputs) == len(checks)

for f in test_functions:
    print(f.__name__)
    startTime = time.time()
    for intervals, check in zip(inputs, checks):
        print(f"intervals=({intervals})")
        result = f(intervals)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_ms=(%0.2f)" % ((time.time() - startTime) * 1000000))
    print()

