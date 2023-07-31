import time
import copy
from typing import List

class Solution:

    #   runtime: beats 97%
    def rotate_ans_rotate4(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        assert all(n == len(matrix[i]) for i in range(len(matrix)))

        for i in range(n//2 + n%2):
            for j in range(n//2):
                m = n-1-j
                k = n-1-i

                a = matrix[m][i]
                b = matrix[k][m]
                c = matrix[j][k]
                d = matrix[i][j]

                matrix[i][j] = a
                matrix[m][i] = b
                matrix[k][m] = c
                matrix[j][k] = d


    #   runtime: beats 99%
    def rotate_ans_transposeAndReflect(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        assert all(n == len(matrix[i]) for i in range(len(matrix)))

        def transpose(matrix, n):
            for i in range(n):
                for j in range(i+1, n):
                    matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

        def reflect(matrix, n):
            for i in range(n):
                for j in range(n//2):
                    matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]

        transpose(matrix, n)
        reflect(matrix, n)


s = Solution()
test_functions = [ s.rotate_ans_rotate4, s.rotate_ans_transposeAndReflect, ]

inputs = [ [[1,2,3],[4,5,6],[7,8,9]], [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]], ]
checks = [ [[7,4,1],[8,5,2],[9,6,3]], [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]], ]
assert len(inputs) == len(checks)

for f in test_functions:
    print(f.__name__)
    startTime = time.time()
    for matrix, check in zip(copy.deepcopy(inputs), checks):
        print(f"matrix=({matrix})")
        f(matrix)
        print(f"result=({matrix})")
        assert matrix == check, "Check comparison failed"
    print("elapsed_ms=(%0.2f)" % ((time.time() - startTime) * 1000000))
    print()

