#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
from typing import List
from collections import defaultdict

class Solution:

    #   runtime: beats 98%
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            result[''.join(sorted(s))].append(s)
        return list(result.values())


s = Solution()
functions = [ s.groupAnagrams, ]

inputs = [ ["eat","tea","tan","ate","nat","bat"], [""], ["a"], ]
checks = [ [["bat"],["nat","tan"],["ate","eat","tea"]], [[""]], [["a"]], ]
assert len(inputs) == len(checks)

for f in functions:
    print(f.__name__)
    for (strs, check) in zip(inputs, checks):
        print(f"strs=({strs})")
        result = f(strs)
        print(f"result=({result})")
        assert sorted( [ sorted(x) for x in result ] ) == sorted( [ sorted(x) for x in check ] ), "Check comparison failed"
    print()

