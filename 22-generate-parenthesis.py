import itertools

class Solution:

    def isValid(self, s: str) -> bool:
        """Determine if a given sequence of brackets '()' is valid, i.e: there is a closing for every opening, and no closing without a preceding opening"""
        if len(s) % 2 != 0:
            return False
        pairs_stack = []
        for i, c in enumerate(s):
            if c == "(":
                pairs_stack.append("(")
            if c == ")":
                if len(pairs_stack) != 0 and pairs_stack[-1] == "(":
                    pairs_stack.pop()
                else:
                    return False
        return len(pairs_stack) == 0

    def generateParenthesis(self, n: int) -> list[str]:
        #return self.generateParenthesis_naive(n)
        return self.generateParenthesis_Ans_backtacking(n)

    #   Result: 
    #       runtime: limit exceded
    def generateParenthesis_naive(self, n):
        perms = [ ''.join(x) for x in itertools.permutations(["(",")"] * n) ]
        result = set()
        for perm in perms:
            if self.isValid(perm):
                result.add(perm)
        return list(result)

    #   Results:
    #       runtime: beats 86%
    def generateParenthesis_Ans_backtacking(self, n):
        result = []
        def backtrack(S=None, l=0, r=0):
            if S is None:
                S = []
            if len(S) == 2*n:
                result.append(''.join(S))
                return True
            if l < n:
                S.append("(")
                backtrack(S, l+1, r)
                S.pop()
            if r < l: 
                S.append(")")
                backtrack(S, l, r+1)
                S.pop()
        backtrack()
        return result

s = Solution()

values_list = [ 3, 1 ]
check_list = [ ["((()))","(()())","(())()","()(())","()()()"], [ "()" ] ]

for value, check in zip(values_list, check_list):
    result = s.generateParenthesis(value)
    print("result=(%s)" % str(result))
    assert result == check, "Check failed"
    print()



        


