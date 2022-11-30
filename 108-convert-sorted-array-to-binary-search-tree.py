#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
from resources.bstreenode import TreeNode
from typing import List, Optional
import random

#   Convert sorted array into height-balanced BST
#   Different solutions exist, depending on how middle element is chosen for even-length lists

class Solution:

    def sortedArrayToBST_ans(self, nums: List[int]) -> Optional[TreeNode]:

        def helper(l: int, r: int) -> Optional[TreeNode]:
            if l > r:
                return None
            p = get_mid_index(l, r)
            result = TreeNode(nums[p])
            result.left = helper(l, p-1)
            result.right = helper(p+1, r)
            return result

        return helper(0, len(nums)-1)


    def sortedArrayToBST_ans_ii(self, nums: List[int]) -> Optional[TreeNode]:

        def helper(nums: List[int]) -> Optional[TreeNode]:
            if len(nums) == 0:
                return None
            p = get_mid_index(0, len(nums)-1)
            result = TreeNode(nums[p])
            result.left = helper(nums[:p])
            result.right = helper(nums[p+1:])
            return result

        return helper(nums)


def get_mid_index(l, r) -> int:
    return get_mid_index_ii(l, r)

def get_mid_index_i(l, r) -> int:
    if l == r:
        return l
    result = (l + r) // 2
    if result % 2 != 0 and random.choice([True,False]):
        result += 1
    return result

def get_mid_index_ii(l, r) -> int:
    return (l + r) // 2

def get_mid_index_iii(l, r) -> int:
    result = (l + r) // 2
    if result % 2 != 0:
        result += 1
    return result


s = Solution()
test_functions = [ s.sortedArrayToBST_ans, s.sortedArrayToBST_ans_ii, ]

input_values = [ [-10,-3,0,5,9], [1,3], [], ]
result_validation = [ ([0,-3,9,-10,None,5], [0,-10,5,None,-3,None,9]), ([1,None,3], [3,1]), ([],), ] 
assert len(input_values) == len(result_validation)

for f in test_functions:
    print(f.__name__)
    for nums, check in zip(input_values, result_validation):
        print(f"nums=({nums})")
        result = f(nums)
        print(f"result:\n{result}")
        if result is None:
            result = []
        else:
            result = result.to_list()
        print(f"result=({result})")
        assert any( [ l == result for l in check ] ), "Check comparison failed"
    print()

