#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
from collections import Counter
from typing import List, Optional

class Solution:
    """Given two sentences, determine the words which occur exactly once in one sentence and do not occur in the other"""

    #   runtime: beats 97%
    #    memory: beats 44%
    def uncommonFromSentences_i(self, s1: str, s2: str) -> List[str]:
        s1 = Counter(s1.split())
        s2 = Counter(s2.split())
        s1_single = set( [ k for k, v in s1.items() if v == 1 ] )
        s2_single = set( [ k for k, v in s2.items() if v == 1 ] )
        s1_multiple = s1.keys() - s1_single
        s2_multiple = s2.keys() - s2_single
        all_single_words = s1_single | s2_single
        result = []
        for word in all_single_words:
            in_s1_single = word in s1_single
            in_s2_single = word in s2_single
            if in_s1_single and in_s2_single:
                continue
            if not (in_s1_single or in_s2_single):
                continue
            if word in s1_multiple or word in s2_multiple:
                continue
            result.append(word)
        return result


    #   runtime: beats 97%
    #    memory: beats 78%
    def uncommonFromSentences_ii(self, s1: str, s2: str) -> List[str]:
        s1 = Counter(s1.split())
        s2 = Counter(s2.split())
        words = s1.keys() | s2.keys()
        result = []
        for word in words:
            if word in s1 and word in s2:
                continue
            if word in s1 and s1[word] > 1:
                continue
            if word in s2 and s2[word] > 1:
                continue
            result.append(word)
        return result


    #   runtime: beats 98%
    #    memory: beats 97%
    def uncommonFromSentences_ans(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split()
        s2 = s2.split()
        c = Counter()
        c.update(s1)
        c.update(s2)
        return [ word for word, count in c.items() if count == 1 ] 


s = Solution()
test_functions = [ s.uncommonFromSentences_i, s.uncommonFromSentences_ii, s.uncommonFromSentences_ans, ]

inputs = [ ("this apple is sweet", "this apple is sour"), ("apple apple", "banana"), ("s z z z s", "s z ejt"), ]
checks = [ ["sweet", "sour"], ["banana"], ["ejt"], ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for (s1, s2), check in zip(inputs, checks):
        print(f"s1=({s1}), s2=({s2})")
        result = f(s1, s2)
        print(f"result=({result})")
        assert set(result) == set(check), "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

