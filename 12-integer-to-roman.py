
class Solution:

    def __init__(self):
        self.int_to_roman_substitutions = { 1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M' }

    def largest_next_value(self, num, int_roman_map):
        keys = int_roman_map.keys()
        for k in sorted(keys, reverse=True):
            if num >= k:
                return k        

    #   Results:
    #       runtime: beats 15%
    def intToRoman_A(self, num: int) -> str:
        result = ""
        while (num > 0):
            loop_val = self.largest_next_value(num, self.int_to_roman_substitutions)
            loop_roman = self.int_to_roman_substitutions[loop_val]
            result = result + loop_roman
            num -= loop_val
        return result


    def intToRoman(self, num: int) -> str:
        return self.intToRoman_A(num)

values_list = [ 3, 4, 9, 58, 1994 ]
check_list = [ 'III', 'IV', 'IX', 'LVIII', 'MCMXCIV' ]

s = Solution()

for value, check in zip(values_list, check_list):
    result = s.intToRoman(value)
    print("value=(%s), result=(%s)" % (value, result))
    print("check=(%s)" % check)
    assert(result == check)

