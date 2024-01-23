#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
import math
import functools
from collections import defaultdict
from typing import List, Optional

#   From 1057-campus-bikes-i:
#   {{{
#    #   runtime: beats 35%
#    def assignBikes_sorting(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
#
#        def dist(p1: List[int], p2: List[int]) -> int:
#            return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
#
#        #   distances[i][j]: distance from worker `i` to bike `j`
#        distances = sorted((dist(worker,bike),i,j) for j, bike in enumerate(bikes) for i, worker in enumerate(workers))
#
#        #   worker_bikes[i]: index of bike assigned to i-th worker
#        worker_bikes = [ None for _ in range(len(workers)) ]
#
#        #   bike_assigned[j]: has j-th bike been assigned 
#        bike_assigned = [ False for _ in range(len(bikes)) ]
#
#        for (distance, i, j) in distances:
#            if worker_bikes[i] is None and not bike_assigned[j]:
#                worker_bikes[i] = j
#                bike_assigned[j] = True
#        return worker_bikes
#
#
#    #   runtime: beats 85%
#    def assignBikes_ans_BucketSort(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
#
#        def find_dist(p1: List[int], p2: List[int]) -> int:
#            return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
#
#        #   dist_to_pairs[d]: list of all pairs of workers/bikes (i,j) which are distance `d` apart
#        dist_to_pairs = defaultdict(list)
#
#        for i, worker in enumerate(workers):
#            for j, bike in enumerate(bikes):
#                dist = find_dist(worker, bike)
#                dist_to_pairs[dist].append((i,j))
#
#        #   bike_assigned[j]: has j-th bike been assigned 
#        bike_assigned = [ False for _ in range(len(bikes)) ]
#
#        #   worker_bikes[i]: index of bike assigned to i-th worker
#        worker_bikes = [ None for _ in range(len(workers)) ]
#
#        #   how many bikes have been assigned
#        assignment_count = 0
#
#        seen_distances_index = 0
#        seen_distances = sorted(dist_to_pairs.keys())
#
#        while assignment_count < len(workers):
#            curr_dist = seen_distances[seen_distances_index]
#            seen_distances_index += 1
#            for i, j in dist_to_pairs[curr_dist]:
#                if worker_bikes[i] is None and not bike_assigned[j]:
#                    bike_assigned[j] = True
#                    worker_bikes[i] = j
#                    assignment_count += 1
#                if assignment_count >= len(workers):
#                    break
#
#        return worker_bikes
#   }}}

class Solution:
    """Given arrays of x-y coordinates of workers and bikes, pair each worker with the closest bike (calculated as Manhattan distance, |x1-x2| + |y1-y2|) such that the sum of all distances is minimised, and return that sum"""

    #   runtime: beats 5%
    def assignBikes_Backtracking_Greedy(self, workers: List[List[int]], bikes: List[List[int]]) -> int:

        def mdist(p1, p2):
            return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

        result = math.inf
        worker_bikes = [ None for _ in workers ]
        bike_assigned = [ False for _ in bikes ]
        assignments_count = 0

        def solve(worker_bikes, i, current_total_distance):
            nonlocal result
            nonlocal assignments_count
            if current_total_distance >= result:
                return
            if assignments_count == len(workers):
                result = min(current_total_distance, result)
                return
            for j, _ in enumerate(bike_assigned):
                if bike_assigned[j]:
                    continue
                worker_bikes[i] = j
                bike_assigned[j] = True
                assignments_count += 1
                new_total_distance = current_total_distance + mdist(workers[i], bikes[j])
                solve(worker_bikes, i+1, new_total_distance)
                worker_bikes[i] = None
                bike_assigned[j] = False
                assignments_count -= 1

        solve(worker_bikes, 0, 0)
        return result


    #   runtime: beats 87%
    def assignBikes_ans_DP_TopDown(self, workers: List[List[int]], bikes: List[List[int]]) -> int:

        def mdist(p1, p2):
            return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

        assigned_mask = [ False for _ in bikes ]

        @functools.cache
        def solve(worker_index, assigned_mask):
            if worker_index >= len(workers):
                return 0
            smallestDistanceSum = math.inf
            for bike_index in range(len(bikes)):
                if assigned_mask[bike_index] == False:
                    new_assigned_mask_1 = list(assigned_mask)
                    new_assigned_mask_1[bike_index] = True
                    temp1 = solve(worker_index + 1, tuple(new_assigned_mask_1))
                    smallestDistanceSum = min(smallestDistanceSum, mdist(workers[worker_index], bikes[bike_index]) + temp1)
            return smallestDistanceSum

        return solve(0, tuple(assigned_mask))


s = Solution()
test_functions = [ s.assignBikes_Backtracking_Greedy, s.assignBikes_ans_DP_TopDown, ]

#   {{{
inputs = [ ([[0,0],[1,1],[2,0]],[[1,0],[2,2],[2,1]]), ([[0,0],[1,0],[2,0],[3,0],[4,0]],[[0,999],[1,999],[2,999],[3,999],[4,999]]), ([[0,0],[1,0],[2,0],[3,0],[4,0],[5,0]],[[0,999],[1,999],[2,999],[3,999],[4,999],[5,999],[6,999]]), ]
checks = [ 4, 4995, 5994, ]
#   }}}
inputs = [ ([[0,0],[1,1],[2,0]],[[1,0],[2,2],[2,1]]), ([[0,0],[1,0],[2,0],[3,0],[4,0]],[[0,999],[1,999],[2,999],[3,999],[4,999]]), ([[0,0],[2,1]],[[1,2],[3,3]]), ]
checks = [ 4, 4995, 6, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for (workers, bikes), check in zip(inputs, checks):
        print(f"workers=({workers}), bikes=({bikes})")
        result = f(workers, bikes)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

