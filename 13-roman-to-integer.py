
class Solution:

    def __init__(self):
        self.roman_map = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
        self.roman_map_substitutions = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'a': 4, 'b': 9, 'c': 40, 'd': 90, 'e': 400, 'f': 900 }

    #   Results:
    #       runtime: beats 27%
    def romanToInt_A(self, s: str) -> int:
        result = 0
        s_reversed = s[::-1]
        for loop_i, loop_char in enumerate(s_reversed):
            loop_val = self.roman_map[loop_char]
            if loop_i == 0 or self.roman_map[s_reversed[loop_i-1]] <= loop_val:
                result += loop_val
            else:
                result -= loop_val
        return result

    #   Results:
    #       runtime: beats 83%
    def romanToInt_Ans(self, s: str) -> int:
        s = s.replace('IV', 'a').replace('IX', 'b').replace('XL', 'c').replace('XC', 'd').replace('CD', 'e').replace('CM', 'f')
        return sum(map(self.roman_map_substitutions.get, s))
        

    def romanToInt(self, s: str) -> int:
        #return self.romanToInt_A(s)
        return self.romanToInt_Ans(s)


s = Solution()

text_list = [ "III", "IV", "IX", "LVIII", "MCMXCIV" ]
check_list = [ 3, 4, 9, 58, 1994 ]

for loop_text, loop_check in zip(text_list, check_list):
    result = s.romanToInt(loop_text)
    print("text=(%s)" % str(loop_text))
    print("result=(%s)" % result)
    assert(result == loop_check)
    print()


