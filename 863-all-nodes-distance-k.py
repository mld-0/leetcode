import time
import math
from resources.bstreenode import TreeNode
from typing import List, Tuple, Optional, Dict

class Solution:

    #   runtime: beats 98%
    def distanceK_parentPointers(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        result: List[int] = []
        parents: Dict[int,TreeNode] = dict()

        def store_parents(node: Optional[TreeNode]):
            if node is None:
                return
            if node.left is not None:
                parents[id(node.left)] = node
                store_parents(node.left)
            if node.right is not None:
                parents[id(node.right)] = node
                store_parents(node.right)

        def get_target_parent(node: TreeNode) -> Optional[TreeNode]:
            if id(node) in parents:
                return parents[id(node)]
            return None

        def get_depth_k_descendants(node: TreeNode, target: TreeNode, distance: int):
            nonlocal k
            if distance == k:
                result.append(node.val)
            else:
                if node.left is not None and node.left is not target:
                    get_depth_k_descendants(node.left, target, distance + 1)
                if node.right is not None and node.right is not target:
                    get_depth_k_descendants(node.right, target, distance + 1)

        store_parents(root)
        get_depth_k_descendants(target, target, 0)

        previous_parent = target
        parent = get_target_parent(previous_parent)
        i = 1
        while parent is not None:
            get_depth_k_descendants(parent, previous_parent, i)
            previous_parent = parent
            parent = get_target_parent(previous_parent)
            i += 1

        return result


    def distanceK_DFS(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        raise NotImplementedError()


    def distanceK_BFS(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        raise NotImplementedError()



def buildTreeAndGetTarget(values, target_value) -> Tuple[TreeNode, TreeNode]:
    """Create a binary tree from a list of unique values, returning both the root node, and the node that has value matching `target_value`"""
    values_non_null = [ x for x in values if x is not None ]
    assert len(set(values_non_null)) == len(values_non_null), "non-null `values` must be unique"
    assert values[values.index(target_value)] == target_value, "`target_value` must be in `values`"
    values_full = TreeNode.fill_list_infer_missing(values)
    tree_nestedValues = TreeNode._splitListToNestedValuesList(values_full)
    tree_nestedNodes = TreeNode._buildTreeFromNestedValuesList(tree_nestedValues)
    root = tree_nestedNodes[0][0]
    targetparentPointersndex = [ (i, tree_nestedValues[i].index(target_value)) for i in range(len(tree_nestedValues)) if target_value in tree_nestedValues[i] ]
    target = tree_nestedNodes[targetparentPointersndex[0][0]][targetparentPointersndex[0][1]]
    assert root is not None and target is not None
    return (root, target)

s = Solution()
test_functions = [ s.distanceK_parentPointers, ]

inputs = [ ([3,5,1,6,2,0,8,None,None,7,4],5,2), ([1],1,3), ([0,2,1,None,None,3],3,3), ]
checks = [ [7,4,1], [], [2], ]
assert len(inputs) == len(checks)

for f in test_functions:
    print(f.__name__)
    startTime = time.time()
    for (values, target_value, k), check in zip(inputs, checks):
        root, target = buildTreeAndGetTarget(values, target_value)
        print(f"target_value=({target_value}), k=({k})")
        print(f"root:\n{root}")
        result = f(root, target, k)
        print(f"result=({result})")
        assert sorted(result) == sorted(check), "Check comparison failed"
    print("elapsed_ms=(%0.2f)" % ((time.time() - startTime) * 1000000))
    print()

