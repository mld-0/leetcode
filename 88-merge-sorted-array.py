from typing import List

class Solution:

    #   runtime: beats 98%
    def merge_threePointers(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        result = [ None for _ in range(m+n) ]
        i = 0
        j = 0
        k = 0
        while i < m and j < n:
            if (nums1[i] <= nums2[j]):
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
    

    #   Continue: 2022-08-28T21:39:35AEST leetcode, 88-merge-sorted-array, merge_inplace (two/three-pointers)
    def merge_inplace(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        ...
        #i = 0
        #j = 0
        #while i < m and j < n:
        #    if nums1[i] <= nums2[j]:
        #        pass
        #    else:
        #        nums1[m] = nums1[i]
        #        nums1[i] = nums2[j]
        #        j += 1
        #        #i -= 1
        #    print("nums1=(%s), i=(%s), nums2=(%s), j=(%s)" % (nums1, i, nums2, j))
        #    i += 1
        #print("nums1=(%s), i=(%s), nums2=(%s), j=(%s)" % (nums1, i, nums2, j))
        #while j < n:
        #    nums1[i] = nums2[j]
        #    print("nums1=(%s), i=(%s), nums2=(%s), j=(%s)" % (nums1, i, nums2, j))
        #    i += 1
        #    j += 1


s = Solution()
test_functions = [ s.merge_threePointers, s.merge_using_sorting, ]
#test_functions = [ s.merge_threePointers, s.merge_using_sorting, s.merge_inplace, ]

inputs = [ ([1,2,3,0,0,0], 3, [2,5,6], 3), ([1], 1, [], 0), ([0], 0, [1], 1), ([4,5,6,0,0,0], 3, [1,2,3], 3), ]
validation = [ [1,2,2,3,5,6], [1], [1], [1,2,3,4,5,6], ]
assert len(inputs) == len(validation)

for f in test_functions:
    print(f.__name__)
    for (nums1, m, nums2, n), check in zip(inputs, validation):
        nums1 = nums1[:]
        nums2 = nums2[:]
        print("nums1=(%s), m=(%s), nums2=(%s), n=(%s)" % (nums1, m, nums2, n))
        f(nums1, m, nums2, n)
        print("result=(%s)" % nums1)
        assert nums1 == check
    print()

