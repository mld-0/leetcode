from resources.listnode import ListNode
from typing import Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    #   runtime: beats 96%
    def removeElements_sentinel(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        sentinel = ListNode()
        p = head
        q = sentinel
        while not p is None:
            if p.val != val:
                q.next = p
                q = q.next
            p = p.next
        q.next = None
        return sentinel.next


    #   runtime: beats 71%
    def removeElements_newList(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None
        p = head
        values = []
        while not p is None:
            if p.val != val:
                values.append(p.val)
            p = p.next
        if len(values) == 0:
            return None
        sentinel = ListNode()
        p = sentinel
        for x in values:
            p.next = ListNode(x)
            p = p.next
        return sentinel.next
            

s = Solution()
functions = [ s.removeElements_sentinel, s.removeElements_newList, ]

inputs = [ ([1,2,6,3,4,5,6],6), ([],1), ([7,7,7,7],7), ]
checks = [ [1,2,3,4,5], [], [], ]
assert len(inputs) == len(checks)

for f in functions:
    print(f.__name__)
    for (head_list, val), check_list in zip(inputs, checks):
        print(f"head_list=({head_list}), val=({val})")
        head = ListNode.from_list(head_list)
        result = f(head, val)
        result_list = [] 
        if not result is None:
            result_list = result.to_list()
        print(f"result_list=({result_list})")
        assert result_list == check_list, "Check comparison failed"
    print()

