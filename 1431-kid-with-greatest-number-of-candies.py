import time
from typing import List, Optional

class Solution:
    """Determine which kids in `candies` will as many or more candies than anyone else if they are given `extraCandies`"""

    #   runtime: beats 95%
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)
        return [ True if i + extraCandies >= greatest else False for i in candies ]


s = Solution()
test_functions = [ s.kidsWithCandies, ]

inputs = [ ([2,3,5,1,3],3), ([4,2,1,1,2],1), ([12,1,12],10), ]
checks = [ [True,True,True,False,True], [True,False,False,False,False], [True,False,True], ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for (candies, extraCandies), check in zip(inputs, checks):
        print(f"candies=({candies}), extraCandies=({extraCandies})")
        result = f(candies, extraCandies)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

