import itertools

class Solution:

    def backspaceCompare(self, s: str, t: str) -> bool:
        """Check if 's' and 't' are equal when '#' denotes a backspace"""
        return self.backspaceCompare_ReverseCounterYield(s, t)


    #   runtime: beats 96%
    def backspaceCompare_Stack(self, s: str, t: str) -> bool:
        def evaluateStr(s):
            result = []
            for c in s:
                if c == '#':
                    if len(result) > 0:
                        result.pop()
                else:
                    result.append(c)
            return ''.join(result)
        return evaluateStr(s) == evaluateStr(t)


    #   runtime: beats 71%
    def backspaceCompare_ReverseCounterIter(self, s: str, t: str) -> bool:
        def evaluateStr(s):
            result = ""
            skip = 0
            for x in reversed(s):
                if x == '#':
                    skip += 1
                elif skip > 0:
                    skip -= 1
                else:
                    result += x
            return result[::-1]
        return evaluateStr(s) == evaluateStr(t)

    
    #   runtime: beats 89%
    def backspaceCompare_ReverseCounterYield(self, s: str, t: str) -> bool:
        def evaluateStr(s):
            skip = 0
            for x in reversed(s):
                if x == '#':
                    skip += 1
                elif skip > 0:
                    skip -= 1
                else:
                    yield x
        return all( x == y for x, y in itertools.zip_longest(evaluateStr(s), evaluateStr(t)) )

        

s = Solution()

input_values = [ ("ab#c", "ad#c"), ("ab##", "c#d#"), ("a##c", "#a#c"), ("a#c", "b"), ]
input_checks = [ True, True, True, False, ]

for (val, t), check in zip(input_values, input_checks):
    print("val=(%s), t=(%s)" % (val, t))
    result = s.backspaceCompare(val, t)
    print("result=(%s)" % result)
    assert result == check, "Check failed"
    print()

