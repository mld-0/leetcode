import time
from typing import List, Optional

class Solution:
    """Given a 1-dimensional keyboard, and `word`, determine the time to type the word, where the time to type a letter is |i-j|, where `i` is the index of the previous letter and `j` the index of the current letter"""

    #   runtime: beats 96%
    def calculateTime(self, keyboard: str, word: str) -> int:
        keyboard = { c: i for i, c in enumerate(keyboard) }
        result = 0
        previous = 0
        for c in word:
            current = keyboard[c]
            result += abs(previous-current)
            previous = current
        return result


s = Solution()
test_functions = [ s.calculateTime, ]

inputs = [ ("abcdefghijklmnopqrstuvwxyz", "cba"), ("pqrstuvwxyzabcdefghijklmno", "leetcode"), ]
checks = [ 4, 73, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for (keyboard, word), check in zip(inputs, checks):
        print(f"keyboard=({keyboard}), word=({word})")
        result = f(keyboard, word)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

