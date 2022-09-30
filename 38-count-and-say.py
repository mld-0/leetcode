#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
from typing import List, Tuple
import sys
import logging
import re
#logging.basicConfig(level=logging.DEBUG, stream=sys.stderr)

class Solution:

    #   runtime: beats 87%
    def countAndSay_Iterative(self, n: int) -> str:
        if n == 1:
            return "1"
        t2 = "1"
        t1 = None
        for i in range(1,n):
            t1 = mapToFrequencies(t2)
            t2 = joinFrequencyPairs(t1)
        return t2

    #   runtime: beats 77%
    def countAndSay_RegexBackref(self, n: int) -> str:
        if n == 1:
            return "1"
        t2 = "1"
        t1 = None
        for i in range(1,n):
            t1 = mapToFrequencies_RegexBackref(t2)
            t2 = joinFrequencyPairs(t1)
        return t2

    #   runtime: beats 87%
    def countAndSay_RegexBackref_ans(self, n: int) -> str:
        s = "1"
        f = lambda x: str(len(x.group(0))) + x.group(1)
        for i in range(1,n):
            s = re.sub(r"(.)\1*", f, s)
        return s

def mapToFrequencies(s: str) -> List[Tuple[int,int]]:
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result.append( ( s[i-1], count ) )
            count = 1
    result.append( ( s[len(s)-1], count ) )
    return result

def mapToFrequencies_RegexBackref(s: str) -> List[Tuple[int,int]]:
    return [ ( x.group(1), len(x.group(0)) ) for x in re.finditer(r"([0-9])\1*", s) ]

def joinFrequencyPairs(pairs: List[Tuple[chr,int]]):
    pairs = [ str(x) for y in pairs for x in y[::-1] ]
    result = ''.join(pairs)
    return result

def test_mapToFrequencies():
    #   {{{
    values = [ "1", "3322251", "33222511", ]
    checks = [ [('1',1)], [('3',2),('2',3),('5',1),('1',1)], [('3',2),('2',3),('5',1),('1',2)], ]
    assert len(values) == len(checks)
    for value, check in zip(values, checks):
        result = mapToFrequencies(value)
        assert result == check, "Check comparison failed"
        result = mapToFrequencies_RegexBackref(value)
        assert result == check, "Check comparison failed"
    logging.debug("test_mapToFrequencies, DONE")
    #   }}}

def test_joinFrequencyPairs():
    #   {{{
    values = [ [('2',2),('3',2),('1',1),('4',5),('1',2)], [('1',1)], [('3',2),('2',3),('5',1),('1',1)], [('3',2),('2',3),('5',1),('1',2)], ]
    checks = [ "2223115421", "11", "23321511", "23321521", ]
    assert len(values) == len(checks)
    for value, check in zip(values, checks):
        result = joinFrequencyPairs(value)
        assert result == check, "Check comparison failed"
    logging.debug("test_joinFrequencyPairs, DONE")
    #   }}}

def run_tests():
    test_mapToFrequencies()
    test_joinFrequencyPairs()

run_tests()

s = Solution()
test_functions = [ s.countAndSay_Iterative, s.countAndSay_RegexBackref, s.countAndSay_RegexBackref_ans, ]

values = [ 1, 4, ]
checks = [ "1", "1211", ]
assert len(values) == len(checks)

for f in test_functions:
    print(f.__name__)
    for n, check in zip(values, checks):
        print("n=(%s)" % n)
        result = f(n)
        print("result=(%s)" % result)
        assert result == check, "Check comparison failed"
    print()

