
def isBadVersion(version: int, bad: int) -> int:
    if version < bad:
        return 0
    return 1

class Solution:

    #   Result:
    #       runtime: beats 59%
    def firstBadVersion(self, n: int, bad: int) -> int:
        l = 1
        r = n

        while l < r:
            mid = (r + l) // 2

            if isBadVersion(mid, bad):
                r = mid
            else:
                l = mid + 1

        return l


s = Solution()

input_values = [ (5, 4), (1, 1), (3, 1) ]
input_check = [ 4, 1, 1 ]

for (n, bad), check in zip(input_values, input_check):
    result = s.firstBadVersion(n, bad)
    print("result=(%s)" % str(result))
    assert( result == check )
    print()

