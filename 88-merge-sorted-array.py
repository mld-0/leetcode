#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
from typing import List

class Solution:

    #   runtime: beats 98%
    def merge_threePointers(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        result = [ None for _ in range(m+n) ]
        i = 0
        j = 0
        k = 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                result[k] = nums1[i]
                i += 1
            else:
                result[k] = nums2[j]
                j += 1
            k += 1
        while i < m:
            result[k] = nums1[i]
            i += 1
            k += 1
        while j < n:
            result[k] = nums2[j]
            j += 1
            k += 1
        nums1[:] = result[:]


    #   runtime: beats 91%
    def merge_using_sorting(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2[:]
        nums1.sort()
    

    #   Whenever one needs to modify an array in-place, consider iterating backwards instead of forward
    #   runtime: beats 99%
    def merge_threePointers_inplace_i(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[i], nums1[k] = nums1[k], nums1[i]
                i -= 1
            else:
                nums2[j], nums1[k] = nums1[k], nums2[j]
                j -= 1
            k -= 1
        while i >= 0:
            nums1[k], nums1[i] = nums1[i], nums1[k]
            i -= 1
            k -= 1
        while j >= 0:
            nums1[k], nums2[j] = nums2[j], nums1[k]
            j -= 1
            k -= 1


    #   runtime: beats 98%
    def merge_threePointers_inplace_ii(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


    #   runtime: beats 96%
    def merge_ans(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        for k in range(n+m-1, -1, -1):
            if j < 0:
                break
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1


s = Solution()
test_functions = [ s.merge_threePointers, s.merge_using_sorting, s.merge_threePointers_inplace_i, s.merge_threePointers_inplace_ii, s.merge_ans, ]

input_values = [ ([1,2,3,0,0,0], 3, [2,5,6], 3), ([1], 1, [], 0), ([0], 0, [1], 1), ([4,5,6,0,0,0], 3, [1,2,3], 3), ([1,2,3,4,5], 5, [], 0), ([1,2,4,5,6,0], 5, [3], 1), ]
result_validation = [ [1,2,2,3,5,6], [1], [1], [1,2,3,4,5,6], [1,2,3,4,5], [1,2,3,4,5,6], ]
assert len(input_values) == len(result_validation)

for f in test_functions:
    print(f.__name__)
    for (nums1, m, nums2, n), check in zip(input_values, result_validation):
        nums1 = nums1[:]
        nums2 = nums2[:]
        print("nums1=(%s), m=(%s), nums2=(%s), n=(%s)" % (nums1, m, nums2, n))
        f(nums1, m, nums2, n)
        print("result=(%s)" % nums1)
        assert nums1 == check
    print()

