#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
from __future__ import annotations
from collections import deque
#   {{{2
#   TODO: 2021-10-15T21:53:07AEDT _leetcode, 117-populating-next-right-pointer-ii, level-traversal (slighly modified from 'tree_to_nested_list()'?), and advance-pointer solutions
#   TODO: 2021-10-16T20:54:37AEDT _leetcode, 117-populating-next-right-pointer-ii, intuition of 'connect_AdvancePointer()', cleanup of solutions (including clarified variable names, 'prev', 'current', 'child' (regarding which level each belongs to)

class Node:
    #   {{{
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
    #   }}}

class Solution:

    def connect(self, root: Node) -> Node:
        return self.connect_AdvancePointer(root)


    #   runtime: beats 93%
    def connect_LevelTraversal(self, root: Node) -> Node:
        """Perform BFS traversal of tree, level by level, assigning the 'next' pointer for each node to the right"""
        if root is None:
            return None

        queue = deque( [root] )
        while len(queue) > 0:
            level_size = len(queue)
            #   for each node on the current level
            for i in range(level_size):
                node = queue.popleft()
                #   don't establish pointers beyond end of level
                if i < level_size - 1:
                    node.next = queue[0]
                #   adding non-None nodes of next level
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

        return root


    #   runtime: beats 93%
    def connect_AdvancePointer(self, root: Node) -> Node:
        """Use the next pointer to traverse each level, assigning the next pointers for the next level in the process"""

        def process_child(child_current, child_previous, leftmost):
            """Update next pointer of 'child_previous' to 'child_current' (if applicable), returning the new 'child_previous' and 'leftmost' nodes"""
            #   'child_current' is missing, no next pointer to update, no need to update 'child_previous'
            if child_current is None:
                return child_previous, leftmost
            #   'child_current' is first node on level, no next pointer to update
            if child_previous is None:
                return child_current, child_current
            #   otherwise update next pointer and return 'child_current' as new previous node
            child_previous.next = child_current
            return child_current, leftmost

        if root is None:
            return None

        leftmost = root

        #   for each level of tree
        while leftmost is not None:
            #   latest node on current level
            current = leftmost

            #   previous node on next level
            child_previous = None
            #   leftmost node of next level
            leftmost = None

            #   for each node 'current' on current level, process l/r children
            while current is not None:
                child_previous, leftmost = process_child(current.left, child_previous, leftmost)
                child_previous, leftmost = process_child(current.right, child_previous, leftmost)
                current = current.next

        return root



    #   runtime: MLE
    def connect_NestedList(self, root: Node) -> Node:
        #   {{{
        """Create nested list from levels of tree, assign the 'next' pointer for each node to the right"""
        if root is None:
            return None

        def get_tree_depth(node: Node) -> int:
            """Get the tree depth from a given root"""
            if node is None:
                return 0
            l = get_tree_depth(node.left)
            r = get_tree_depth(node.right)
            return max(l, r) + 1

        def tree_to_nested_list(root):
            """Create nested list, each inner list containing nodes from level of tree"""
            #   number of levels in tree
            tree_depth = get_tree_depth(root)
            #   create nested list of nodes, inner levels corresponding to levels of tree
            nodes = [ [ None ] * 2**level for level in range(tree_depth) ]
            nodes[0][0] = root
            #   BFS traversal of tree, filling levels nested of nested list
            queue = deque()
            queue.append( root )
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
                    level_position = 0
                    level += 1
            return nodes

        #   get nodes for each level as a nested list
        nodes = tree_to_nested_list(root)

        #   assign next pointer for each non-None node
        for level_nodes in nodes:
            for i in range(len(level_nodes)-1):
                if level_nodes[i] is None:
                    continue
                level_nodes[i].next = None
                for node_next in level_nodes[i+1:]:
                    if node_next is not None:
                        level_nodes[i].next = node_next
                        break

        return root
        #   }}}


s = Solution()

nodes_list = [1,2,3,4,5,None,7]
head = Node.from_list(nodes_list)
print("head:\n%s" % str(head))
result = s.connect(head)
print("result:\n%s" % str(result))
if result.left is not None:
    assert result.left.next == result.right, "Check failed 1.1"
if result.left.left is not None:
    assert result.left.left.next == result.left.right, "Check failed 1.2"
if result.left.right is not None:
    assert result.left.right.next == result.right.right, "Check failed 1.3"
print()

