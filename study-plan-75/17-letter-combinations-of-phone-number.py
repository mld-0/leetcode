import time
from typing import List, Optional

class Solution:

    #   runtime: beats 87%
    def letterCombinations(self, digits: str) -> List[str]:
        letters_map = { k: [c for c in v] for k, v in { 1: '', 2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz' }.items() }

        def backtrack(index: int, combination: List[str]):
            if index >= len(digits):
                result.append(''.join(combination))
                return
            current_digit = int(digits[index])
            for v in letters_map[current_digit]:
                combination.append(v)
                backtrack(index+1, combination)
                combination.pop()

        if len(digits) == 0:
            return []
        result = []
        backtrack(0, [])
        return result 


s = Solution()
test_functions = [ s.letterCombinations, ]

inputs = [ "23", "", "2" ]
checks = [ ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], [], ["a", "b", "c"] ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for digits, check in zip(inputs, checks):
        print(f"digits=({digits})")
        result = f(digits)
        print(f"result=({result})")
        assert set(result) == set(check), "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

