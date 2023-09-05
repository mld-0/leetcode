import time
from typing import List, Optional

class Solution:
    """Flowers cannot be placed in adjacent spots in array `flowerbed`, is it possible to insert `n` more flowers?"""

    #   runtime: beats 99%
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:    

        def can_place(i: int) -> bool:
            if flowerbed[i] == 1:
                return False
            if i > 0 and flowerbed[i-1] == 1:
                return False
            if i <= len(flowerbed)-2 and flowerbed[i+1] == 1:
                return False
            return True

        placed = 0
        for i in range(len(flowerbed)):
            if can_place(i):
                flowerbed[i] = 1
                placed += 1
        return placed >= n


s = Solution()
test_functions = [ s.canPlaceFlowers, ]

inputs = [ ([1,0,0,0,1],1), ([1,0,0,0,1],2), ([1,0,0,0,0,1],2), ]
checks = [ True, False, False, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for (flowerbed, n), check in zip(inputs, checks):
        print(f"flowerbed=({flowerbed}), n=({n})")
        result = f(flowerbed, n)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

