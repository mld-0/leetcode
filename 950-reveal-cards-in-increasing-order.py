#   {{{3
       #   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
from collections import deque
from typing import List, Optional

class Solution:
    """Given a list of numbers, return those numbers in an order such that we will remove the numbers in sorted order when we repeat the following steps: 1) remove the next number, 2) move the next number to the end"""

    #   runtime: beats 80%
    #    memory: beats 98%
    def deckRevealedIncreasing_ans_IndicesQueue(self, deck: List[int]) -> List[int]:
        deck = sorted(deck)
        indices = deque(range(len(deck)))
        result = [ None for _ in deck ]
        for card in deck:
            result[indices.popleft()] = card
            if len(indices) > 0:
                indices.append(indices.popleft())
        return result

 
def is_correct(deck: List[int]) -> bool:
    deck = deque(deck)
    result = deque()
    while len(deck) > 0:
        a = deck.popleft()
        b = deck.popleft() if len(deck) > 0 else None
        result.append(a)
        if b is not None:
            deck.append(b)
    return list(result) == sorted(list(result))

s = Solution()
test_functions = [ s.deckRevealedIncreasing, ]

inputs = [ [1,2,3,4,5,6,7], [1,2,3,4,5,6,7,8,9], [17,13,11,2,3,5,7], [1,1000], [1,2,3,4,5,6], [1,2,3,4,5], ]
checks = [ [1,6,2,5,3,7,4], [1,9,2,6,3,8,4,7,5], [2,13,3,11,5,17,7], [1,1000], [1,4,2,6,3,5], [1,5,2,4,3], ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for deck, check in zip(inputs, checks):
        print(f"deck=({deck})")
        result = f(deck)
        print(f"check=({check})")
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

