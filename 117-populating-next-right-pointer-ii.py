#   {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   {{{2
from __future__ import annotations
from collections import deque
from resources.bstreenode import TreeNode
#   TODO: 2021-10-15T21:53:07AEDT _leetcode, 117-populating-next-right-pointer-ii, level-traversal (slighly modified from 'tree_to_nested_list()'?), and advance-pointer solutions
#   TODO: 2021-10-16T20:54:37AEDT _leetcode, 117-populating-next-right-pointer-ii, intuition of 'connect_AdvancePointer()', cleanup of solutions (including clarified variable names, 'prev', 'current', 'child' (regarding which level each belongs to)

class Node(TreeNode):

    def __init__(self, val: int=0, left: Node=None, right: Node=None, next: Node=None):
        super().__init__(val, left, right)
        self.next = next

    def from_list(values: list):
        def set_next(head):
            if head is None:
                return
            head.next = None
            set_next(head.left)
            set_next(head.right)
        result = TreeNode.from_list(values)
        set_next(result)
        return result


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

