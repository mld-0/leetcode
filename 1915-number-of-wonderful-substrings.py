#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
from collections import defaultdict, Counter
from typing import List, Optional

class Solution:
    """Determine the number of continuous substrings in the input where no more than 1 letter occurs an odd number of times"""

    #   runtime: TLE
    def wonderfulSubstrings_naive(self, word: str) -> int:
        def is_wonderful(subword: str) -> bool:
            odd_occurences = 0
            counts = Counter(subword)
            for letter, count in counts.items():
                if count % 2 != 0:
                    odd_occurences += 1
                if odd_occurences > 1:
                    return False
            return True
        results = []
        for i in range(len(word)):
            for j in range(i, len(word)):
                subword = word[i:j+1]
                if is_wonderful(subword):
                    results.append(subword)
        nontrival_results = [ x for x in results if len(x) > 1 ]
        print(f"nontrival_results=({nontrival_results})")
        return len(results)


    #   runtime: TLE
    def wonderfulSubstrings_i(self, word: str) -> int:

        #   prefix_odd_bitmasks[i]: bitwise representation of whether `word[:i+1]` contains each letter an odd number of times
        prefix_odd_bitmasks = [ 0 for _ in range(len(word)) ]
        previous = 0
        for i in range(0, len(word)):
            char = word[i]
            _next = previous ^ (1 << (ord(char) - 97))
            previous = _next
            prefix_odd_bitmasks[i] = _next
        #print(f"({[bin(x) for x in prefix_odd_bitmasks]})")

        result = len(word)
        #nontrival_results = []
        for r in range(1, len(prefix_odd_bitmasks)):
            if (prefix_odd_bitmasks[r] & (prefix_odd_bitmasks[r] - 1)) == 0:    # 1 bit set
                result += 1
                #nontrival_results.append( [0, r] )
        for l in range(0, len(prefix_odd_bitmasks)):
            for r in range(l+2, len(prefix_odd_bitmasks)):
                temp = prefix_odd_bitmasks[l] ^ prefix_odd_bitmasks[r]
                if (temp & (temp - 1)) == 0:    #   1 or 0 bits differ
                    result += 1
                    #nontrival_results.append( [l+1, r] )
        #print(nontrival_results)
        return result


    #   runtime: beats 29%
    #    memory: beats 22%
    def wonderfulSubstrings_ans_i(self, word: str) -> int:
        freq = defaultdict(int)
        freq[0] = 1
        mask = 0
        result = 0
        for c in word:
            mask ^= (1 << (ord(c) - 97))
            if mask in freq:
                result += freq[mask]
            freq[mask] += 1
            for odd_c in range(0, 10):
                if (mask ^ (1 << odd_c)) in freq:
                    result += freq[mask ^ (1 << odd_c)]
        return result


    #   runtime: beats 45%
    #    memory: beats 80%
    def wonderfulSubstrings_ans_ii(self, word):
        count = [1] + [0] * 1024
        res = cur = 0
        for c in word:
            cur ^= 1 << (ord(c) - ord('a'))
            res += count[cur]
            res += sum(count[cur ^ (1 << i)] for i in range(10))
            count[cur] += 1
        return res


s = Solution()
test_functions = [ s.wonderfulSubstrings_i, s.wonderfulSubstrings_ans_i, s.wonderfulSubstrings_ans_ii, ]

#   {{{
inputs = ["aahfjhbbadacibdaicdicbhgijijhgjafjbeddhgbaddbgifibfdgdbdcccgjadieigagecacdabcjfjjbfjiabeiiihhdhcfjgjjjhgcbdicehifjajeaffjhbgcheibcedahbhgjhghhcbdcddegdijbcdfajhbfaajaijcfejidijcbbecfeijiagcejhbfbifaghffjeecjahiaghageggfiifejfeigibijdihfbifaihejcigifhhejifhfagdahjfaiafhebdedfeabacgjadbbfghiejjchijefcbdchdggcighggjjgacbbcdddcebhdaejijcejhdcagjgiggggdfeefchbacegbfgahbcbecgcjdffagjafcjidhbghaafbggaicfjcbdjhefacgddjjcebigbefjcefjgijcfbjhcijdgijaeefdgdfgcijdjchgfjaghdfbecbggfbifefebhchgccebfhbbhdhjdihicjfdgddhbidghjbbdafefejbhfghfcjdicfefaefbaejgeadjjjhdigfadfdiajhiaicehehdjbbeicdgffgehgicbidbifefigaieigfeibhgbcaeghfehechehbhjdbhaagcgcfcecefdhaedjdhaigdfefeadadicagebcegeahcdhijhjdcgcdhihcajfaaggcdejigjbafabichedcdgcjccjdihbaffiddbbafdfdagafgdhheaehjdhhfjcfjdgghjcehfcdgaghbfgfaccjbabbjbhhcjfaddjgafjcebdbbcahjbiefabahchadgjfgdddcejedecfahidfbiebbjdadegibfecdjbhcbccjehffhcdgcebihdbadahbaecfhadiicjfjhaeaebcgiaijhbjdggbdebbfgbhceffbeegiefjcceefifidfiegjhefcjicahcddcjidjfhfceidhabgfjjcdbagiajciih"]
checks = [6950]
#   }}}
inputs = [ "aabb", "aba", "he", "abab", "ccjjc", "abcaab", ]
checks = [ 9, 4, 2, 7, 13, 10, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for word, check in zip(inputs, checks):
        print(f"word=({word})")
        result = f(word)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

