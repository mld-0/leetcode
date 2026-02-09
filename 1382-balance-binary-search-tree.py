#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
from typing import List, Optional
from resources.bstreenode import TreeNode

class Solution:
    """Generate a balanced BST from the values of an input BST"""

    def balanceBST_i(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        raise NotImplementedError("Finished `is_balanced()` check function, but solution is unstarted")



def check_is_height_balanced(root: Optional[TreeNode]) -> bool:
    """Determine if a given BST is height balanced (Created with ChatGPT5.2) (tests *appear* correct)"""
    def height(n: Optional[TreeNode]) -> int:
        if n is None:
            return 0
        hl = height(n.left)
        if hl == -1:
            return -1
        hr = height(n.right)
        if hr == -1:
            return -1
        if abs(hl - hr) > 1:
            return -1
        return 1 + max(hl, hr)
    return height(root) != -1

def check_is_valid_bst(root: Optional[TreeNode]) -> bool:
    """Check if a given btree is a valid bst (Created with ChatGPT5.2) (tests *appear* correct)"""
    def valid(node: Optional[TreeNode], low, high) -> bool:
        if node is None:
            return True
        if (low is not None and node.val <= low) or (high is not None and node.val >= high):
            return False
        return valid(node.left, low, node.val) and valid(node.right, node.val, high)
    return valid(root, None, None)

#   Test check functions:
#   {{{
def test_check_is_height_balanced():
    inputs = [ [1,None,2,None,3,None,4,None,None], [1], [1,2,3], [1,2,3,4,5], [1,2,3,None,4,None,5], [1,2,None,3], [1, 2, 3, 4, 5, None, None, 8, 9, 10, 11], [], [10,5,None,None,15,6,None], [3,2,None,1], [10,5,15,2,7,11,20], ]
    checks_height_balanced = [ False, True, True, True, True, False, False, True, False, False, True, ]
    assert len(inputs) == len(checks_height_balanced)
    for (vals, check_height_balanced) in zip(inputs, checks_height_balanced):
        node_vals = TreeNode.from_list_infer_missing(vals)
        assert check_is_height_balanced(node_vals) == check_height_balanced, "Test is height balanced Failed"
def test_check_is_valid_bst():
    inputs = [ [1,None,2,None,3,None,4,None,None], [1], [1,2,3], [1,2,3,4,5], [1,2,3,None,4,None,5], [1,2,None,3], [1, 2, 3, 4, 5, None, None, 8, 9, 10, 11], [], [10,5,None,None,15,6,None], [3,2,None,1], [10,5,15,2,7,11,20], ]
    checks_valid_bst = [ True, True, False, False, False, False, False, True, False, True, True, ]
    assert len(inputs) == len(checks_valid_bst)
    for (vals, check_valid_bst) in zip(inputs, checks_valid_bst):
        node_vals = TreeNode.from_list_infer_missing(vals)
        assert check_is_valid_bst(node_vals) == check_valid_bst, "Test is_valid_bst failed"
#   }}}
test_check_is_height_balanced()
test_check_is_valid_bst()

s = Solution()
test_functions = [ s.balanceBST_i, ]

inputs = [ [1,None,2,None,3,None,4,None,None], [2,1,3], ]
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for vals in inputs:
        root = TreeNode.from_list_infer_missing(vals)
        print(f"root:\n{root}")
        result = f(root)
        print(f"result:\n{result}")
        assert (result is None) == (root is None), "xnor None check failed"
        assert check_is_height_balanced(result), "Check heigh failed"
        assert check_is_valid_bst(result), "Check is bst failed"
        if result is not None and root is not None:
            assert set(result.to_list()) == set(root.to_list()), "Sorted list comparison failed"
            assert len(result.to_list()) == len(root.to_list()), "List length comparison failed"
        print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
        print()

