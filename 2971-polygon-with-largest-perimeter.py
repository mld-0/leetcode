#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
import heapq
from typing import List, Optional
#   arg_printer(args: List, arg_names: List), list2str(vals: List, max_str_length: int=60) {{{
def arg_printer(args: List, arg_names: List):  
    assert len(args) == len(arg_names), "input args / arg_names length mismatch"
    output = ""
    for arg, arg_name in zip(args, arg_names):
        output += f"{arg_name}=({list2str(arg)}), "
    print(output[:-2])
def list2str(vals: List, max_str_length: int=60):  
    def build_string(vals, num_elements):
        if num_elements < len(vals):
            return f"[{','.join(map(str, vals[:num_elements]))},...,{vals[-1]}]"
        else:
            return str(vals)
    if type(vals) != type([]):
        return str(vals)
    if len(vals) == 0:
        return str(vals)
    num_elements = len(vals)
    while num_elements > 0:
        formatted_list = build_string(vals, num_elements)
        if len(formatted_list) <= max_str_length:
            break
        num_elements -= 1
    return formatted_list
#   }}}

class Solution:
    """Given lengths [a1,a2,a3,...,ak] a polygon can be formed if a1<=a2<=a3<=...<=ak and a1+a2+a3+...>ak. Determine the largest perimeter of a polygon whose sides can be formed from the lengths in `nums`"""

    #   runtime: beats 40%
    def largestPerimeter_PrefixSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        prefix_sum = nums[:]
        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
        i = 2
        result_i = i
        while i < len(nums):
            if nums[i] < prefix_sum[i-1]:
                result_i = i
            i += 1
        if result_i == 2:
            if nums[2] < prefix_sum[1]:
                return prefix_sum[result_i]
            else:
                return -1
        return prefix_sum[result_i]


    #   runtime: beats 45%
    def largestPerimeter_PrefixSumOptimised(self, nums: List[int]) -> int:
        nums = sorted(nums)
        i = 2
        result_i = i
        prefix_sum = sum(nums[:2])
        result = prefix_sum
        while i < len(nums):
            if nums[i] < prefix_sum:
                result_i = i
                result = prefix_sum + nums[i]
            prefix_sum += nums[i]
            i += 1
        if result_i == 2:
            if nums[2] < result:
                return result
            else:
                return -1
        return result


    #   runtime: beats 65%
    def largestPerimeter_ans_Iterative(self, nums: List[int]) -> int:
        nums = sorted(nums)
        previous_elements_sum = 0
        ans = -1
        for num in nums:
            if num < previous_elements_sum:
                ans = num + previous_elements_sum
            previous_elements_sum += num
        return ans


    #   runtime: beats 98%
    def largestPerimeter_ans_Stack(self, nums: List[int]) -> int:
        A = sorted(nums)
        cur = sum(A)
        while A and cur <= A[-1] * 2:
            cur -= A.pop()
        return sum(A) if len(A) > 2 else -1


    #   runtime: beats 98%
    def largestPerimeter_ans_PriorityQueue(self, nums: List[int]) -> int:
        A = nums[:]
        cur = sum(A)
        heapq._heapify_max(A)
        while A and cur <= A[0] * 2:
            cur -= heapq._heappop_max(A)
        return cur if len(A) > 2 else -1


s = Solution()
test_functions = [ s.largestPerimeter_PrefixSum, s.largestPerimeter_PrefixSumOptimised, s.largestPerimeter_ans_Iterative, s.largestPerimeter_ans_Stack, s.largestPerimeter_ans_PriorityQueue, ]
arg_names = ["nums"]

inputs = [ [5,5,5], [1,12,1,2,5,50,3], [5,5,50], [1,5,1,5], [50,12,2,3,4], [1,33,25,42,12,2,20,14,4,22], [1,5,1,7], ]
checks = [ 15, 12, -1, 12, 9, 175, -1, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for args, check in zip(inputs, checks):
        if type(args) != type(tuple()) and len(arg_names) == 1: args = tuple([args])
        arg_printer(args, arg_names)
        result = f(*args)
        print(f"result=({list2str(result)})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

