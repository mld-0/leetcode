#   {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   {{{2
from __future__ import annotations
from collections import deque
from resources.bstreenode import TreeNode

class Solution:
    def connect(self, root: TreeNode) -> TreeNode:
        """Assign 'next' pointer of each node to the next node on the right on the same level"""
        return self.connect_NestedList(root)
        #return self.connect_AdvancePointer(root)

    #   runtime: beats 35%
    def connect_NestedList(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None

        def max_depth(root: TreeNode) -> int:
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
    def connect_AdvancePointer(self, root: TreeNode) -> TreeNode:
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
    loop_tree = TreeNode.from_list(values)
    print("loop_tree:")
    print(loop_tree)
    result = s.connect(loop_tree) 
    print("result=(%s)" % str(result))
    print()

