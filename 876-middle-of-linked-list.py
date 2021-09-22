from __future__ import annotations
from typing import Optional
import math
from resources.listnode import ListNode


class Solution:

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #return self.middleNode_A(head)
        return self.middleNode_C(head)

    #   runtime: beats 5%
    def middleNode_A(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        head_len = 1
        p = head
        while not p.next is None:
            p = p.next
            head_len += 1
        mid_index = math.ceil((head_len-1) / 2)
        p = head
        for i in range(mid_index):
            p = p.next
        return p

    #   runtime: beats 67%
    def middleNode_B(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        head_len = 1
        p = head
        nodes.append(p)
        while not p.next is None:
            p = p.next
            nodes.append(p)
            head_len += 1
        mid_index = math.ceil((head_len-1) / 2)
        return nodes[mid_index]

    #   runtime: beats 99%
    def middleNode_C(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = head
        r = head
        while (not r is None) and (not r.next is None):
            l = l.next
            r = r.next.next
        return l


input_values = [ [1,2,3,4,5], [1,2,3,4,5,6], [0] ]
input_checks = [ [3,4,5], [4,5,6], [0] ]

s = Solution()

for node_list, check in zip(input_values, input_checks):
    node = ListNode.from_list(node_list)
    result = s.middleNode(node)
    print("result=(%s)" % str(result))
    assert( result.to_list() == check )


