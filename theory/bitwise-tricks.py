
#   XOR:
#       a ^ b = (a & ~b) | (~a & b)
#       0 ^ 0 = 0
#       0 ^ 1 = 1
#       1 ^ 0 = 1
#       1 ^ 1 = 0


#   Two's Compliment: How negative numbers are usually represented
#   To make a positive number negative, or a negative number positive, invert the bits and add one
#       -1 * n = (n ^ INT_MAX) + 1
#   
#   Two's compliment has the very useful property of allowing subtraction to be performed with the same circitry as addition, since a - b = a + (-b), where -b is the two's compliment of b.


#   From: 231-power-of-two:
#
#   isolates the rightmost one bit of n:
#       (n & (-n))      
#
#   sets rightmost one bit of n to zero:
#       (n & (n-1))     
#
#   A positive number if a power of two if either:
#       (n & (-n))  == n
#       (n & (n-1)) == 0

