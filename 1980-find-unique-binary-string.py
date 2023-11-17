import time
from typing import List, Optional

class Solution:
    """Given a list of binary numbers (as strings), `nums`, all of length n, find a binary number which does not appear in `nums`"""

    #   runtime: beats 8%
    def findDifferentBinaryString_i(self, nums: List[str]) -> str:
        max_len = len(nums[0])
        binary_strings = set( [ format(i, f'0{max_len}b') for i in range(2**max_len) ] )
        missing_values = binary_strings - set(nums)
        return list(missing_values)[0]


    #   runtime: beats 94%
    def findDifferentBinaryString_ii(self, nums: List[str]) -> str:
        max_len = len(nums[0])
        nums = set(nums)
        for i in range(2**max_len):
            b = format(i, f'0{max_len}b')
            if b not in nums:
                return b


    #   runtime: beats 99%
    def findDifferentBinaryString_ans_Recusive(self, nums: List[str]) -> str:

        def solve(curr):
            if len(curr) == n:
                if curr not in nums:
                    return curr
                return ""
            temp = solve(curr + "0")
            if temp:
                return temp
            return solve(curr + "1")

        n = len(nums[0])
        nums = set(nums)
        return solve("")


    #   runtime: beats 96%
    def findDifferentBinaryString_ans_DiagonalAssignment(self, nums: List[str]) -> str:
        ans = []
        for i in range(len(nums)):
            curr = nums[i][i]
            ans.append("1" if curr == "0" else "0")
        return "".join(ans)


s = Solution()
test_functions = [ s.findDifferentBinaryString_i, s.findDifferentBinaryString_ii, s.findDifferentBinaryString_ans_Recusive, s.findDifferentBinaryString_ans_DiagonalAssignment, ]

inputs = [ ["01","10"], ["00","01"], ["111","011","001"], ]
checks = [ ["11","00"], ["11","10"], ["101","000","010","100","110"], ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for vals, check in zip(inputs, checks):
        print(f"vals=({vals})")
        result = f(vals)
        print(f"result=({result})")
        assert result in check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

