
class Solution:

    #   runtime: beats 99%
    def addBinary_naive(self, a: str, b: str) -> str:
        a = int(a,2)
        b = int(b,2)
        result = bin(a + b)
        return result[2:]


    #   runtime: beats 74%
    def addBinary_ii(self, a: str, b: str) -> str:
        def bin2int(s: str) -> int:
            result = 0
            for i,x in enumerate(s[::-1]):
                result += int(x) * 2 ** i
            return result
        def int2bin(x: int) -> str:
            if x == 0:
                return "0"
            result = ""
            while x > 0:
                t = int(x % 2)
                x >>= 1
                if t == 0:
                    result += "0"
                else:
                    result += "1"
            return result[::-1]
        a = bin2int(a)
        b = bin2int(b)
        result = int2bin(a + b)
        return result


s = Solution()
test_functions = [ s.addBinary_naive, s.addBinary_ii, ]

test_inputs = [ ("11","1"), ("1010","1011"), ("0","0"), ("10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101", "110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011"), ]
test_validate = [ "100", "10101", "0", "110111101100010011000101110110100000011101000101011001000011011000001100011110011010010011000000000", ]
assert len(test_inputs) == len(test_validate)

for f in test_functions:
    print(f.__name__)
    for (a, b), check in zip(test_inputs, test_validate):
        print("a=(%s), b=(%s)" % (a, b))
        result = f(a, b)
        print("result=(%s)" % result)
        assert result == check, "Check comparison failed"
    print()

