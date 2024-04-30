
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


#   From: 1915-number-of-wonderful-strings:
#   Check whether two numbers differ by 0, 1, or more bits 
#   (xor them and check if the result is a power of two)
#       temp = a ^ b
#       if a == b:
#           print("differ by 0 bits")
#       elif (a & (a - 1)) == 0: 
#           print("differ by 1 bit")
#       else: 
#           print("differ by >1 bits")



#   From: 201-bitwise-and-number-range
#   
#   isolate the leftmost one bit of n:
#       1 << int(math.log2(n))
#
#   [{a better way (surely)?}]
