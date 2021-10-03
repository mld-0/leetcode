
class Solution:

    def hammingWeight(self, n: int) -> int:
        return self.hammingWeight_ans(n)

    #   runtime: beats 38%
    def hammingWeight_binstring(self, n: int) -> int:
        bin_str = bin(n)[2:]
        count = 0
        for c in bin_str:
            if c == '1':
                count += 1
        return count

    #   runtime: beats 88%
    def hammingWeight_lsb(self, n: int) -> int:
        count = 0
        while n > 0:
            c = n & 1
            if c == 1:
                count += 1
            n = n >> 1
        return count 

    #   runtime: beats 97%
    def hammingWeight_ans(self, n: int) -> int:
        count = 0
        while n > 0:
            count += 1
            #   set rightmost one bit to zero
            n = n & (n - 1)
        return count


s = Solution()

input_values = [0b00000000000000000000000000001011, 0b00000000000000000000000010000000, 0b11111111111111111111111111111101, ]
input_checks = [ 3, 1, 31, ]

for n, check in zip(input_values, input_checks):
    print("n=(%s)" % str(n))
    result = s.hammingWeight(n)
    print("result=(%s)" % str(result))
    assert result == check, "Check failed"
    print()

