#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
import pprint
import math
from collections import deque
from typing import List
#   {{{2

class Solution:

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        #return self.updateMatrix_DFS(mat)
        return self.updateMatrix_DP(mat)


    #   runtime: beats 23%
    def updateMatrix_DFS(self, mat: List[List[int]]) -> List[List[int]]:
        #   result[row][col] = distance to nearest '0', initially 0 for '0' cells, and math.inf for '1' cells
        result = [ [ math.inf for col in range(len(mat[0])) ] for row in range(len(mat)) ]
        adjacent_offsets = [ (-1,0), (1,0), (0,-1), (0,1) ]  # offsets for 4-connected-ness

        #   DFS queue
        queue = deque()

        #   set result[row][col] = 0 for zero cells and add zero cells to queue
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    result[row][col] = 0
                    queue.append( (row,col) )

        #   process (row,col) in queue
        while len(queue) > 0:
            row, col = queue.popleft()

            #   for each square that that is 4-adjacent to (row,col)
            for delta_row, delta_col in adjacent_offsets:
                #   out-of-bounds, skip
                if row+delta_row < 0 or row+delta_row >= len(mat):
                    continue
                if col+delta_col < 0 or col+delta_col >= len(mat[0]):
                    continue

                #   Update adjacent cell using current cell if it describes a shorter path to the adjacent cell, adding the adjacent cell to the queue if so
                if result[row+delta_row][col+delta_col] > result[row][col] + 1:
                    result[row+delta_row][col+delta_col] = result[row][col] + 1
                    queue.append( (row+delta_row, col+delta_col) )

        return result

    
    #   runtime: beats 72%
    def updateMatrix_DP(self, mat: List[List[int]]) -> List[List[int]]:
        #   result[row][col] = distance to nearest '0', initially 0 for '0' cells, and math.inf for '1' cells
        result = [ [ math.inf for col in range(len(mat[0])) ] for row in range(len(mat)) ]

        #   Pass 1: d[i,j] = min( d[i,j], min(d[i-1,j], d[i,j-1])+1 )
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    result[row][col] = 0
                else:
                    if row > 0:
                        result[row][col] = min(result[row][col], result[row-1][col] + 1)
                    if col > 0:
                        result[row][col] = min(result[row][col], result[row][col-1] + 1)

        #   Pass 2: d[i,j] = min( d[i,j], min(d[i+1,j], d[i,j+1])+1 )
        for row in range(len(mat)-1, -1, -1):
            for col in range(len(mat[0])-1, -1, -1):
                if row < len(mat)-1:
                    result[row][col] = min(result[row][col], result[row+1][col] + 1)
                if col < len(mat[0])-1:
                    result[row][col] = min(result[row][col], result[row][col+1] + 1)

        return result


s = Solution()

input_values = [ [[0,0,0],[0,1,0],[0,0,0]], [[0,0,0],[0,1,0],[1,1,1]], [[0,1,0,1,1],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]], [[1,1,0,0,1,0,0,1,1,0],[1,0,0,1,0,1,1,1,1,1],[1,1,1,0,0,1,1,1,1,0],[0,1,1,1,0,1,1,1,1,1],[0,0,1,1,1,1,1,1,1,0],[1,1,1,1,1,1,0,1,1,1],[0,1,1,1,1,1,1,0,0,1],[1,1,1,1,1,0,0,1,1,1],[0,1,0,1,1,0,1,1,1,1],[1,1,1,0,1,0,1,1,1,1]], [[1,1,0,1,1,1,1,1,1,1],[1,1,0,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,1,1,0],[1,1,1,1,1,1,0,0,1,0],[1,0,0,1,1,1,0,1,0,1],[0,0,1,0,0,1,1,0,0,1],[0,1,0,1,1,1,1,1,1,1],[1,0,0,1,1,0,0,0,0,0],[0,0,1,1,1,1,0,1,1,1],[1,1,0,0,1,0,1,0,1,1]] ]
input_checks = [ [[0,0,0],[0,1,0],[0,0,0]], [[0,0,0],[0,1,0],[1,2,1]], [[0,1,0,1,2],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]], [[2,1,0,0,1,0,0,1,1,0],[1,0,0,1,0,1,1,2,2,1],[1,1,1,0,0,1,2,2,1,0],[0,1,2,1,0,1,2,3,2,1],[0,0,1,2,1,2,1,2,1,0],[1,1,2,3,2,1,0,1,1,1],[0,1,2,3,2,1,1,0,0,1],[1,2,1,2,1,0,0,1,1,2],[0,1,0,1,1,0,1,2,2,3],[1,2,1,0,1,0,1,2,3,4]], [[2,1,0,1,2,2,2,3,3,2],[2,1,0,1,1,1,1,2,2,1],[3,2,1,1,0,0,0,1,1,0],[2,1,1,2,1,1,0,0,1,0],[1,0,0,1,1,1,0,1,0,1],[0,0,1,0,0,1,1,0,0,1],[0,1,0,1,1,1,1,1,1,1],[1,0,0,1,1,0,0,0,0,0],[0,0,1,1,2,1,0,1,1,1],[1,1,0,0,1,0,1,0,1,2]] ]

for mat, check in zip(input_values, input_checks):
    print("mat:")
    pprint.pprint(mat)
    result = s.updateMatrix(mat)
    print("result:")
    pprint.pprint(result)
    assert( result == check )
    print()

