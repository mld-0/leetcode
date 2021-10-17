#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
from typing import List
from collections import deque
import heapq
from queue import PriorityQueue
#   {{{2
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        #return self.shortestPathBinaryMatrix_DFS(grid)
        return self.shortestPathBinaryMatrix_AStar(grid)


    #   runtime: beats 27%
    def shortestPathBinaryMatrix_DFS(self, grid: List[List[int]]) -> int:
        """Determine distance from top-left to bottom-right for 8-connected zero-values in 'grid' using DFS"""

        def get_neighbours(row, col):
            """Generate valid surrounding indexes for a given index"""
            deltas = [ (-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1), ]
            for delta_row, delta_col in deltas:
                if row+delta_row < 0 or row+delta_row >= len(grid):
                    continue
                if col+delta_col < 0 or col+delta_col >= len(grid[row]):
                    continue
                yield (row+delta_row, col+delta_col)

        #   check path start/end points are valid
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1

        #   queue: (row, col, distance)
        queue = deque([ (0,0,1) ])
        visited = set([ (0,0) ])

        while len(queue) > 0:
            row, col, distance = queue.popleft()
            if (row, col) == (len(grid)-1, len(grid[0])-1):
                return distance
            for neighbour_row, neighbour_col in get_neighbours(row, col):
                if (neighbour_row, neighbour_col) in visited:
                    continue
                if grid[neighbour_row][neighbour_col] != 0:
                    continue
                visited.add( (neighbour_row, neighbour_col) )
                queue.append( (neighbour_row, neighbour_col, distance+1) )

        return -1


    #   runtime: beats 94%
    def shortestPathBinaryMatrix_AStar(self, grid: List[List[int]]) -> int:
        """Determine distance from top-left to bottom-right for 8-connected zero-values in 'grid' using AStar"""

        def get_neighbours(row, col):
            """Generate valid surrounding indexes for a given index"""
            #   prefer horizontal/vertical neighours to diagonal neighbours
            deltas = [ (-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1), ]
            for delta_row, delta_col in deltas:
                if row+delta_row < 0 or row+delta_row >= len(grid):
                    continue
                if col+delta_col < 0 or col+delta_col >= len(grid[row]):
                    continue
                yield (row+delta_row, col+delta_col)

        def best_case_distance(row, col):
            """AStar heuristic, gives lower bound for remaining distance"""
            #   Formula for chebyshev distance heuristic:
            #   LINK: http://theory.stanford.edu/~amitp/GameProgramming/Heuristics.html
            d1, d2 = 1, 1  
            dx = abs(len(grid)-1 - row)
            dy = abs(len(grid[0])-1 - col)
            return d1 * (dx + dy) + (d2 - 2 * d1) * min(dx, dy) 

        #   check path start/end points are valid
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1

        #   priority_queue entries: (total-distance-estimate, distance-so-far, (row, col))
        priority_queue = [ (1+best_case_distance(0,0), 1, (0,0) ) ]
        visited = set()

        while priority_queue:
            estimate, distance, (row, col) = heapq.heappop(priority_queue)
            if (row, col) in visited:
                continue
            if (row, col) == (len(grid)-1, len(grid[0])-1):
                return distance
            visited.add( (row, col) )
            for neighbour_row, neighbour_col in get_neighbours(row, col):
                #   optimisation:
                if (neighbour_row, neighbour_col) in visited:
                    continue
                if grid[neighbour_row][neighbour_col] != 0:
                    continue
                #   diagonals have distance 1, not sqrt(2)
                estimate = best_case_distance(neighbour_row, neighbour_col) + distance + 1
                heapq.heappush( priority_queue, (estimate, distance+1, (neighbour_row, neighbour_col)) )

        return -1


s = Solution()

input_values = [ [[0,0,0],[1,1,0],[1,1,0]], [[1,0,0],[1,1,0],[1,1,0]], [[0,0,0,0,1],[1,0,0,0,0],[0,1,0,1,0],[0,0,0,1,1],[0,0,0,1,0]], [[0,0,0,0,1,1,1,1,0],[0,1,1,0,0,0,0,1,0],[0,0,1,0,0,0,0,0,0],[1,1,0,0,1,0,0,1,1],[0,0,1,1,1,0,1,0,1],[0,1,0,1,0,0,0,0,0],[0,0,0,1,0,1,0,0,0],[0,1,0,1,1,0,0,0,0],[0,0,0,0,0,1,0,1,0]], ]
input_checks = [ 4, -1, -1, 11, ]

for grid, check in zip(input_values, input_checks):
    print("grid=(%s)" % grid)
    result = s.shortestPathBinaryMatrix(grid)
    print("result=(%s)" % result)
    assert result == check, "Check failed"
    print()

