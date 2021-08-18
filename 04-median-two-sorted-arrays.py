
class Solution:

    #   Result:
    #       runtime: 100ms (beats 31%)
    def findMedianSortedArray_First(self, nums1: list[int], nums2: list[int]) -> float:
        combined = []
        nums1_i = 0
        nums2_i = 0
        while (nums1_i < len(nums1) or nums2_i < len(nums2)):
            if nums1_i < len(nums1) and nums2_i < len(nums2):
                if nums1[nums1_i] < nums2[nums2_i]:
                    combined.append(nums1[nums1_i])
                    nums1_i += 1
                else:
                    combined.append(nums2[nums2_i])
                    nums2_i += 1
            elif nums1_i < len(nums1):
                combined += nums1[nums1_i:]
                break
            elif nums2_i < len(nums2):
                combined += nums2[nums2_i:]
                break
        midpoint = len(combined) // 2
        if len(combined) % 2 != 0:
            return combined[midpoint]
        else:
            return (combined[midpoint] + combined[midpoint-1]) / 2

    #   Result:
    #       runtime: 92ms (beats 66%)
    def findMedianSortedArray(self, nums1: list[int], nums2: list[int]) -> float:
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        combined_len = nums1_len + nums2_len
        index_median = [ combined_len // 2 ]
        median = [ None ]
        if (nums1_len+nums2_len) % 2 == 0:
            index_median = [ index_median[0]-1, index_median[0] ]
            median = [ None, None ] 
        i1 = 0
        i2 = 0
        val = None
        count = None
        while (None in median):
            count = i1 + i2 
            if i1 >= nums1_len:
                val = nums2[i2]
                i2 += 1
            elif i2 >= nums2_len:
                val = nums1[i1]
                i1 += 1
            elif nums1[i1] < nums2[i2]:
                val = nums1[i1]
                if nums1_len > i1:
                    i1 += 1
            else:
                val = nums2[i2]
                if nums2_len > i2:
                    i2 += 1
            if count == index_median[0]:
                median[0] = val
            if len(index_median) > 1 and count == index_median[1]:
                median[1] = val
        if len(median) == 1:
            return median[0]
        else:
            return (median[0]+median[1])/2


s = Solution()

nums1 = [1, 3]
nums2 = [2]
check = 2
result = s.findMedianSortedArray(nums1, nums2)
print("result=(%s)" % result)
assert(result == check)

nums1 = [1, 2]
nums2 = [3, 4]
check = 2.5
result = s.findMedianSortedArray(nums1, nums2)
print("result=(%s)" % result)
assert(result == check)

nums1 = [0, 0]
nums2 = [0, 0]
check = 0
result = s.findMedianSortedArray(nums1, nums2)
print("result=(%s)" % result)
assert(result == check)

nums1 = []
nums2 = [1]
check = 1
result = s.findMedianSortedArray(nums1, nums2)
print("result=(%s)" % result)
assert(result == check)

nums1 = [2]
nums2 = []
check = 2
result = s.findMedianSortedArray(nums1, nums2)
print("result=(%s)" % result)
assert(result == check)

