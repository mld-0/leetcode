import time
from collections import Counter
from typing import List, Optional

class Solution:

    #   runtime: beats 93%
    def makeEqual(self, words: List[str]) -> bool:
        all_words = ''.join(words)
        letters_counts = Counter(all_words)
        return all( [ count % len(words) == 0 for letter, count in letters_counts.items() ] )


s = Solution()
test_functions = [ s.makeEqual, ]

inputs = [ ["abc","aabc","bc"], ["ab","a"], ]
checks = [ True, False, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for words, check in zip(inputs, checks):
        print(f"words=({words})")
        result = f(words)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

