import time
from collections import Counter

class Solution:

    #   runtime: TLE
    def buddyStrings_naive(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        for l in range(0, len(s)-1):
            for r in range(l+1, len(s)):
                trial = s[:l] + s[r] + s[l+1:r] + s[l] + s[r+1:]
                if trial == goal:
                    return True
        return False


    #   runtime: beats 98%
    def buddyStrings_ii(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            c = Counter(s)
            return any(count >= 2 for count in c.values())
        d = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                d.append(i)
        if len(d) != 2:
            return False
        return s[d[0]] == goal[d[1]] and s[d[1]] == goal[d[0]]


s = Solution()
test_functions = [ s.buddyStrings_naive, s.buddyStrings_ii, ]

inputs = [ ("ab","ba"), ("ab","ab"), ("aa","aa"), ("aaab","aaab"), ]
checks = [ True, False, True, True, ]
assert len(inputs) == len(checks)

for f in test_functions:
    print(f.__name__)
    startTime = time.time()
    for (s, goal), check in zip(inputs, checks):
        print(f"s=({s}), goal=({goal})")
        result = f(s, goal)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_ms=(%0.2f)" % ((time.time() - startTime) * 1000000))
    print()

