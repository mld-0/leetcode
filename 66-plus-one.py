from typing import List

class Solution:

    #   runtime: beats 98%
    def plusOne_naive(self, digits: List[int]) -> List[int]:
        digits = [ str(x) for x in digits ]
        digits = ''.join(digits)
        digits = int(digits)
        result = [ int(x) for x in str(digits+1) ]
        return result


    #   runtime: beats 85%
    def plusOne_carrying(self, digits: List[int]) -> List[int]:
        result = [ x for x in digits ]
        if digits[-1] != 9:
            result[-1] += 1
            return result

        nines_start = len(result) - 1
        while nines_start > 0 and digits[nines_start-1] == 9:
            nines_start -= 1

        if nines_start == 0:
            result.insert(0, 1)
            for i in range(1, len(result)):
                result[i] = 0
        else:
            result[nines_start-1] += 1
            for i in range(nines_start, len(result)):
                result[i] = 0

        return result


    #   runtime: beats 72%
    def plusOne_customFunctions(self, digits: List[int]) -> List[int]:

        def atoi(s: str) -> int:
            result = 0
            for i, x in enumerate(s):
                result += (ord(x) - ord('0')) * 10 ** (len(s)-i-1)
            return result

        def itoa(x: int) -> str:
            import math
            if x == 0:
                return "0"
            if x < 10:
                return chr(x+ord('0'))
            result = []
            while x > 0:
                order = math.floor(math.log10(x))
                msd = int(x / (10**order))
                result.append(chr(msd+ord('0')))
                x = int(x - msd * 10**order)
                if x == 0:
                    new_order = 0
                else:
                    new_order = math.floor(math.log10(x))
                while order > new_order+1:
                    result.append('0')
                    order -= 1
            while order > new_order:
                result.append('0')
                order -= 1
            result = join(result, '')
            return result

        def join(l: List[str], delim: str):
            result = ""
            for x in l:
                result += x
                result += delim
            if len(delim) > 0:
                result = result[:0-len(delim)]
            return result

        digits = [ itoa(x) for x in digits ]
        digits = join(digits, '')
        digits = atoi(digits)
        result = [ atoi(x) for x in itoa(digits+1) ]
        return result


    #   runtime: beats 95%
    def plusOne_customFunctions_ii(self, digits: List[int]) -> List[int]:

        def atoi(s: str) -> int:
            result = 0
            for i, x in enumerate(s):
                result += (ord(x) - ord('0')) * 10 ** (len(s)-i-1)
            return result

        def itoa(x: int) -> str:
            import math
            if x == 0:
                return "0"
            if x < 10:
                return chr(x+ord('0'))
            result = []
            while x > 0:
                temp = x % 10
                result.append(chr(temp+ord('0')))
                x = x // 10
            result = result[::-1]
            result = join(result, '')
            return result

        def join(l: List[str], delim: str):
            result = ""
            for x in l:
                result += x
                result += delim
            if len(delim) > 0:
                result = result[:0-len(delim)]
            return result

        digits = [ itoa(x) for x in digits ]
        digits = join(digits, '')
        digits = atoi(digits)
        result = [ atoi(x) for x in itoa(digits+1) ]
        return result



s = Solution()
test_functions = [ s.plusOne_naive, s.plusOne_carrying, s.plusOne_customFunctions, s.plusOne_customFunctions_ii, ]

input_values = [ [1,2,3], [4,3,2,1], [9], [7,2,8,5,0,9,1,2,9,5,3,6,6,7,3,2,8,4,3,7,9,5,7,7,4,7,4,9,4,7,0,1,1,1,7,4,0,0,6], ]
input_checks = [ [1,2,4], [4,3,2,2], [1,0], [7,2,8,5,0,9,1,2,9,5,3,6,6,7,3,2,8,4,3,7,9,5,7,7,4,7,4,9,4,7,0,1,1,1,7,4,0,0,7], ]
assert len(input_values) == len(input_checks)

for f in test_functions:
    print(f.__name__)
    for digits, check in zip(input_values, input_checks):
        print("digits=(%s)" % digits)
        result = f(digits)
        print("result=(%s)" % result)
        assert check == result, "Check failed"
    print()

