from typing import List

class Solution:

    #   runtime: beats 45%
    def findClosestElements_Sort(self, arr: List[int], k: int, x: int) -> List[int]:
        f = lambda n: abs(x-n)
        arr = sorted(arr, key = f)
        arr = sorted(arr[:k])
        return arr


    #   runtime: beats 92%
    def findClosestElements_twoPointers(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr) - 1
        while r - l >= k:
            a = arr[l]
            b = arr[r]
            delta_a = abs(a - x)
            delta_b = abs(b - x)
            if delta_a < delta_b or (delta_a == delta_b and a < b):
                r -= 1
            else:
                l += 1
        return arr[l:r+1]


    def findClosestElements_twoPointersBinarySearch(self, arr: List[int], k: int, x: int) -> List[int]:
        ...


s = Solution()
#test_functions = [ s.findClosestElements_Sort, s.findClosestElements_twoPointers, s.findClosestElements_twoPointersBinarySearch, ]
test_functions = [ s.findClosestElements_Sort, s.findClosestElements_twoPointers, ]

input_values = [ ([1,2,3,4,5], 4, 3), ([1,2,3,4,5], 4, -1), ]
result_validation = [ [1,2,3,4], [1,2,3,4], ]
assert len(input_values) == len(result_validation)

for f in test_functions:
    print(f.__name__)
    for (arr, k, x), check in zip(input_values, result_validation):
        print("arr=(%s), k=(%s), x=(%s)" % (arr, k, x))
        result = f(arr, k, x)
        print("result=(%s)" % result)
        assert result == check
    print()

