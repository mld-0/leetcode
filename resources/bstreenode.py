#   {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   {{{2

#   Required for own-class type hints (alternatively use class name as string)
from __future__ import annotations  

from typing import List, Optional, Any
import sys
import logging

#   Continue: 2022-09-17T14:39:33AEST test_fillListInferMissing, tested with simple input (simple 2-level tree) only (need an example of a bigger tree with omitted empty branches) [...] (does leetcode give such an input?) [...] 2024-01-11T20:26:25AEDT added extra test case from 1026-max-diff-between-node-and-ancestor for which it was incorrect and debuged function, (message and warning remain since more test cases are probably warrented still (for this and other methods))

#   Ongoing: 2024-01-12T18:36:45AEDT `fill_list_infer_missing()` doesn't work for inputs where each empty node is denoted by a 'None' -> ergo it can't be used for any input?

class TreeNode:

    def __init__(self, val: Any=0, left: Optional[TreeNode]=None, right: Optional[TreeNode]=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def from_list(values: List[Any]) -> Optional[TreeNode]:
        """Create Binary tree from list containing nodes values in breadth-first order. None represents an empty node. Lists that have non-None children of None parents are invalid (use `from_list_infer_missing() for such lists)."""
        #   number of level in binary tree resulting from 'values'
        if not values:
            return None
        tree_nestedValues = TreeNode._splitListToNestedValuesList(values)
        tree_nestedNodes = TreeNode._buildTreeFromNestedValuesList(tree_nestedValues)
        head = tree_nestedNodes[0][0]
        return head

    @staticmethod
    def from_list_infer_missing(values: List[Any]) -> Optional[TreeNode]:
        """Create Binary tree (as per `from_list()`), with missing elements filled in by `fill_list_infer_missing()`"""
        values = TreeNode.fill_list_infer_missing(values)
        return TreeNode.from_list(values)

    def to_list_nested(self) -> List[List[Any]]:
        """Convert tree into nested list, with inner list containing values from each level"""
        tree_nestedNodes = self._tree_toNestedNodesList()
        f = lambda x: None if not x else x.val
        tree_nestedValues = [ [ f(n) for n in x ] for x in tree_nestedNodes ]
        logging.debug("tree_nestedValues=(%s)" % str(tree_nestedValues))
        return tree_nestedValues

    def to_list(self) -> List[Any]:
        """Convert tree into list (such that 'from_list()' will produce an identical tree)"""
        tree_nestedValues = self.to_list_nested()
        #   flatten 'tree_nestedValues'
        result = [ val for level in tree_nestedValues for val in level ]
        if not TreeNode.is_length_of_complete_binary_tree(len(result)):
            raise Exception(f"TreeNode.to_list(): len(result)=({len(result)}) invalid for result=({result}) (plz debug)")
        return result

    @staticmethod
    def fill_list_infer_missing(values: List[Any]) -> List[Any]:
        """Convert tree-as-list as given for leetcode input to format acceptable for 'from_list()' (by filling in missing None children of None parents)"""
        #   {{{
        if len(values) == 0:
            return []
        values = list(values)
        if values[0] is None:
            raise Exception(f"TreeNode.fill_list_infer_missing(): First element in values=({values}) may not be None")
        result: List[List[Any]] = [ [ values[0] ] ]
        z = 1
        loop_level = 1
        while z < len(values):
            loop_nodes = []
            parent_level = result[loop_level-1]
            previous_z = z
            for x in parent_level:
                if x is not None:
                    if z < len(values):
                        loop_nodes.append(values[z])
                    else:
                        loop_nodes.append(None)
                    z += 1
                    if z < len(values):
                        loop_nodes.append(values[z])
                    else:
                        loop_nodes.append(None)
                    z += 1
                else:
                    loop_nodes.append(None)
                    loop_nodes.append(None)
                    if TreeNode.is_length_of_complete_binary_tree(len(values)) and z+1 < len(values) and values[z] is None and values[z+1] is None:
                        #   Ongoing: 2024-01-12T19:37:01AEDT this skipping of twin None values in the event the input is the exact length of a binary-tree seems like asking for trouble for that edgecase where we are given a tree with lots of implicit missing values that just happens to be the exact size of a full binary tree - although ... presumedly it would only ever actually be a problem if the input is inconsistent about including/excluding None values for missing nodes? 
                        z += 2
            if z == previous_z:
                raise Exception(f"TreeNode.fill_list_infer_missing(): z not incremented (parent_level=({parent_level}) must be all None) for values=({values}) (invalid input?) (or, plz debug?)")
            result.append(loop_nodes)
            loop_level += 1
        logging.debug(f"result=({result})")
        result_flat = [ val for level in result for val in level ]
        logging.debug("result_flat=(%s)" % result_flat)
        if not TreeNode.is_length_of_complete_binary_tree(len(result_flat)):
            raise Exception(f"TreeNode.fill_list_infer_missing(): len(result_flat)=({len(result_flat)}) invalid for result_flat=({result_flat}), values=({values}) (plz debug)")
        return result_flat
        #   }}}

    @staticmethod
    def max_depth(root: Optional[TreeNode]) -> int:
        """Depth of deepest node in tree"""
        if root is None:
            return 0
        l = TreeNode.max_depth(root.left)
        r = TreeNode.max_depth(root.right)
        return max(l, r) + 1

    @staticmethod
    def _splitListToNestedValuesList(values: List[Any]) -> List[List[Any]]:
        """Split 'values' into a list of lists, each inner list corresponding to a level in the tree, eg: [1,3,2,5] becomes [ [1], [3,2], [5,None,None,None] ]. Lists that have non-None children of None parent nodes are invalid."""
        #   {{{
        tree_levels_count = TreeNode._listLevelsCountWhenNested(values)
        z = 0
        tree_nestedValues = []
        for loop_level in range(tree_levels_count):
            loop_vals = []
            for j in range(2**loop_level):
                if len(values) > z:
                    val = values[z]
                    z += 1
                else:
                    val = None
                loop_vals.append(val)
            if not TreeNode.is_power_of_two(len(loop_vals)):
                raise Exception(f"TreeNode._splitListToNestedValuesList(): invalid len(loop_vals)=({len(loop_vals)}) for loop_vals=({loop_vals}), values=({values}) (plz debug)")
            tree_nestedValues.append(loop_vals)
        logging.debug("tree_nestedValues=(%s)" % str(tree_nestedValues))
        assert len(tree_nestedValues) == tree_levels_count
        return tree_nestedValues
        #   }}}

    @staticmethod
    def _listLevelsCountWhenNested(values: List[Any]) -> int:
        """For a given flat list, how many levels of nested list / tree are necessary to represent it"""
        tree_levels_count = 0
        while 2**tree_levels_count <= len(values):
            tree_levels_count += 1
        return tree_levels_count

    @staticmethod
    def _buildTreeFromNestedValuesList(tree_nestedValues: List[List[Optional[TreeNode]]]) -> List[List[Optional[TreeNode]]]:
        """Create tree from given nested list of values, returning nested list of the nodes of that tree"""
        #   {{{
        head = TreeNode(tree_nestedValues[0][0])
        tree_nestedNodes: List[List[Optional[TreeNode]]] = [ [ head ] ]
        #   For each level in tree, create and attach children of previous level
        for loop_level in range(1, len(tree_nestedValues)):
            loop_nodes: List[Optional[TreeNode]] = []
            for j, val in enumerate(tree_nestedValues[loop_level]):
                parent_node = tree_nestedNodes[loop_level-1][j//2]
                parent_val = tree_nestedValues[loop_level-1][j//2]
                #   None indicates missing node
                if val is None:
                    loop_nodes.append(None)
                    continue
                #   Cannot create children for missing node
                if parent_node is None:
                    raise Exception("TreeNode._buildTreeFromNestedValuesList(): Invalid list: Unable to create non-null child for null parent\nloop_level=(%s), j=(%s), tree_nestedValues=(%s)" % (loop_level, j, tree_nestedValues))
                #   Assign node to parent
                if j % 2 == 0:
                    logging.debug("(%s).L=(%s)" % (parent_val, val))
                    parent_node.left = TreeNode(val)
                    loop_nodes.append(parent_node.left)
                else:
                    logging.debug("(%s).R=(%s)" % (parent_val, val))
                    parent_node.right= TreeNode(val)
                    loop_nodes.append(parent_node.right)
            if not TreeNode.is_power_of_two(len(loop_nodes)):
                raise Exception(f"TreeNode._buildTreeFromNestedValuesList(): invalid len(loop_nodes)=({len(loop_nodes)}) for tree_nestedValues=({tree_nestedValues}) (plz debug)")
            tree_nestedNodes.append(loop_nodes)
        return tree_nestedNodes
        #   }}}

    def _tree_toNestedNodesList(self) -> List[List[Optional[TreeNode]]]:
        """Get the nodes of the tree as a nested list"""
        #   {{{
        depth = TreeNode.max_depth(self)
        #   nested list of nodes, each inner list corresponding to a level of the tree
        tree_nestedNodes: List[List[Optional[TreeNode]]] = [ [ None for x in range(2**i) ] for i in range(depth) ]
        tree_nestedNodes[0][0] = self
        for loop_level in range(1, len(tree_nestedNodes)):
            for j in range(len(tree_nestedNodes[loop_level])):
                parent_node = tree_nestedNodes[loop_level-1][j//2]
                if parent_node is None:
                    tree_nestedNodes[loop_level][j] = None
                    continue
                if j % 2 == 0:
                    tree_nestedNodes[loop_level][j] = parent_node.left
                else:
                    tree_nestedNodes[loop_level][j] = parent_node.right
        return tree_nestedNodes
        #   }}}

    def __repr__(self):
        """Text representation of tree as multi-line string"""
        #   {{{
        result = ""
        lines, *_ = self._repr_helper()
        for line in lines:
            result += line + "\n"
        return result[:-1]
        #   }}}

    def _repr_helper(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        #   {{{
        #   LINK: https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.val
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle
        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._repr_helper()
            s = '%s' % self.val
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._repr_helper()
            s = '%s' % self.val
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
        # Two children.
        left, n, p, x = self.left._repr_helper()
        right, m, q, y = self.right._repr_helper()
        s = '%s' % self.val
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
        #   }}}

    @staticmethod
    def is_length_of_complete_binary_tree(n):
        """Check if n is 1 less than a power of 2 (correct length of a complete binary tree as a list)"""
        return n > 0 and (n + 1) & n == 0

    @staticmethod
    def is_power_of_two(n):
        """Check if n is a power of 2 (correct length for a complete level of a binary tree)"""
        return n > 0 and (n & (n - 1)) == 0

    def __eq__(self, lhs):
        if not isinstance(lhs, TreeNode):
            return False
        if self.val != lhs.val:
            return False
        if self.left != lhs.left:
            return False
        if self.right != lhs.right:
            return False
        return True


def test_fromList_toList():
    #   {{{
    print("test_fromList_toList:")
    input_values = [ 
        [1,3,2,5], 
        [2,1,3,None,4,None,7], 
        [1], 
        [1,2], 
        [], 
        list(range(1,16)), 
        [1,2,3,4,None,None,7,8,9,None,None,None,None,14,15], 
    ]
    for values in input_values:
        loop_tree = TreeNode.from_list(values)
        print(loop_tree)
        if loop_tree is not None:
            loop_list = loop_tree.to_list()
            print("loop_list=(%s)" % str(loop_list))
            assert [ values[i] == loop_list[i] for i in range(len(values)) ] 
        else:
            assert values == [] 
    print()
    #   }}}

def test_fillListInferMissing():
    #   {{{
    print("test_fillListInferMissing:")
    logging.warning("test_fillListInferMissing test values insufficent - need more complex example of btree-as-list to call this tested")
    input_values = [ 
        [1], 
        [], 
        [1,2], 
        [1,None,2,3], 
        [1,None,2], 
        [1,2,2,None,3,None,3], 
        [5,4,1,None,1,None,4,2,None,2,None], 
        [1,None,2,None,0,3], 
        [1,None,2,None,None,None,0,None,None,None,None,None,None,3,None], 


        [1,3,2,5], 
        [2,1,3,None,4,None,7], 
        [1], 
        [1,2], 
        [], 
        list(range(1,16)), 
        [1,2,3,4,None,None,7,8,9,None,None,None,None,14,15], 
    ]
    result_validate = [ 
        [1], 
        [], 
        [1,2,None], 
        [1,None,2,None,None,3,None], 
        [1,None,2], 
        [1,2,2,None,3,None,3], 
        [5,4,1,None,1,None,4,None,None,2,None,None,None,2,None], 
        [1,None,2,None,None,None,0,None,None,None,None,None,None,3,None], 
        [1,None,2,None,None,None,0,None,None,None,None,None,None,3,None], 

        [1,3,2,5], 
        [2,1,3,None,4,None,7], 
        [1], 
        [1,2], 
        [], 
        list(range(1,16)), 
        [1,2,3,4,None,None,7,8,9,None,None,None,None,14,15], 
    ]

    assert len(input_values) == len(result_validate)
    for values, check in zip(input_values, result_validate):
        print("values=(%s)" % values)
        result = TreeNode.fill_list_infer_missing(values)
        print("result=(%s)" % result)
        while len(check) < len(result): #   extend `check` with `None` to account for trailing `None`s
            check.append(None)
        assert result == check, "Check comparison failed"
        if values == check:
            logging.debug("note: values == check (no modification was required)")
        print(TreeNode.from_list(result))
    print()
    #   }}}

def test_eq():
    #   {{{
    input_values = [ 
        [1,3,2,5], 
        [2,1,3,None,4,None,7], 
        [1], 
        [1,2], 
        [], 
        list(range(1,16)), 
        [1,2,3,4,None,None,7,8,9,None,None,None,None,14,15], 
    ]
    for i in range(len(input_values)):
        for j in range(len(input_values)):
            l = TreeNode.from_list(input_values[i])
            r = TreeNode.from_list(input_values[j])
            if i == j:
                assert l == r
            else:
                assert l != r
    #   }}}

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, stream=sys.stderr)
    test_fromList_toList()
    test_fillListInferMissing()
    test_eq()

