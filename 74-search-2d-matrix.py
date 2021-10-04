from typing import List

class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #return self.searchMatrix_linear(matrix, target)
        return self.searchMatrix_rowcol(matrix, target)

    #   runtime: beats 97%
    def searchMatrix_linear(self, matrix: List[List[int]], target: int) -> bool:
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

    #   runtime: beats 88%
    def searchMatrix_rowcol(self, matrix: List[List[int]], target: int) -> bool:
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
        print("row_search=(%s)" % row_search)

        #   binary search for col in row containing element
        col_l = 0
        col_r = len(matrix[0]) - 1
        while col_l <= col_r:
            col_mid = (col_r + col_l) // 2
            print("col_mid=(%s)" % col_mid)
            print("matrix[row_search][col_mid]=(%s)" % matrix[row_search][col_mid])
            if matrix[row_search][col_mid] == target:
                return True
            elif matrix[row_search][col_mid] > target:
                col_r = col_mid - 1
            elif matrix[row_search][col_mid] < target:
                col_l = col_mid + 1

        return False


s = Solution()

input_values = [ ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3), ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13), ([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 11), ]
input_checks = [ True, False, True, ]

for (matrix, target), check in zip(input_values, input_checks):
    print("matrix=(%s), target=(%s)" % (matrix, target))
    result = s.searchMatrix(matrix, target)
    print("result=(%s)" % result)
    assert result == check, "Check failed"
    print()

