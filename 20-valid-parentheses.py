
class Solution:

    #   Results:
    #       runtime: beats 86%
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        pairs_stack = []
        for i, c in enumerate(s):
            if c == "(":
                pairs_stack.append("(")
            if c == "[":
                pairs_stack.append("[")
            if c == "{":
                pairs_stack.append("{")
            if c == ")":
                if len(pairs_stack) != 0 and pairs_stack[-1] == "(":
                    pairs_stack.pop()
                else:
                    return False
            if c == "]":
                if len(pairs_stack) != 0 and pairs_stack[-1] == "[":
                    pairs_stack.pop()
                else:
                    return False
            if c == "}":
                if len(pairs_stack) != 0 and pairs_stack[-1] == "{":
                    pairs_stack.pop()
                else:
                    return False
        return len(pairs_stack) == 0



s = Solution()

input_list = [ "()", "()[]{}", "(]", "([)]", "{[]}", "){" ]
check_list = [ True, True, False, False, True, False ]

for str_input, str_check in zip(input_list, check_list):
    print("str_input=(%s)" % str_input)
    result = s.isValid(str_input)
    print("result=(%s)" % result)
    print("str_check=(%s)" % str_check)
    assert( result == str_check )

