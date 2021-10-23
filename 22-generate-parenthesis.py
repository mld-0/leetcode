import itertools

class Solution:

    def generateParenthesis(self, n: int) -> list[str]:
        #return self.generateParenthesis_naive(n)
        return self.generateParenthesis_Ans_backtacking(n)


    #   runtime: TLE
    def generateParenthesis_naive(self, n):

        def isValid(s: str) -> bool:
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

        perms = [ ''.join(x) for x in itertools.permutations(["(",")"] * n) ]
        result = set()
        for perm in perms:
            if isValid(perm):
                result.add(perm)
        return list(result)


    #   runtime: beats 90%
    def generateParenthesis_Ans_backtacking(self, n):
        result = []

        def backtrack(combination, l, r):
            if len(combination) == 2*n:
                result.append(''.join(combination))
                return
            if l < n:
                combination.append("(")
                backtrack(combination, l+1, r)
                combination.pop()
            if r < l: 
                combination.append(")")
                backtrack(combination, l, r+1)
                combination.pop()

        backtrack([], 0, 0)
        return result


    #   runtime: beats 51%
    def generateParenthesis_Ans_ClosureNumber(self, N):
        if N == 0: 
            return ['']

        result = []
        for c in range(N):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(N-1-c):
                    result.append('({}){}'.format(left, right))

        return result


s = Solution()
test_functions = [ s.generateParenthesis_naive, s.generateParenthesis_Ans_backtacking, s.generateParenthesis_Ans_ClosureNumber, ]

values_list = [ 3, 1 ]
check_list = [ ["((()))","(()())","(())()","()(())","()()()"], [ "()" ] ]

for test_func in test_functions:
    print(test_func.__name__)
    for value, check in zip(values_list, check_list):
        print("value=(%s)" % value)
        result = test_func(value)
        print("result=(%s)" % str(result))
        assert sorted(result) == sorted(check), "Check failed"
    print()

