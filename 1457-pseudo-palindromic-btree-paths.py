import time
from collections import Counter, defaultdict
from resources.bstreenode import TreeNode
from typing import List, Optional

class Solution:
    """How many paths from root to each leaf node could be rearranged into a palindrome"""

    #   runtime: beats 75%
    def pseudoPalindromicPaths_CounterDFS(self, root: Optional[TreeNode]) -> int:
        result = 0

        def trace_path(node, path_counter):
            nonlocal result
            if node is None:
                return
            path_counter[node.val] += 1
            if node.left is None and node.right is None:
                if is_pseudo_palindromic(path_counter):
                    result += 1
                return
            trace_path(node.left, path_counter.copy())
            trace_path(node.right, path_counter)

        def is_pseudo_palindromic(path_counter):
            odd_counts = 0
            for n in path_counter.keys():
                if path_counter[n] % 2 != 0:
                    odd_counts += 1
            return odd_counts <= 1

        trace_path(root, defaultdict(int))
        return result


    #   runtime: beats 100%
    def pseudoPalindromicPaths_ans_BitwiseOddCounterDFS(self, root: Optional[TreeNode]) -> int:
        result = 0

        def trace_path(node, path_odd_counter):
            nonlocal result
            if node is None:
                return
            path_odd_counter = path_odd_counter ^ (1 << node.val)
            if node.left is None and node.right is None:
                if is_pseudo_palindromic(path_odd_counter):
                    result += 1
                    return
            trace_path(node.left, path_odd_counter)
            trace_path(node.right, path_odd_counter)

        def is_pseudo_palindromic(path_odd_counter):
            #   is there at most 1 odd count
            return path_odd_counter & (path_odd_counter - 1) == 0
        
        trace_path(root, 0)
        return result


s = Solution()
test_functions = [ s.pseudoPalindromicPaths_CounterDFS, s.pseudoPalindromicPaths_ans_BitwiseOddCounterDFS, ]

inputs = [ [2,3,1,3,1,None,1], [2,1,1,1,3,None,None,None,None,None,1], [9], ]
checks = [ 2, 1, 1, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for vals, check in zip(inputs, checks):
        head = TreeNode.from_list_infer_missing(vals)
        print(f"head:\n{head}")
        result = f(head)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

