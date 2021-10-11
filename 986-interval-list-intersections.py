from typing import List

class Solution:

    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        return self.intervalIntersection_TwoPointers(firstList, secondList)

    def intervalIntersection_TwoPointers(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        """Given two sorted list of intervals (as start/end points), return intersection as a sorted list of intervals"""
        result = []

        #   position in A
        l = 0
        #   position in B
        r = 0

        #   for each pair of intervals
        while l < len(A) and r < len(B):
            #   start of interval
            low = max(A[l][0], B[r][0])
            #   end of interval
            high = min(A[l][1], B[r][1])

            if low <= high:
                result.append( [low, high] )

            #   Ongoing: 2021-10-11T22:18:14AEDT (why test ends) (and only ends) (and ignore starts)?
            #   advance interval with smaller end value
            if A[l][1] < B[r][1]:
                l += 1
            else:
                r += 1

        return result


s = Solution()

input_values = [ ([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]), ([[1,3],[5,9]], []), ([], [[4,8],[10,12]]), ([[1,7]], [[3,10]]) ]
input_checks = [ [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]], [], [], [[3,7]] ]

for (A, B), check in zip(input_values, input_checks):
    print("A=(%s), B=(%s)" % (A, B))
    result = s.intervalIntersection(A, B)
    print("result=(%s)" % result)
    assert result == check, "Check failed"
    print()
