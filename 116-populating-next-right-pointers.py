#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
from __future__ import annotations
from collections import deque
#   {{{2

class Node:
    def __init__(self, val: int=0, left: Node=None, right: Node=None, next: Node=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
    def from_list(values: list):
        """Create Binary tree from list containing nodes values in breadth-first order. None represents an empty node. Lists that have non-None children of empty nodes are invalid."""
        #   {{{
        #   number of level in binary tree resulting from 'values'
        if values is None or len(values) == 0:
            return None
        tree_levels_count = 0
        while 2**tree_levels_count <= len(values):
            tree_levels_count += 1
        #   Split 'values' into a list of lists, each inner list corresponding to a level in the tree, eg: [1,3,2,5] becomes [ [1], [3,2], [5,None,None,None] ]
        z = 0
        tree_values = []
        for loop_level in range(tree_levels_count):
            loop_vals = []
            for j in range(2**loop_level):
                if len(values) > z:
                    val = values[z]
                    z += 1
                else:
                    val = None
                loop_vals.append(val)
            tree_values.append(loop_vals)
        print("tree_values=(%s)" % str(tree_values))
        head = Node(tree_values[0][0])
        tree_nodes = [ [ head ] ]
        #   For each level in tree, create and attach children of previous level
        for loop_level in range(1, tree_levels_count):
            loop_nodes = []
            for j, val in enumerate(tree_values[loop_level]):
                parent_node = tree_nodes[loop_level-1][j//2]
                parent_val = tree_values[loop_level-1][j//2]
                if j % 2 == 0:
                    print("(%s).L=(%s)" % (parent_val, val))
                else:
                    print("(%s).R=(%s)" % (parent_val, val))
                #   None indicates missing node
                if val is None:
                    loop_nodes.append(None)
                    continue
                #   Cannot create children for missing node
                if parent_node is None:
                    raise Exception("Invalid list: Unable to create non-null child for null parent\nloop_level=(%s), j=(%s), tree_values=(%s)" % (loop_level, j, tree_values))
                #   Assign node to parent
                if j % 2 == 0:
                    parent_node.left = Node(val)
                    loop_nodes.append(parent_node.left)
                else:
                    parent_node.right= Node(val)
                    loop_nodes.append(parent_node.right)
                tree_nodes.append(loop_nodes)
        return head
        #   }}}
    def to_list_nested(self):
        """Convert tree into nested list, with inner list giving values of each level"""
        #   {{{
        depth = Node.max_depth(self)
        #   nested list of nodes, each inner list corresponding to a level of the tree
        tree_nodes = [ [ None for x in range(2**i) ] for i in range(depth) ]
        #   tree_vals contains values corresponding to tree_nodes
        tree_vals = [ [ None for x in range(2**i) ] for i in range(depth) ]
        tree_nodes[0][0] = self
        tree_vals[0][0] = self.val
        for loop_level in range(1, len(tree_nodes)):
            for j in range(len(tree_nodes[loop_level])):
                parent_node = tree_nodes[loop_level-1][j//2]
                if parent_node is None:
                    tree_nodes[loop_level][j] = None
                    tree_vals[loop_level][j] = None
                    continue
                if j % 2 == 0:
                    tree_nodes[loop_level][j] = parent_node.left
                else:
                    tree_nodes[loop_level][j] = parent_node.right
                if tree_nodes[loop_level][j] is None:
                    tree_vals[loop_level][j] = None
                else:
                    tree_vals[loop_level][j] = tree_nodes[loop_level][j].val
        #print("tree_vals=(%s)" % str(tree_vals))
        return tree_vals
        #   }}}
    def to_list(self):
        """Convert tree into list (such that 'from_list()' will produce an identical tree)"""
        #   {{{
        tree_vals = self.to_list_nested()
        #   result is given by flattening 'tree_vals'
        result = [ val for level in tree_vals for val in level ]
        return result
        #   }}}
    def max_depth(root: Node):
        """Depth of deepest node in tree"""
        #   {{{
        if root is None:
            return 0
        l = Node.max_depth(root.left)
        r = Node.max_depth(root.right)
        return max(l, r) + 1
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
        #   LINK: https://queueoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
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


class Solution:
    def connect(self, root: Node) -> Node:
        """Assign 'next' pointer of each node to the next node on the right on the same level"""
        return self.connect_NestedList(root)
        #return self.connect_AdvancePointer(root)

    #   runtime: beats 35%
    def connect_NestedList(self, root: Node) -> Node:
        if root is None:
            return None

        def max_depth(root: Node) -> int:
            if root is None:
                return 0
            l = max_depth(root.left)
            r = max_depth(root.right)
            return max(l, r) + 1

        #   get depth of tree
        tree_depth = max_depth(root)

        #   create nested list of nodes, each inner list being a level of the tree
        nodes = [ [ None for j in range(2**i) ] for i in range(tree_depth) ]
        nodes[0][0] = root

        queue = deque([root])
        level = 0
        level_position = 0
        while level < tree_depth:
            node = queue.popleft()
            nodes[level][level_position] = node
            level_position += 1
            if node is None:
                queue.append(None)
                queue.append(None)
            else:
                queue.append(node.left)
                queue.append(node.right)
            if level_position == 2**level:
                level += 1
                level_position = 0

        #   For each level in nested list of nodes, assign next pointers
        for l in nodes:
            for i in range(len(l)-1):
                l[i].next = l[i+1]

        return root

    
    #   runtime: beats 99%
    def connect_AdvancePointer(self, root: Node) -> Node:
        if root is None:
            return None

        leftmost = root

        while not leftmost.left is None:
            head = leftmost

            while not head is None:
                #   connection 1 (shared parent)
                head.left.next = head.right

                #   connection 2 (different parent)
                if not head.next is None:
                    head.right.next = head.next.left

                head = head.next

            leftmost = leftmost.left

        return root



s = Solution()

#   Ongoing: 2021-09-22T23:30:37AEST How to check (solution) next pointer? (for multiple cases, against variable(s))
input_values = [ [1,2,3,4,5,6,7], [] ]

for values in input_values:
    print("values=(%s)" % str(values))
    loop_tree = Node.from_list(values)
    print("loop_tree:")
    print(loop_tree)
    result = s.connect(loop_tree) 
    print("result=(%s)" % str(result))
    print()

