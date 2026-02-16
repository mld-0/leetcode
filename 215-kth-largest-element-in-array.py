import time
from collections import heapq
import heapq
from typing import List, Optional

class Solution:
    """Find the k-th largest value in a list (including duplicates)"""

    #   runtime: beats 9%
    #    memory: beats 6%
    def findKthLargest_heapq_i(self, nums: List[int], k: int) -> int:
        top_k = heapq.nlargest(k, nums)
        return top_k[-1]


    #   runtime: beats 10%
    #    memory: beats 6%
    def findKthLargest_heapq_ii(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)
        top_k = heapq.nlargest(k, nums)
        return top_k[-1]


    #   runtime: beats 80%
    #    memory: beats 25%
    def findKthLargest_sort(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]


    def findKthLargest_countingSort(self, nums: List[int], k: int) -> int:
        raise NotImplementedError("Review counting-sort and ans quickselect / heap-implementation")



    #   runtime: beats 60%
    #    memory: beats 50%
    def findKthLargest_ans_heapq(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]


    def findKthLargest_ans_quickselect(self, nums: List[int], k: int) -> int:
        raise NotImplementedError("Review counting-sort and ans quickselect / heap-implementation")


    def findKthLargest_ans_heap(self, nums: List[int], k: int) -> int:
        #   Leetcode on heaps: https://leetcode.com/explore/learn/card/heap/643/heap/
        raise NotImplementedError("Review counting-sort and ans quickselect / heap-implementation")



s = Solution()
test_functions = [ s.findKthLargest_heapq_i, s.findKthLargest_heapq_ii, s.findKthLargest_sort, s.findKthLargest_countingSort, s.findKthLargest_ans_heapq, s.findKthLargest_ans_quickselect, ]

inputs = [ ([3,2,1,5,6,4],2), ([3,2,3,1,2,4,5,5,6],4), ]
checks = [ 5, 4, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for (nums,k), check in zip(inputs, checks):
        nums = nums[:]
        print(f"nums=({nums}), k=({k})")
        result = f(nums, k)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

