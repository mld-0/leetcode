#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
from collections import deque
from functools import cache
from typing import List, Optional

class Solution:
    """Given a circle of players, labeled [1,n], progress clockwise around the circle k-1 times at each stage, removing the player landed on and progressing to the next. Return the last remaining player when starting at player 1."""


    #   runtime: beats 29%
    #    memory: beats 49%
    def findTheWinner_Map(self, n: int, k: int) -> int:
        next_player = dict()
        for i in range(1, n+1):
            next_player[i] = i + 1
        next_player[n] = 1
        previous_player = 1
        current_player = 1
        num_removed = 0
        while num_removed < n-1:
            for i in range(1, k):
                previous_player = current_player
                current_player = next_player[current_player]
            loser = current_player
            current_player = next_player[loser]
            next_player[previous_player] = current_player
            num_removed += 1
        return current_player


    #   runtime: beats 78%
    #    memory: beats 50%
    def findTheWinner_ans_List(self, n: int, k: int) -> int:
        circle = list(range(1, n+1))
        start_index = 0
        while len(circle) > 1:
            removal_index = (start_index + k - 1) % len(circle)
            circle.pop(removal_index)
            start_index = removal_index
        return circle[0]


    #   runtime: beats 29%
    #    memory: beats 50%
    def findTheWinner_ans_Queue(self, n: int, k: int) -> int:
        circle = deque(range(1, n+1))
        while len(circle) > 1:
            for _ in range(k-1):
                circle.append(circle.popleft())
            circle.popleft()
        return circle[0]


    #   runtime: beats 95%
    #    memory: beats 50%
    def findTheWinner_ans_Recursion(self, n: int, k: int) -> int:
        def solve(N, K):
            if N == 1:
                return 0
            return (solve(N-1, K) + K) % N
        return solve(n, k) + 1


    #   runtime: beats 97%
    #    memory: beats 85%
    def findTheWinner_ans_Iterative(self, n: int, k: int) -> int:
        result = 0
        for i in range(2, n+1):
            result = (result + k) % i
        return result + 1


s = Solution()
test_functions = [ s.findTheWinner_Map, s.findTheWinner_ans_List, s.findTheWinner_ans_Queue, s.findTheWinner_ans_Recursion, s.findTheWinner_ans_Iterative, ]

inputs = [ (5,2), (6,5), (3,1), (300,3), (500,5), ]
checks = [ 3, 1, 3, 191, 332, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for (n, k), check in zip(inputs, checks):
        print(f"n=({n}), k=({k})")
        result = f(n, k)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

