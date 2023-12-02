import time
from collections import Counter, defaultdict
from typing import List, Optional

class Solution:

    #   runtime: beats 21%
    def countCharacters_i(self, words: List[str], chars: str) -> int:
        words_counts = [ Counter(w) for w in words ]
        chars_count = Counter(chars)
        result = 0
        for i, word_counts in enumerate(words_counts):
            word_check = True
            for c in word_counts.keys():
                if c not in chars_count.keys():
                    word_check = False
                    continue
                if word_counts[c] > chars_count[c]:
                    word_check = False
                    continue
            if word_check == True:
                result += len(words[i])
        return result


    #   runtime: beats 22%
    def countCharacters_ii(self, words: List[str], chars: str) -> int:
        words_counts = [ Counter(w) for w in words ]
        chars_count = Counter(chars)
        chars_set = set(chars_count.keys())
        result = 0
        for i, word_counts in enumerate(words_counts):
            word_check = True
            if set(word_counts.keys()) > chars_set:
                word_check = False
                continue
            for c in word_counts.keys():
                if word_counts[c] > chars_count[c]:
                    word_check = False
                    continue
            if word_check == True:
                result += len(words[i])
        return result


    #   runtime: beats 95%
    def countCharacters_ans(self, words: List[str], chars: str) -> int:

        def canForm(word, counts):
            c = [0] * 26
            for ch in word:
                x = ord(ch) - ord('a')
                c[x] += 1
                if c[x] > counts[x]:
                    return False
            return True

        counts = [0] * 26
        for ch in chars:
            counts[ord(ch) - ord('a')] += 1
        result = 0
        for word in words:
            if canForm(word, counts):
                result += len(word)
        return result


s = Solution()
test_functions = [ s.countCharacters_i, s.countCharacters_ii, s.countCharacters_ans, ]

inputs = [ (["cat","bt","hat","tree"],"atach"),  (["hello","world","leetcode"],"welldonehoneyr"), ]
checks = [ 6, 10, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for (words, chars), check in zip(inputs, checks):
        print(f"words=({words}), chars=({chars})")
        result = f(words, chars)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()


