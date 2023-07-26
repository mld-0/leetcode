import time
import functools
from resources.bstreenode import TreeNode
from typing import List, Optional

class Solution:

    #   runtime: beats 100%
    @functools.cache
    def allPossibleFBT_ans_DP_TopDown(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        if n == 0:
            return []
        if n == 1:
            return [ TreeNode(0) ]
        if n == 3:
            return [ TreeNode(0, TreeNode(0), TreeNode(0)) ]

        result = []
        for i in range(1, n, 2):
            left = self.allPossibleFBT_ans_DP_TopDown(i)
            right = self.allPossibleFBT_ans_DP_TopDown(n - i - 1)
            for l in left:
                for r in right:
                    result.append( TreeNode(0,l,r) )

        return result


    #   runtime: beats 92%
    def allPossibleFBT_ans_DP_BottomUp(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []

        #   dp[i] = all possible root nodes for tree n=i
        dp = [ [] for _ in range(n+1) ]
        dp[1].append(TreeNode(0))

        for count in range(3, n+1, 2):
            for i in range(1, count-1, 2):
                for l in dp[i]:
                    for r in dp[count - 1 - i]:
                        root = TreeNode(0, l, r)
                        dp[count].append(root)

        return dp[n]



s = Solution()
test_functions = [ s.allPossibleFBT_ans_DP_TopDown, s.allPossibleFBT_ans_DP_BottomUp, ]

inputs = [ 7, 3, 2, ]
checks = [ [[0,0,0,None,None,0,0,None,None,0,0],[0,0,0,None,None,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,None,None,None,None,0,0],[0,0,0,0,0,None,None,0,0]], [[0,0,0]], [], ]
assert len(inputs) == len(checks)

for f in test_functions:
    print(f.__name__)
    startTime = time.time()
    for n, check in zip(inputs, checks):
        print(f"n=({n})")
        result = f(n)
        print("result=(%s)" % [x.to_list() for x in result])
        check = sorted([ TreeNode.fill_list_infer_missing(x) for x in check ], key=lambda x: len(x))
        result_vals = sorted([ x.to_list() for x in result ], key=lambda x: len(x))
        assert check == result_vals, "Check comparison failed"
    print("elapsed_ms=(%0.2f)" % ((time.time() - startTime) * 1_000_000))
    print()

