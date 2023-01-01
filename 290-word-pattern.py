
class Solution:

    #   runtime: beats 98%
    def wordPattern(self, pattern: str, s: str) -> bool:
        letters = [ c for c in pattern ]
        words = s.split()
        if len(letters) != len(words):
            return False
        letters_to_words = dict()
        for letter, word in zip(letters, words):
            if letter in letters_to_words.keys():
                if not letters_to_words[letter] == word:
                    return False
            else:
                if word in letters_to_words.values():
                    return False
                letters_to_words[letter] = word
        return True
        

s = Solution()
test_functions = [ s.wordPattern, ]

inputs = [ ("abba", "dog cat cat dog"), ("abba", "dog cat cat fish"), ("aaaa", "dog cat cat dog"), ("abba", "dog dog dog dog"), ("aaa", "aa aa aa aa"), ]
checks = [ True, False, False, False, False, ]
assert len(inputs) == len(checks)

for f in test_functions:
    print(f.__name__)
    for (pattern, s), check in zip(inputs, checks):
        print(f"pattern=({pattern}), s=({s})")
        result = f(pattern, s)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print()

