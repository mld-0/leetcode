from typing import List

class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        return self.maxAreaOfIsland_Recursive(grid)


    def maxAreaOfIsland_Recursive(self, grid: List[List[int]]) -> int:
        seen = set()
        def area(row, col):
            if row < 0 or row >= len(grid):
                return 0
            if col < 0 or col >= len(grid[0]):
                return 0
            if (row, col) in seen:
                return 0
            if grid[row][col] == 0:
                return 0
            seen.add( (row, col) )
            return 1 + area(row+1, col) + area(row-1, col) + area(row, col+1) + area(row, col-1)
        return max( [ area(row, col) for row in range(len(grid)) for col in range(len(grid[0])) ] )


    #   TODO: 2021-09-21T17:47:34AEST _leetcode, 695-max-area-of-island, iterative (stack) solution
    def maxAreaOfIsland_Stack(self, grid: List[List[int]]) -> int:
        pass


s = Solution()

input_values = [ [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]], [[0,0,0,0,0,0,0,0]], ]
input_checks = [ 6, 0, ]

for grid, check in zip(input_values, input_checks):
    result = s.maxAreaOfIsland(grid)    
    print("result=(%s)" % str(result))
    assert( result == check ) 
    print()

