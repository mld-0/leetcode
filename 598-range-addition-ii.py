
class Solution:

    #   Problem: For each element in m x n matrix, add 1 to elements at indexs 0<=x<i, 0<=y<j for (i,j) in ops, and return the count of the maximum value in matrix

    #   Results:
    #       memory limit exceded
    def maxCount_A(self, m: int, n: int, ops: list[list[int]]) -> int:
        if len(ops) == 0:
            return m * n
        A = [ [ 0 ] * n for x in range(m) ]
        maxval = 0
        for x, y in ops:
            for i in range(x):
                for j in range(y):
                    A[i][j] += 1
                    maxval = max(maxval, A[i][j])
        count = 0
        for i in range(m):
            for j in range(n):
                if A[i][j] == maxval:
                    count += 1
        return count

    #   Results:
    #       runtime: beats 75%
    def maxCount_Ans(self, m: int, n: int, ops: list[list[int]]) -> int:
        xval = m
        yval = n
        for x, y in ops:
            xval = min(xval, x)
            yval = min(yval, y)
        return xval*yval


    def maxCount(self, m: int, n: int, ops: list[list[int]]) -> int:
        return self.maxCount_Ans(m, n, ops)



s = Solution()

ops = [[2,2],[3,3]]
m = 3
n = 3
result = s.maxCount(m, n, ops)
expected = 4
print("maxCount(%s, %s, %s)" % (m, n, ops))
print("result=(%s)" % str(result))
assert(result == expected)
print()

m = 3
n = 3
ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
result = s.maxCount(m, n, ops)
expected = 4
print("maxCount(%s, %s, %s)" % (m, n, ops))
print("result=(%s)" % str(result))
assert(result == expected)
print()

m = 3
n = 3
ops = []
result = s.maxCount(m, n, ops)
expected = 9
print("maxCount(%s, %s, %s)" % (m, n, ops))
print("result=(%s)" % str(result))
assert(result == expected)
print()

m = 40000
n = 40000
ops = []
result = s.maxCount(m, n, ops)
expected = 40000 * 40000
print("maxCount(%s, %s, %s)" % (m, n, ops))
print("result=(%s)" % str(result))
print()

m = 39999
n = 39999
ops = [[19999, 19999]]
result = s.maxCount(m, n, ops)
expected = 19999 * 19999
print("maxCount(%s, %s, %s)" % (m, n, ops))
print("result=(%s)" % str(result))
print()

