import itertools
import functools

def cartesian_product(*iterables):
    pools = [tuple(pool) for pool in iterables]
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)

class Solution:

    digit_to_letters = { '1': [], '2': ['a','b','c'], '3': ['d','e','f'], '4': ['g','h','i'], '5': ['j','k','l'], '6': ['m','n','o'], '7': ['p','q','r','s'], '8': ['t','u','v'], '9': ['w','x','y','z'] }

    def letterCombinations(self, digits: str) -> list[str]:
        #return self.letterCombinations_A(digits)
        #return self.letterCombinations_iterNested(digits)
        return self.letterCombinations_oneline(digits)

    #   Result:
    #       runtime: beats 63%
    def letterCombinations_A(self, digits: str) -> list[str]:
        combinations_list = [ self.digit_to_letters[x] for x in digits ]
        result = [ ''.join(x) for x in itertools.product(*combinations_list) ]
        return result

    #   Result:
    #       runtime: beats 96%
    def letterCombinations_cartesianproduct(self, digits: str) -> list[str]:
        combinations_list = [ self.digit_to_letters[x] for x in digits ]
        result = [ ''.join(x) for x in cartesian_product(*combinations_list) ]
        return result

    #   Result:
    #       runtime: beats 5%
    def letterCombinations_iterNested(self, digits):
        combinations_list = [ self.digit_to_letters[x] for x in digits ]
        result = ['']
        for loop_combinations in combinations_list:
            tmp = []
            for y in result:
                for x in loop_combinations:
                    tmp.append(y+x)
            result = tmp
        return result

    #   Result:
    #       runtime: beats 86%
    def letterCombinations_oneline(self, digits):
        if len(digits) == 0: 
            return []
        return functools.reduce(lambda a, d: [ x+y for x in a for y in self.digit_to_letters[d]], digits, [''])

s = Solution()

digits_list = [ "23", "", "2" ]
check_list = [ ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], [], ["a", "b", "c"] ]

for digits, check in zip(digits_list, check_list):
    result = s.letterCombinations(digits)
    print("result=(%s)" % result)
    print()


