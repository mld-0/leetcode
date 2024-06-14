#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
from collections import Counter
from typing import List, Optional

class Solution:
    """Determine the number of times it is necessary to increment an element in the array to make each element in the array unique"""

    #   runtime: TLE
    def minIncrementForUnique_i(self, nums: List[int]) -> int:
        moves = 0
        nums = sorted(nums)
        counts = Counter(nums)
        remaining_non_unique = [ k for k, v in counts.items() if v > 1 ]
        for n in reversed(remaining_non_unique):
            while counts[n] > 1:
                current = n
                while current in counts:
                    current += 1
                    moves += 1
                counts[n] -= 1
                counts[current] = 1
        return moves


    #   runtime: TLE
    def minIncrementForUnique_ii(self, nums: List[int]) -> int:

        def sort_with_one_wrong_element(arr):
            n = len(arr)
            # Step 1: Identify the misplaced element
            misplaced_index = -1
            for i in range(n - 1):
                if arr[i] > arr[i + 1]:
                    misplaced_index = i
                    break
            if misplaced_index == -1:
                return arr  # The array is already sorted
            # Step 2: Identify where the misplaced element should go
            misplaced_value = arr[misplaced_index]
            correct_index = misplaced_index + 1
            while correct_index < n and arr[correct_index] < misplaced_value:
                correct_index += 1
            # Step 3: Remove the misplaced element and reinsert it at the correct position
            arr.pop(misplaced_index)
            arr.insert(correct_index - 1, misplaced_value)

        moves = 0
        nums = sorted(nums)
        for i in range(len(nums)-1, 0, -1):
            current = nums[i]
            previous = nums[i-1]
            j = i
            next_current = -1
            if current != previous:
                continue
            while j < len(nums)-1 and (nums[j] == nums[j+1] - 1 or nums[j] == nums[j+1]):
                j += 1
            next_current = nums[j] + 1
            delta = next_current - current
            moves += delta
            nums[i] = next_current
            sort_with_one_wrong_element(nums)
        return moves


    #   runtime: beats 88%
    #    memory: beats 54%
    def minIncrementForUnique_SortingIterative(self, nums: List[int]) -> int:
        moves = 0
        nums = sorted(nums)
        for i in range(1, len(nums)):
            current = nums[i]
            previous = nums[i-1]
            if current > previous:
                continue
            moves += previous - current + 1
            nums[i] = nums[i-1] + 1
        return moves


    #   runtime: beats 99%
    #    memory: beats 97%
    def minIncrementForUnique_ans_Counting(self, nums: List[int]) -> int:
        max_val = max(nums)
        result = 0
        frequency_count = [ 0 ] * (len(nums) + max_val + 1)
        for val in nums:
            frequency_count[val] += 1
        for i in range(len(frequency_count)):
            if frequency_count[i] <= 1:
                continue
            duplicates = frequency_count[i] - 1
            frequency_count[i+1] += duplicates
            frequency_count[i] = 1
            result += duplicates
        return result


s = Solution()
test_functions = [ s.minIncrementForUnique_i, s.minIncrementForUnique_ii, s.minIncrementForUnique_SortingIterative, s.minIncrementForUnique_ans_Counting, ]

inputs = [ [3,2,1,2,1,7], [1,2,2], [2,2,2,1], ]
checks = [ 6, 1, 3, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for s, check in zip(inputs, checks):
        print(f"s=({s})")
        result = f(s)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

