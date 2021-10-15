#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
from collections import deque
from typing import List
#   {{{2
class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        #return self.numIslands_DFS(grid)
        return self.numIslands_BFS(grid)

    #   runtime: beats 41%
    def numIslands_DFS(self, grid: List[List[str]]) -> int:
        result = 0
        visited = set()

        def visit_surrounding(row, col):
            if row < 0 or row >= len(grid):
                return False
            if col < 0 or col >= len(grid[row]):
                return False
            if grid[row][col] != "1":
                return False
            if (row, col) in visited:
                return False
            visited.add( (row, col) )
            offsets = [ (-1,0), (1,0), (0,-1), (0,1), ]
            for delta_row, delta_col in offsets:
                visit_surrounding(row+delta_row, col+delta_col)
            return True

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    trial = visit_surrounding(row, col)
                    if trial == True:
                        result += 1

        return result


    #   runtime: beats 75%
    def numIslands_BFS(self, grid: List[List[str]]) -> int:
        result = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):

                if grid[row][col] == '1':
                    result += 1
                    grid[row][col] = 0
                    neighbours = deque()
                    neighbours.append( (row, col) )

                    while len(neighbours) > 0:
                        r, c = neighbours.popleft()
                        if r-1 >= 0 and grid[r-1][c] == '1':
                            neighbours.append( (r-1, c) )
                            grid[r-1][c] = 0
                        if r+1 < len(grid) and grid[r+1][c] == '1':
                            neighbours.append( (r+1, c) )
                            grid[r+1][c] = 0
                        if c-1 >= 0 and grid[r][c-1] == '1':
                            neighbours.append( (r, c-1) )
                            grid[r][c-1] = 0
                        if c+1 < len(grid[r]) and grid[r][c+1] == '1':
                            neighbours.append( (r, c+1) )
                            grid[r][c+1] = 0

        return result


#   TODO: 2021-10-15T15:34:41AEDT _leetcode, 200-number-of-islands, UnionFind solution


s = Solution()

input_values = [ [["1","1","1","1","0"], ["1","1","0","1","0"], ["1","1","0","0","0"], ["0","0","0","0","0"]], [["1","1","0","0","0"], ["1","1","0","0","0"], ["0","0","1","0","0"], ["0","0","0","1","1"]], ]
input_checks = [ 1, 3, ]

for grid, check in zip(input_values, input_checks):
    print("grid=(%s)" % str(grid))
    result = s.numIslands(grid)
    print("result=(%s)" % str(result))
    assert result == check, "Check failed"
    print()

