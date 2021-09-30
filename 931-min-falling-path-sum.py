#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
import math
import functools
from typing import List
#   {{{2

class Solution:

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        #return self.minFallingPathSum_Recursive(matrix)
        #return self.minFallingPathSum_Path_Recursive(matrix)
        return self.minFallingPathSum_DP_BottomUp(matrix)


    #   runtime: TLE
    def minFallingPathSum_Recursive(self, matrix: List[List[int]]) -> int:
        @functools.lru_cache()
        def min_path(row, col):
            path = matrix[row][col]
            offset_deltas = [ -1, 0, 1 ]

            trials = [ math.inf ]
            if row < len(matrix) - 1:
                for delta_col in offset_deltas:
                    if col+delta_col >= 0 and col+delta_col < len(matrix[0]):
                        trials.append( min_path(row+1, col+delta_col ) )
                path += min(trials)

            return path
        
        results = []
        for col in range(len(matrix[0])):
            results.append( min_path(0, col) )
        print(results)

        return min(results)


    #   runtime: TLE
    def minFallingPathSum_Path_Recursive(self, matrix: List[List[int]]) -> int:
    #   {{{
    #   See: 120-triangle for simpler example of tracing steps of solution of recursive function
        @functools.lru_cache()
        def min_path(row, col):
            steps = []
            all_loop_steps = []
            path = matrix[row][col]
            offset_deltas = [ -1, 0, 1 ]
            #trials = [ math.inf ]
            trials = []
            all_cols = []
            if row < len(matrix) - 1:
                for delta_col in offset_deltas:
                    if col+delta_col >= 0 and col+delta_col < len(matrix[0]):
                        loop_trial, loop_steps = min_path(row+1, col+delta_col )
                        trials.append( loop_trial )
                        all_loop_steps.append( loop_steps )
                        all_cols.append(col+delta_col)
                trials_min = math.inf
                trials_min_index = -1
                for i, loop_trial in enumerate(trials):
                    if loop_trial < trials_min:
                        trials_min = loop_trial
                        trials_min_index = i
                path += trials_min
                steps = steps + all_loop_steps[trials_min_index] + [ (row+1, all_cols[trials_min_index]) ]
            return path, steps
        results = []
        steps = []
        for col in range(len(matrix[0])):
            loop_result, loop_steps = min_path(0, col)
            results.append( loop_result )
            steps.append( loop_steps )
        results_min = math.inf
        results_min_index = -1
        for i, loop_result in enumerate(results):
            if loop_result < results_min:
                results_min = loop_result
                results_min_index = i
        steps = [ (0, results_min_index) ] + steps[results_min_index][::-1]
        print("steps=(%s)" % str(steps))
        values_traveled = [ matrix[row][col] for row, col in steps ]
        print("values_traveled=(%s)" % str(values_traveled))
        return results[results_min_index]
    #   }}}


    #   runtime: beats 54%
    def minFallingPathSum_DP_BottomUp(self, matrix: List[List[int]]) -> int:
        grid = matrix[:]
        for row in range(1, len(matrix)):
            for col in range(len(matrix[row])):
                trials = [ math.inf ] * 3

                if row-1 >= 0 and col-1 >= 0:
                    trials[0] = grid[row-1][col-1]
                if row-1 >= 0:
                    trials[1] = grid[row-1][col]
                if row-1 >= 0 and col+1 < len(matrix[row]):
                    trials[2] = grid[row-1][col+1]

                grid[row][col] += min(trials)

        return min(grid[-1])
        

    #   TODO: _leetcode, 931-min-falling-path-sum, dynamic programming 'top down' solution
    def minFallingPathSum_DP_TopDown(self, matrix: List[List[int]]) -> int:
        raise NotImplementedError()


    #   TODO: 2021-09-30T21:14:12AEST _leetcode, 931-min-falling-path-sum, trace path of solution (for recursive and DP solutions)
    def minFallingPathSum_Path_DP(self, matrix: List[List[int]]) -> int:
        raise NotImplementedError()


s = Solution()

input_values = [ [[2,1,3],[6,5,4],[7,8,9]], [[-19,57],[-40,-5]], [[-48]], [[100,-42,-46,-41],[31,97,10,-10],[-58,-51,82,89],[51,81,69,-51]], [[17,82],[1,-44]], ]
input_checks = [ 13, -59, -48, -36, -27 ]

for matrix, check in zip(input_values, input_checks):
    result = s.minFallingPathSum(matrix)
    print("result=(%s)" % str(result))
    assert result == check, "Check failed"
    print()

