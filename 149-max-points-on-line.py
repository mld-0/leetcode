#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modecount_slopes=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
from typing import List
import math
#   {{{2
class Solution:

    #   runtime: beats 95%
    def maxPoints(self, points: List[List[int]]) -> int:

        def max_points_on_line_containing_point(i: int) -> int:

            def slope_coprimes(x1: int, y1: int, x2: int, y2: int) -> List[int]:
                """Get the slope described by a pair of coordinates as a pair of co-prime numbers"""
                delta_x = x2 - x1
                delta_y = y2 - y1
                # vertical line
                if delta_x == 0:
                    return (math.inf, math.inf)  
                # horizontal line
                if delta_y == 0:
                    return (0, 0)  
                #   keep delta_x positive
                if delta_x < 0:
                    delta_x = -1 * delta_x
                    delta_y = -1 * delta_y
                gcd = math.gcd(delta_x, delta_y)
                #   slope represented as pair of integers to avoid rounding errors
                return ( delta_x / gcd, delta_y / gcd )

            def form_line_with_point(i: int, j: int, count: int, count_duplicates: int):
                """Given a pair of points, update 'count', 'count_duplicates', and 'count_slopes'"""
                x1 = points[i][0]
                y1 = points[i][1]
                x2 = points[j][0]
                y2 = points[j][1]
                #   duplicate point case
                if x1 == x2 and y1 == y2:
                    count_duplicates += 1
                else:
                    slope = slope_coprimes(x1, y1, x2, y2)
                    count_slopes[slope] = count_slopes.get(slope, 1) + 1
                    count = max(count_slopes[slope], count)
                return count, count_duplicates

            #   how many points have a given slope WRT point i
            count_slopes = dict()
            #   number of points on line with most points through point i
            count = 1
            #   how many points have same coordinates as point i
            count_duplicates = 0
            for j in range(i+1, len(points)):
                count, count_duplicates = form_line_with_point(i, j, count, count_duplicates)
            return count + count_duplicates

        #   less than 3 points -> all points fall on the same line
        if len(points) < 3:
            return len(points)

        #   result is number of points that form a line on the line with the most points
        result = 1
        #   for each point, determine max number of points that form a line with that point
        for i in range(len(points)-1):
            trial = max_points_on_line_containing_point(i)
            result = max(trial, result)
        return result


s = Solution()
test_functions = [ s.maxPoints, ]

input_values = [ [[1,1],[2,2],[3,3]], [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]], ]
input_checks = [ 3, 4, ]

for test_func in test_functions:
    print(test_func.__name__)
    for points, check in zip(input_values, input_checks):
        print("points=(%s)" % points)
        result = test_func(points)
        print("result=(%s)" % result)
    print()

