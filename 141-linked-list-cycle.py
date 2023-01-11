from resources.listnode import ListNode
from typing import Optional

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    #   runtime: beats 96%
    def hasCycle_Set(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        seen = set()
        n = head
        while not n.next is None:
            if n in seen:
                return True
            seen.add(n)
            n = n.next
        return False


    #   runtime: beats 97%
    def hasCycle_TwoPointers(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow = head
        fast = head.next
        while True:
            try:
                slow = slow.next
                fast = fast.next.next
            except AttributeError as e:
                return False
            if slow == fast:
                return True


def make_cycle(head, pos_cycle):
    """Link last node in LinkedList 'head' to 'pos_end'-th node"""
    if head is None:
        raise Exception("head is None")
    if pos_cycle < -1:
        raise Exception(f"pos_cycle=({pos_cycle}) < -1")
    if pos_cycle == -1:
        return
    node_end = head
    while not node_end.next is None:
        node_end = node_end.next
    node_cycle = head
    for i in range(pos_cycle):
        if node_cycle is None:
            raise Exception(f"pos_cycle=({pos_cycle}) is beyond end")
        node_cycle = node_cycle.next
    if node_cycle is None:
        raise Exception(f"pos_cycle=({pos_cycle}) is beyond end")
    node_end.next = node_cycle


s = Solution()
functions = [ s.hasCycle_Set, s.hasCycle_TwoPointers, ]

inputs = [ ([3,2,0,-4],1),  ([1,2],0), ([1],-1), (None,-1), ]
checks = [ True, True, False, False, ]
assert len(inputs) == len(checks)

for f in functions:
    print(f.__name__)
    for (head, pos), check in zip(inputs, checks):
        print(f"head=({head}), pos=({pos})")
        if not head is None:
            head_node = ListNode.from_list(head)
            make_cycle(head_node, pos)
        else:
            head_node = None
        result = f(head_node)
        x = head_node
        assert result == check, "Check comparison failed"
    print()

