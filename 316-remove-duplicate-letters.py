import time
from collections import defaultdict, Counter
from typing import List, Optional

class Solution:
    """Remove letters from `s` until each character remains only once, in the smallest alphabetically-sorted order possible"""

    #   runtime: beats 5%
    def removeDuplicateLetters_GreedySetAndDict(self, s: str) -> str:

        letters = set(s)
        result_indicies = []
        result_letters = []
        used_letters = set()

        available = dict()
        for i, c in enumerate(s):
            available[i] = set([ c for c in s[i:] ])

        while len(result_indicies) < len(letters):
            trial_index = None
            remaining_letters = set(letters - used_letters)
            start_index = 0 if len(result_indicies) == 0 else result_indicies[-1]
            for i in range(start_index, len(s)):
                if (trial_index is None or s[i] < s[trial_index]) and available[i] >= remaining_letters and s[i] in remaining_letters:
                    trial_index = i

            used_letters.add(s[trial_index])
            result_indicies.append(trial_index)
            result_letters.append(s[trial_index])

        return ''.join(result_letters)


    #   runtime: beats 92%
    def removeDuplicateLetters_ans_GreedyStack(self, s: str) -> str:
        result = []
        used_letters = set()
        last_occurence = { c: i for i, c in enumerate(s) }

        for i, c in enumerate(s):
            if c not in used_letters:
                while len(result) > 0 and c < result[-1] and i < last_occurence[result[-1]]:
                    remove_letter = result.pop()
                    used_letters.discard(remove_letter)
                result.append(c)
                used_letters.add(c)

        return ''.join(result)



    #   runtime: beats 8%
    def removeDuplicateLetters_ans_GreedyCounter(self, s: str) -> str:
        counts = Counter(s)
        index = 0

        for i, c in enumerate(s):
            if c < s[index]:
                index = i
            counts[c] -= 1
            if counts[c] == 0:
                break

        if len(s) == 0:
            return ''

        new_s = s[index:].replace(s[index], "")
        return s[index] + self.removeDuplicateLetters_ans_GreedyCounter(new_s)


s = Solution()
test_functions = [ s.removeDuplicateLetters_GreedySetAndDict, s.removeDuplicateLetters_ans_GreedyStack, s.removeDuplicateLetters_ans_GreedyCounter, ]

inputs = [ "bcabc", "cbacdcbc", ]
checks = [ "abc", "acdb", ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for s, check in zip(inputs, checks):
        print(f"s=({s})")
        result = f(s)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()


