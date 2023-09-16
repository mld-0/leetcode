import time
from typing import List, Optional

class Solution:
    """Each element in `asteroids` has a size given by its magnitude, and a constant speed whose direction given by its sign. When two asteroids collide, the smaller one explodes (or both explode if they are the same size). Determine which asteroids remain after all collisions take place."""

    #   runtime: beats 87%
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        i = 0
        while i < len(asteroids):
            peek = None
            if len(result) > 0:
                peek = result[-1]
            else:
                result.append(asteroids[i])
                i += 1
                continue
            if peek > 0 and asteroids[i] < 0:
                if abs(peek) == abs(asteroids[i]):
                    result.pop()
                    i += 1
                elif abs(peek) > abs(asteroids[i]):
                    i += 1
                elif abs(peek) < abs(asteroids[i]):
                    result.pop() 
            else:
                result.append(asteroids[i])
                i += 1
        return result


    #   runtime: beats 95%
    def asteroidCollision_ans_i(self, asteroids: List[int]) -> List[int]:
        result = []
        s = []
        for x in asteroids:
            if x > 0:
                s.append(x)
            else:
                while len(s) > 0 and s[-1] < abs(x):
                    s.pop()
                if len(s) == 0:
                    result.append(x)
                else:
                    if s[-1] == abs(x):
                        s.pop()
        result += s
        return result


s = Solution()
test_functions = [ s.asteroidCollision, s.asteroidCollision_ans_i, ]

inputs = [ [5,10,-5], [8,-8], [10,2,-5], [-2,-1,1,2], [-2,-2,1,-2], ]
checks = [ [5,10], [], [10], [-2,-1,1,2], [-2,-2,-2], ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for asteroids, check in zip(inputs, checks):
        print(f"asteroids=({asteroids})")
        result = f(asteroids)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

