from typing import Optional
from resources.bstreenode import TreeNode

#class TreeNode:
#    def __init__(self, val=0, left=None, right=None):
#        self.val = val
#        self.left = left
#        self.right = right

class Solution:

    #   runtime: beats 93%
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p:
            return False
        if not q: 
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


s = Solution()
test_functions = [ s.isSameTree, ]

input_values = [ ([1,2,3], [1,2,3]), ([1,2], [1,None,2]), ([1,2,1], [1,1,2]), ]
result_validate = [ True, False, False, ]
assert len(input_values) == len(result_validate)

for f in test_functions:
    print(f.__name__)
    for (p_list, q_list), check in zip(input_values, result_validate):
        #p_list = TreeNode.fill_list_infer_missing(p_list)
        #q_list = TreeNode.fill_list_infer_missing(q_list)
        print("p_list=(%s), q_list=(%s)" % (p_list, q_list))
        p = TreeNode.from_list(p_list)
        q = TreeNode.from_list(q_list)
        print("p:\n%s" % str(p))
        print("q:\n%s" % str(q))
        result = f(p, q)
        print("result=(%s)" % result)
        assert result== check, "Check comparison failed"
    print()

