
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        return x_str == x_str[::-1]


input_items = [ 121, -121, 10, -101 ]
check_items = [ True, False, False, False ]

s = Solution()

for loop_input, loop_check in zip(input_items, check_items):
    print("loop_input=(%s)" % loop_input)
    loop_result = s.isPalindrome(loop_input)
    print("loop_result=(%s)" % loop_result)
    assert(loop_result == loop_check)

