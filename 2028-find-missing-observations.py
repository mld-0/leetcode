#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
from typing import List, Optional

class Solution:
    """Find an array of `n` elements between [1,6] which when combined with the array `rolls` give an average value of `mean`"""

    #   runtime: beats 58%
    #    memory: beats 70%
    def missingRolls_i(self, rolls: List[int], mean: int, n: int) -> List[int]:
        result_total = mean * (len(rolls) + n) - sum(rolls)
        result_avg = result_total / n
        if result_avg > 6:
            return []
        if result_avg < 1:
            return []
        result = [ int(result_avg) ] * n
        delta_result = result_total - (int(result_avg) * n)
        for i in range(delta_result):
            result[i] += 1
        return result


    #   runtime: beats 73%
    #    memory: beats 77%
    def missingRolls_ii(self, rolls: List[int], mean: int, n: int) -> List[int]:
        result_total = mean * (len(rolls) + n) - sum(rolls)
        result_avg = result_total / n
        if result_avg > 6:
            return []
        if result_avg < 1:
            return []
        result = [ int(result_avg) ] * n
        delta_result = result_total - (int(result_avg) * n)
        i = 0
        while delta_result > 0:
            value = 6 - result[i]
            if value > delta_result:
                value = delta_result
            result[i] += value
            delta_result -= value
            i += 1
        return result


    #   runtime: beats 66%
    #    memory: beats 57%
    def missingRolls_ans(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sum_rolls = sum(rolls)
        # Find the remaining sum.
        remaining_sum = mean * (n + len(rolls)) - sum_rolls
        # Check if sum is valid or not.
        if remaining_sum > 6 * n or remaining_sum < n:
            return []
        distribute_mean = remaining_sum // n
        mod = remaining_sum % n
        # Distribute the remaining mod elements in n_elements list.
        n_elements = [distribute_mean] * n
        for i in range(mod):
            n_elements[i] += 1
        return n_elements


s = Solution()
test_functions = [ s.missingRolls_i, s.missingRolls_ii, s.missingRolls_ans, ]

inputs = [ ([3,2,4,3],4,2), ([1,5,6],3,4), ([1,2,3,4],6,4), ([6,1,5,2],4,4), ]
checks = [ [6,6], [2,3,2,2], [], [5,4,4,5], ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

def validate_result(result, check) -> bool:
    if len(result) != len(check): 
        return False
    if sum(result) != sum(check):
        return False
    return True

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for (rolls, mean, n), check in zip(inputs, checks):
        print(f"rolls=({rolls}), mean=({mean}), n=({n})")
        result = f(rolls, mean, n)
        print(f"result=({result})")
        assert validate_result(result, check), "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

