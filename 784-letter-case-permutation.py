import functools
import itertools
from typing import List

def is_sortable(obj):
    cls = obj.__class__
    return cls.__lt__ != object.__lt__ or cls.__gt__ != object.__gt__
  
class Solution:

    def letterCasePermutation(self, s: str) -> List[str]:
        return self.letterCasePermutation_Itertools_C(s)

    #   runtime: beats 98%
    def letterCasePermutation_Itertools_A(self, s: str) -> List[str]:
        split_letters_capitalpair = lambda c: [ c.upper(), c.lower() ] if c.isalpha() else [ c ]
        s_split = [ split_letters_capitalpair(x) for x in s ]
        result = [ ''.join(x) for x in itertools.product(*s_split) ]
        return result

    #   runtime: beats 98%
    def letterCasePermutation_Itertools_B(self, s: str) -> List[str]:
        split_letters_capitalpair = lambda c: [ c.upper(), c.lower() ] if c.isalpha() else [ c ]
        s_split = map(split_letters_capitalpair, s)
        result = [ ''.join(x) for x in itertools.product(*s_split) ]
        return result

    #   runtime: beats 87%
    def letterCasePermutation_Itertools_C(self, s: str) -> List[str]:

        def product(*args, repeat=1):
            """Implement itertools.product()"""
            #   LINK: https://docs.python.org/3/library/itertools.html#itertools.product
            # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
            # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
            pools = [tuple(pool) for pool in args] * repeat
            result = [[]]
            for pool in pools:
                result = [x+[y] for x in result for y in pool]
            for prod in result:
                yield tuple(prod)

        split_letters_capitalpair = lambda c: [ c.upper(), c.lower() ] if c.isalpha() else [ c ]
        s_split = [ split_letters_capitalpair(x) for x in s ]
        result = [ ''.join(x) for x in product(*s_split) ]
        return result


    def letterCasePermutation_Recursive(self, s: str) -> List[str]:
        raise NotImplementedError()


    def letterCasePerumtation_BinaryMask(self, s: str) -> List[str]:
        raise NotImplementedError()
    

s = Solution()

input_values = [ "a1b2", "3z4", "12345", "0" ]
input_checks = [ ["a1b2","a1B2","A1b2","A1B2"], ["3z4","3Z4"], ["12345"], ["0"] ]

for loop_str, check in zip(input_values, input_checks):
    result = s.letterCasePermutation(loop_str)
    print("result=(%s)" % str(result))
    assert is_sortable(result), "'is_sortable()' failed"
    assert sorted(result) == sorted(check)
    print()

