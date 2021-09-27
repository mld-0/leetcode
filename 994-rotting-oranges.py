#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
import pprint
from collections import deque
from typing import List
#   {{{2

class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:
        return self.orangesRotting_Ans(grid)

    #   runtime: beats 91%
    def orangesRotting_Ans(self, grid: List[List[int]]) -> int:
        #   {{{
        #   remaining 'fresh' cells
        fresh_remaining = 0  
        #   cycles, or 'minutes' elapsed
        minutes_elapsed = 0

        #   BFS queue
        queue = deque()

        #   4-adjacency
        adjacent_offsets = [ (-1,0), (1,0), (0,-1), (0,1) ]

        #   add initially rotten cells to queue, and count initial fresh cells
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append( (row,col) )
                elif grid[row][col] == 1:
                    fresh_remaining += 1

        #   (-1,-1) denotes end of one cycle, or that a 'minute' has elapsed
        queue.append( (-1,-1) )

        #   process queue
        while len(queue) > 0:
            row, col = queue.popleft()

            #   upon reaching end of cycle, if not at end of queue, increment 'minutes_elapsed' and append another (-1,-1)
            if row == -1 and col == -1:
                if len(queue) > 0:
                    minutes_elapsed += 1
                    queue.append( (-1, -1) )
                continue

            #   (otherwise), process adjacent cells
            for delta_row, delta_col in adjacent_offsets:
                #   skip invalid
                if delta_row+row < 0 or delta_row+row >= len(grid):
                    continue
                if delta_col+col < 0 or delta_col+col >= len(grid[0]):
                    continue

                #   if adjacent cell is 'fresh', set adjacent cell to 'rotten', and add to queue
                if grid[delta_row+row][delta_col+col] == 1:
                    grid[delta_row+row][delta_col+col] = 2
                    fresh_remaining -= 1
                    queue.append( (delta_row+row, delta_col+col) )

        if fresh_remaining == 0:
            return minutes_elapsed
        else:
            return -1
        #   }}}


s = Solution()

input_values = [ [[2,1,1],[1,1,0],[0,1,1]], [[2,1,1],[0,1,1],[1,0,1]], [[0,2]] ]
input_checks = [ 4, -1, 0 ]

#   grid[row][col]: 0=empty, 1=fresh, 2=rotten
for grid, check in zip(input_values, input_checks):
    print("grid:")
    pprint.pprint(grid)
    result = s.orangesRotting(grid)
    print("result=(%s)" % str(result))
    assert( result == check )
    print()






