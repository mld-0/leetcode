import time
from typing import List, Set, Optional

class Solution:
    """Return a list, `answer = [ answer1, answer2 ]`, where answer1 is a list of all the distinct integers in `nums1` not in `nums2`, and answer2 is a list of all the distinct integers in `nums2` not in `nums1`"""

    #   runtime: beats 96%
    def findDifference_set(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set(nums2)
        return [ list(s1-s2), list(s2-s1) ]


    #   runtime: beats 95%
    def findDifference_ii(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        def set_difference(a: Set[int], b: Set[int]) -> List[int]:
            l = []
            for x in a:
                if x not in b:
                    l.append(x)
            return l

        s1 = set(nums1)
        s2 = set(nums2)
        l1 = set_difference(s1, s2)
        l2 = set_difference(s2, s1)
        return [ l1, l2 ]


s = Solution()
test_functions = [ s.findDifference_set, s.findDifference_ii, ]

inputs = [ ([1,2,3],[2,4,6]), ([1,2,3,3],[1,1,2,2]), ([1,2,3,4,4,5,6,7,8,9,10,12,13,15,17],[2,3,3,5,7,9,11,12,14,16,17,19,20,21]), ]
checks = [ [[1,3],[4,6]], [[3],[]], [[1,4,6,8,10,13,15],[11,14,16,19,20,21]], ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for (nums1, nums2), check in zip(inputs, checks):
        print(f"nums1=({nums1}), nums2=({nums2})")
        result = f(nums1, nums2)
        print(f"result=({result})")
        assert sorted(result[0]) == sorted(check[0]), "Check comparison failed i"
        assert sorted(result[1]) == sorted(check[1]), "Check comparison failed ii"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()


