#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
#   Requires 'from __future__ import annotations' ... ((for 'TreeNode' type hints) alternatively use class name as string?)
from __future__ import annotations
from typing import List, Optional
import sys
import pprint
import logging
#   {{{2
#   Ongoing: 2022-09-09T22:47:12AEST 94-binary-tree-inorder-traversal features input list '[1,None,2,3]' which we needed to convert to '[1,None,2,None,None,3]' to be able to create the tree the problem describes - is this format with implied empty branches used in other problems (necessitating a converter between them?)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def from_list(values: List) -> TreeNode:
        """Create Binary tree from list containing nodes values in breadth-first order. None represents an empty node. Lists that have non-None children of empty nodes are invalid."""
        #   number of level in binary tree resulting from 'values'
        if not values:
            return None
        tree_nestedValues = TreeNode._splitListToNestedValuesList(values)
        tree_nestedNodes = TreeNode._buildTreeFromNestedValuesList(tree_nestedValues)
        head = tree_nestedNodes[0][0]
        return head

    def to_list_nested(self) -> List[List]:
        """Convert tree into nested list, with inner list containing values from each level"""
        tree_nestedNodes = self._toNestedNodesList()
        f = lambda x: None if not x else x.val
        tree_nestedValues = [ [ f(n) for n in x ] for x in tree_nestedNodes ]
        logging.debug("tree_nestedValues=(%s)" % str(tree_nestedValues))
        return tree_nestedValues

    def to_list(self) -> List:
        """Convert tree into list (such that 'from_list()' will produce an identical tree)"""
        tree_nestedValues = self.to_list_nested()
        #   result is given by flattening 'tree_nestedValues'
        result = [ val for level in tree_nestedValues for val in level ]
        return result

    def max_depth(root: TreeNode) -> int:
        """Depth of deepest node in tree"""
        if root is None:
            return 0
        l = TreeNode.max_depth(root.left)
        r = TreeNode.max_depth(root.right)
        return max(l, r) + 1

    def _splitListToNestedValuesList(values: List) -> List[List]:
        #   {{{
        tree_levels_count = 0
        while 2**tree_levels_count <= len(values):
            tree_levels_count += 1
        #   Split 'values' into a list of lists, each inner list corresponding to a level in the tree, eg: [1,3,2,5] becomes [ [1], [3,2], [5,None,None,None] ]
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
            tree_nestedValues.append(loop_vals)
        logging.debug("tree_nestedValues=(%s)" % str(tree_nestedValues))
        assert len(tree_nestedValues) == tree_levels_count
        return tree_nestedValues
        #   }}}

    def _buildTreeFromNestedValuesList(tree_nestedValues: List[List]) -> List[List[TreeNode]]:
        #   {{{
        head = TreeNode(tree_nestedValues[0][0])
        tree_nestedNodes = [ [ head ] ]
        #   For each level in tree, create and attach children of previous level
        for loop_level in range(1, len(tree_nestedValues)):
            loop_nodes = []
            for j, val in enumerate(tree_nestedValues[loop_level]):
                parent_node = tree_nestedNodes[loop_level-1][j//2]
                parent_val = tree_nestedValues[loop_level-1][j//2]
                #   None indicates missing node
                if val is None:
                    loop_nodes.append(None)
                    continue
                #   Cannot create children for missing node
                if parent_node is None:
                    raise Exception("Invalid list: Unable to create non-null child for null parent\nloop_level=(%s), j=(%s), tree_nestedValues=(%s)" % (loop_level, j, tree_nestedValues))
                #   Assign node to parent
                if j % 2 == 0:
                    logging.debug("(%s).L=(%s)" % (parent_val, val))
                    parent_node.left = TreeNode(val)
                    loop_nodes.append(parent_node.left)
                else:
                    logging.debug("(%s).R=(%s)" % (parent_val, val))
                    parent_node.right= TreeNode(val)
                    loop_nodes.append(parent_node.right)
            tree_nestedNodes.append(loop_nodes)
        return tree_nestedNodes
        #   }}}

    def _toNestedNodesList(self) -> List[List[Optional[TreeNode]]]:
        #   {{{
        depth = TreeNode.max_depth(self)
        #   nested list of nodes, each inner list corresponding to a level of the tree
        tree_nestedNodes = [ [ None for x in range(2**i) ] for i in range(depth) ]
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
        lines, *_ = self._display_aux()
        for line in lines:
            result += line + "\n"
        return result[:-1]
        #   }}}

    def _display_aux(self):
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
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
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

    def fill_list_infer_missing(values: List) -> List:
        """Convert tree-as-list as given for leetcode input to format acceptable for 'from_list()' (by filling in missing None children of None parents)"""
        raise NotImplementedError()



def test_fromList_toList():
    #   {{{
    input_values = [ [1,3,2,5], [2,1,3,None,4,None,7], [1], [1,2], [], list(range(1,16)), [1,2,3,4,None,None,7,8,9,None,None,None,None,14,15], ]
    for values in input_values:
        loop_tree = TreeNode.from_list(values)
        print(loop_tree)
        if loop_tree is not None:
            loop_list = loop_tree.to_list()
            print("loop_list=(%s)" % str(loop_list))
            assert( [ values[i] == loop_list[i] for i in range(len(values)) ] )
            print()
        else:
            assert( values == [] )
    #   }}}

def test_fillListInferMissing():
    input_values = [ [1], [], [1,2], [1,None,2,3], ]
    result_validate = [ [1], [], [1,2,None], [1,None,2,None,None,3,None], ]
    assert len(input_values) == len(result_validate)
    for values, check in zip(input_values, result_validate):
        print("values=(%s)" % values)
        result = TreeNode.fill_list_infer_missing(values)
        print("result=(%s)" % result)
        assert result == check, "Check comparison failed"



if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, stream=sys.stderr)
    test_fromList_toList()
    #test_fillListInferMissing()

