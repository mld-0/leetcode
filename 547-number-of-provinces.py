#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
from collections import deque
from typing import List
#   {{{2
class Solution: 

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        return self.findCircleNum_BFS(isConnected)

    
    #   runtime: beats 60%
    def findCircleNum_DFS(self, isConnected: List[List[int]]) -> int:
        result = 0
        visited = set()

        def visit_adjacent(index):
            """Mark given index as visited, and recurse for connected indexs which have not been visited"""
            visited.add( index )
            for j in range(len(isConnected[index])):
                if j == index:
                    continue
                if isConnected[index][j] == 1 and j not in visited:
                    visit_adjacent(j)

        for index in range(len(isConnected)):
            if index not in visited:
                result += 1
                visit_adjacent(index)

        return result


    #   runtime: beats 16%
    def findCircleNum_BFS(self, isConnected: List[List[int]]) -> int:
        result = 0
        visited = set()

        for index in range(len(isConnected)):
            if index not in visited:
                result += 1

                queue = deque()
                queue.append( index )

                while len(queue) > 0:
                    i = queue.popleft()
                    visited.add( i )
                    for j in range(len(isConnected[i])):
                        if j == i:
                            continue
                        if isConnected[i][j] == 1 and j not in visited:
                            queue.append( j )

        return result


    #   TODO: 2021-10-15T17:12:13AEDT _leetcode, 547-number-of-provinces, 'UnionFind' solution


s = Solution()

input_values = [ [[1,1,0],[1,1,0],[0,0,1]], [[1,0,0],[0,1,0],[0,0,1]], ]
input_checks = [ 2, 3, ] 

for isConnected, check in zip(input_values, input_checks):
    print("isConnected=(%s)" % isConnected)
    result = s.findCircleNum(isConnected)
    print("result=(%s)" % result)
    assert result == check, "Check failed"
    print()

