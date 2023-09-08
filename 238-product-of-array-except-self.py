#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
from functools import cache
from typing import List, Optional

class Solution:
    """Find array `answer`, where each element `answer[i]` is the product of all elements of `nums` except `nums[i], in O(n), without using the division operator. Follow-up: solution which uses only O(1) extra space."""

    #   runtime: beats 60%
    def productExceptSelf_nSquaredWithMap(self, nums: List[int]) -> List[int]:
        """Not O(n)"""
        result = []
        seen = dict()
        for i, n in enumerate(nums):
            if not n in seen:
                product = 1
                for j, x in enumerate(nums):
                    if j == i:
                        continue
                    product *= x
                seen[n] = product
            result.append(seen[n])
        return result


    #   runtime: beats 92%
    def productExceptSelf_ans_divisionByAddingPowersOfTwoWithBithShifting(self, nums: List[int]) -> List[int]:
        """Not O(n)"""

        @cache
        def divide(dividend: int, divisor: int) -> int:
            """Adding Powers of Two with Bit-Shifting (taken from from 29-divide-two-integers answers)"""
            #   {{{
            # Constants.
            MAX_INT = 2147483647        # 2**31 - 1
            MIN_INT = -2147483648       # -2**31
            HALF_MIN_INT = -1073741824  # MIN_INT // 2
            # Special case: overflow.
            if dividend == MIN_INT and divisor == -1:
                return MAX_INT
            # We need to convert both numbers to negatives.
            # Also, we count the number of negatives signs.
            negatives = 2
            if dividend > 0:
                negatives -= 1
                dividend = -dividend
            if divisor > 0:
                negatives -= 1
                divisor = -divisor
            # In the first loop, we simply find the largest double of divisor
            # that fits into the dividend.
            # The >= is because we're working in negatives. In essence, that
            # piece of code is checking that we're still nearer to 0 than we
            # are to INT_MIN.
            highest_double = divisor
            highest_power_of_two = -1
            while highest_double >= HALF_MIN_INT and dividend <= highest_double + highest_double:
                highest_power_of_two += highest_power_of_two
                highest_double += highest_double
            # In the second loop, we work out which powers of two fit in, by
            # halving highest_double and highest_power_of_two repeatedly.
            # We can do this using bit shifting so that we don't break the
            # rules of the question :-)
            quotient = 0
            while dividend <= divisor:
                if dividend <= highest_double:
                    quotient += highest_power_of_two
                    dividend -= highest_double
                # We know that these are always even, so no need to worry about the
                # annoying "bit-shift-odd-negative-number" case.
                highest_power_of_two >>= 1
                highest_double >>= 1
            # If there was originally one negative sign, then
            # the quotient remains negative. Otherwise, switch
            # it to positive.
            return quotient if negatives == 1 else -quotient
            #   }}}

        seen_zeros = 0
        zero_index = None
        total_product = 1
        for i, n in enumerate(nums):
            if n == 0:
                seen_zeros += 1
                zero_index = i
            else:
                total_product *= n
        result = [ 0 for _ in nums ]
        if seen_zeros > 1:
            return result
        elif seen_zeros == 1:
            result[zero_index] = total_product
            return result
        for i, n in enumerate(nums):
            x = divide(total_product, n)
            result[i] = x
        return result


    #   runtime: beats 60%
    def productExceptSelf_ans_LRProductLists(self, nums: List[int]) -> List[int]:
        L_cum_product = [ 0 for _ in nums ]
        R_cum_product = [ 0 for _ in reversed(nums) ]

        cum_product = 1
        for i in range(len(nums)):
            cum_product *= nums[i]
            L_cum_product[i] = cum_product

        cum_product = 1
        for i in range(len(nums)-1, -1, -1):
            cum_product *= nums[i]
            R_cum_product[i] = cum_product

        result = [ 1 for _ in nums ]
        for i in range(len(nums)):
            if i > 0:
                result[i] *= L_cum_product[i-1]
            if i < len(nums)-1:
                result[i] *= R_cum_product[i+1]
        return result


    #   runtime: beats 97%
    def productExceptSelf_ans_LRProductConstSpace(self, nums: List[int]) -> List[int]:
        #   We use R_cum_product to store the result, so it doesn't count towards our O(1) space requirement
        R_cum_product = [ 0 for _ in nums ]
        cum_product = 1
        for i in range(len(nums)-1, -1, -1):
            cum_product *= nums[i]
            R_cum_product[i] = cum_product

        cum_product = nums[0]
        R_cum_product[0] = R_cum_product[1]
        for i in range(1, len(nums)-1):
            R_cum_product[i] = R_cum_product[i+1] * cum_product
            #   cum_product is equal to L_cum_product[i-1] for each eteration
            cum_product *= nums[i]
        R_cum_product[len(nums)-1] = cum_product

        return R_cum_product


s = Solution()
test_functions = [ s.productExceptSelf_nSquaredWithMap, s.productExceptSelf_ans_divisionByAddingPowersOfTwoWithBithShifting, s.productExceptSelf_ans_LRProductLists, s.productExceptSelf_ans_LRProductConstSpace, ]

inputs = [ [1,2,3,4], [-1,1,0,-3,3], [1,-1], [5,9,2,-9,-9,-7,-8,7,-9,10], ]
checks = [ [24,12,8,6], [0,0,9,0,0], [-1,1], [-51438240,-28576800,-128595600,28576800,28576800,36741600,32148900,-36741600,28576800,-25719120], ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for nums, check in zip(inputs, checks):
        print(f"nums=({nums})")
        result = f(nums)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

