import sys
import time
import logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

class Solution:

    #   Ongoing: 2021-09-15T16:46:59AEST _leetcode, reverseOnlyLetters, 'Ans' is significantly faster than 'A' when run locally, but submission considers A (slightly) faster? (and what is an actually fast answer (according to submission)) <- (upon further investigation) this is entirely due to calls to logging.debug()
    def reverseOnlyLetters(self, s: str) -> str:
        return self.reverseOnlyLetters_A(s)
        #return self.reverseOnlyLetters_Ans(s)

    #   Result:
    #       runtime: beats 14%
    def reverseOnlyLetters_A(self, s: str) -> str:
        non_letters = dict()
        letters = []
        for i, c in enumerate(s):
            if not c.isalpha():
                non_letters[i] = c
            else:
                letters.append(c)
        letters = letters[::-1]
        result = ""
        i = 0
        #logging.debug("non_letters=(%s)" % str(non_letters))
        #logging.debug("letters=(%s)" % str(letters))
        for c in letters:
            while i in non_letters.keys():
                result += non_letters[i]
                i += 1
            result += c
            i += 1
        while i < len(s):
            result += non_letters[i]
            i += 1
        return result

    #   Result:
    #       runtime: beats 10%
    def reverseOnlyLetters_Ans(self, s: str) -> str:
        l = 0
        r = len(s) - 1
        result = list(s)
        while l < r:
            if not result[l].isalpha():
                l += 1
            elif not result[r].isalpha():
                r -= 1
            else:
                result[l], result[r] = result[r], result[l]
                l += 1
                r -= 1
        return ''.join(result)


s = Solution()

test_inputs = [ "-", "ab-cd", "a-bC-dEf-ghIj", "Test1ng-Leet=code-Q!", "cba", "dac-", "z<*zj" ]
test_checks = [ "-", "dc-ba", "j-Ih-gfE-dCba", "Qedo1ct-eeLg=ntse-T!", "abc", "cad-", "j<*zz" ]

start = time.time()
for loop_input, loop_check in zip(test_inputs, test_checks):
    result = s.reverseOnlyLetters(loop_input)
    print("result=(%s)" % str(result))
    assert( result == loop_check )

end = time.time()
elapsed = (end - start)*1000000
print("elapsed=(%s)" % str(elapsed))
