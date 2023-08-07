import time
from typing import List

class Solution:

    #   runtime: beats 99%
    def searchMatrix_revisit(self, matrix: List[List[int]], target: int) -> bool:

        def find_row(target):
            l = 0
            r = len(matrix) - 1
            while l <= r:
                mid = (l + r) // 2
                if matrix[mid][0] == target:
                    return mid
                elif matrix[mid][0] < target:
                    l = mid + 1
                elif matrix[mid][0] > target:
                    r = mid - 1
            return l - 1

        def find_col(target, row):
            l = 0
            r = len(matrix[row]) - 1
            while l <= r:
                mid = (l + r) // 2
                if matrix[row][mid] == target:
                    return mid
                elif matrix[row][mid] < target:
                    l = mid + 1
                elif matrix[row][mid] > target:
                    r = mid - 1
            return -1

        row = find_row(target)
        col = find_col(target, row)
        if col == -1:
            return False
        else:
            return True


    #   runtime: beats 97%
    def searchMatrix_linear(self, matrix: List[List[int]], target: int) -> bool:
        """Binary search of 2d matrix as 1d flattened list"""
        def get_element_linear_index(index: int) -> int:
            row = index // len(matrix[0])
            col = index % len(matrix[0])
            return matrix[row][col]

        l = 0
        r = (len(matrix) * len(matrix[0])) - 1

        while l <= r:
            mid = (l + r) // 2
            if get_element_linear_index(mid) == target:
                return True
            elif get_element_linear_index(mid) < target:
                l = mid + 1
            elif get_element_linear_index(mid) > target:
                r = mid - 1

        return False


    #   runtime: beats 98%
    def searchMatrix_rowcol(self, matrix: List[List[int]], target: int) -> bool:
        """Binary search to identify row, then binary search to identify col"""
        #   binary search for row containing element
        row_l = 0
        row_r = len(matrix) - 1
        while row_l <= row_r:
            row_mid = (row_r + row_l) // 2
            if matrix[row_mid][0] == target:
                return True
            elif matrix[row_mid][0] > target:
                row_r = row_mid - 1
            elif matrix[row_mid][0] < target:
                row_l = row_mid + 1

        #   row containing result
        row_search = row_l
        if row_search > 0:
            row_search -= 1

        #   binary search for col in row containing element
        col_l = 0
        col_r = len(matrix[0]) - 1
        while col_l <= col_r:
            col_mid = (col_r + col_l) // 2
            if matrix[row_search][col_mid] == target:
                return True
            elif matrix[row_search][col_mid] > target:
                col_r = col_mid - 1
            elif matrix[row_search][col_mid] < target:
                col_l = col_mid + 1

        return False


s = Solution()
test_functions = [ s.searchMatrix_revisit, s.searchMatrix_linear, s.searchMatrix_rowcol, ]

inputs = [ ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3), ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13), ([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 11), ([[1,2,3],[4,5,6]],2), ([[1,2,3],[4,5,6]],1), ]
checks = [ True, False, True, True, True, ]
assert len(inputs) == len(checks)

for f in test_functions:
    print(f.__name__)
    startTime = time.time()
    for (matrix, target), check in zip(inputs, checks):
        print("matrix=(%s), target=(%s)" % (matrix, target))
        result = f(matrix, target)
        print("result=(%s)" % result)
        assert result == check, "Check comparison failed"
    print(f"elapsed_ms=(%0.2f)" % ((time.time() - startTime) * 1_000_000))
    print()

