import time
import itertools
import functools
from typing import List, Optional


class Solution:

    digit_to_letters = { '1': [], '2': ['a','b','c'], '3': ['d','e','f'], '4': ['g','h','i'], '5': ['j','k','l'], '6': ['m','n','o'], '7': ['p','q','r','s'], '8': ['t','u','v'], '9': ['w','x','y','z'] }


    #   runtime: beats 90%
    def letterCombinations_Backtracking(self, digits: str) -> list[str]:
        if len(digits) == 0:
            return []

        result = []

        def backtrack(index, combination):
            if len(combination) == len(digits):
                result.append(''.join(combination))
                return
            #   letter possibilities for digit at 'index'
            d = digits[index]
            possible_letters = self.digit_to_letters[d]
            for c in possible_letters:
                combination.append(c)
                backtrack(index+1, combination)
                combination.pop()

        backtrack(0, [])
        return result


    #   runtime: beats 90%
    def letterCombinations_Itertools(self, digits: str) -> list[str]:
        if len(digits) == 0:
            return []
        all_possible_letters = [ self.digit_to_letters[x] for x in digits ]
        result = [ ''.join(x) for x in itertools.product(*all_possible_letters) ]
        return result


    #   runtime: beats 90%
    def letterCombinations_cartesianproduct(self, digits: str) -> list[str]:

        def cartesian_product(*iterables):
            pools = [ tuple(pool) for pool in iterables ]
            result = [ [] ]
            for pool in pools:
                result = [ x+[y] for x in result for y in pool ]
            return result

        if len(digits) == 0:
            return []
        all_possible_letters = [ self.digit_to_letters[x] for x in digits ]
        result = [ ''.join(x) for x in cartesian_product(*all_possible_letters) ]
        return result


    #   runtime: beats 5%
    def letterCombinations_iterNested(self, digits):
        if len(digits) == 0: 
            return []
        all_possible_letters = [ self.digit_to_letters[x] for x in digits ]
        result = ['']
        for loop_combinations in all_possible_letters:
            tmp = []
            for y in result:
                for x in loop_combinations:
                    tmp.append(y+x)
            result = tmp
        return result


    #   runtime: beats 86%
    def letterCombinations_oneline(self, digits):
        if len(digits) == 0: 
            return []
        f = lambda a, d: [ x+y for x in a for y in self.digit_to_letters[d]]
        return functools.reduce(f, digits, [''])


s = Solution()

test_functions = [ s.letterCombinations_Backtracking, s.letterCombinations_Itertools, s.letterCombinations_cartesianproduct, s.letterCombinations_iterNested, s.letterCombinations_oneline, ]

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

