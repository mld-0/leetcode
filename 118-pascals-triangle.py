from typing import List

class Solution:

    def generate(self, numRows: int) -> List[List[int]]:
        return self.generate_DP(numRows)

    def generate_DP(self, numRows: int) -> List[List[int]]:
        result = [ [ None for col in range(row+1) ] for row in range(numRows) ]
        result[0][0] = 1

        for row in range(1, numRows):
            result[row][0] = 1
            result[row][-1] = 1

        for row in range(1, numRows):
            for col in range(1, row):
                result[row][col] = result[row-1][col-1] + result[row-1][col]

        return result


    #   runtime: beats 97%
    def generate_iii(self, numRows: int) -> List[List[int]]:
        result = [ [ 1 for _ in range(row+1)] for row in range(numRows) ]
        for row in range(1, numRows):
            for col in range(1, row):
                result[row][col] = result[row-1][col-1] + result[row-1][col]
        return result


s = Solution()
test_functions = [ s.generate_DP, s.generate_iii, ]

input_values = [ 5, 1, ]
input_checks = [ [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]], [[1]], ]
assert len(input_values) == len(input_checks)


for test_func in test_functions:
    print(test_func.__name__)
    for numRows, check in zip(input_values, input_checks):
        print("numRows=(%s)" % numRows)
        result = s.generate(numRows)
        print("result=(%s)" % str(result))
        assert result == check, "Check failed"
    print()

