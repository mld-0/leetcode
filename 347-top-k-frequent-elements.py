import time
import heapq
import random
from typing import List
from collections import Counter

class Solution:

    #   runtime: beats 75%
    def topKFrequent_CounterSorted(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        top_nums_by_count = sorted(counts.keys(), key=lambda x: counts[x], reverse=True)
        return top_nums_by_count[:k]


    #   runtime: beats 93%
    def topKFrequent_ans_CounterHeapSorted(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        return heapq.nlargest(k, counts.keys(), key=lambda x: counts[x])


    #   runtime: beats 55%
    def topKFrequent_ans_Quickselect(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        unique = list(count.keys())

        def partition(left, right, pivot_index) -> int:
            pivot_frequency = count[unique[pivot_index]]
            # 1. move pivot to end
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]  
            # 2. move all less frequent elements to the left
            store_index = left
            for i in range(left, right):
                if count[unique[i]] < pivot_frequency:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    store_index += 1
            # 3. move pivot to its final place
            unique[right], unique[store_index] = unique[store_index], unique[right]  
            return store_index

        def quickselect(left, right, k_smallest) -> None:
            """Sort a list within left..right till kth less frequent element takes its place"""
            # base case: the list contains only one element
            if left == right: 
                return
            # select a random pivot_index
            pivot_index = random.randint(left, right)     
            # find the pivot position in a sorted list   
            pivot_index = partition(left, right, pivot_index)
            # if the pivot is in its final sorted position
            if k_smallest == pivot_index:
                 return 
            # go left
            elif k_smallest < pivot_index:
                quickselect(left, pivot_index - 1, k_smallest)
            # go right
            else:
                quickselect(pivot_index + 1, right, k_smallest)

        # kth top frequent element is (n-k)th less frequent. Do a partial sort: from less frequent to the most frequent, till (n-k)th less frequent element takes its place (n-k) in a sorted array. All element on the left are less frequent. All the elements on the right are more frequent.  
        n = len(unique) 
        quickselect(0, n - 1, n - k)
        return unique[n-k:]


s = Solution()
test_functions = [ s.topKFrequent_CounterSorted, s.topKFrequent_ans_CounterHeapSorted, s.topKFrequent_ans_Quickselect, ]

inputs = [ ([1,1,1,2,2,3], 2), ([1], 1), ([4,4,4,4,5], 1), ([1,2,3,4,5],5), ([7,7,5,5,5,8,8,8,8], 2), ([6,6,9,9,9,6,6,9,9,1,1,1,1,1], 3), ]
checks = [ [1,2], [1], [4], [1,2,3,4,5], [8,5], [1,9,6], ]
assert len(inputs) == len(checks)

for f in test_functions:
    print(f.__name__)
    startTime = time.time()
    for (nums, k), check in zip(inputs, checks):
        print(f"nums=({nums}), k=({k})")
        result = f(nums, k)
        print(f"result=({result})")
        assert sorted(result) == sorted(check), "Check comparison failed"
    print("elapsed_ms=(%0.2f)" % ((time.time() - startTime) * 1000000))
    print()

