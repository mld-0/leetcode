import sys
import logging
from typing import Optional
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next
    def from_list(values):
        if len(values) == 0:
            return None
        result = ListNode()
        first = result
        second = first
        for v in values:
            first.val = v
            first.next = ListNode()
            second = first
            first = first.next
        second.next = None
        return result
    def to_list(self):
        result = []
        first = self
        while first is not None:
            result.append(first.val)
            first = first.next
        return result
    def __repr__(self):
        return str(self.to_list())

class Solution:

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #return self.removeNthFromEnd_Ans(head, n)
        return self.removeNthFromEnd_A(head, n)


    def removeNthFromStart(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 0:
            head = head.next
            return head
        first = head
        second = first
        i = 0
        while i < n:
            second = first
            first = first.next
            i += 1
        if first is not None:
            second.next = first.next
        else:
            second.next = None
        return head


    #       runtime: beats 55%
    def removeNthFromEnd_A(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_len = 1
        first = head

        while first.next is not None:
            first = first.next
            list_len += 1

        index_remove = list_len - n

        return self.removeNthFromStart(head, index_remove)


    #       runtime: beats 80%
    def removeNthFromEnd_Ans(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        second = head

        while n > 0:
            first = first.next
            n -= 1

        if first is None:
            return head.next

        while first.next:
            first = first.next
            second = second.next

        second.next = second.next.next
        return head


    #   runtime: beats 98%
    def removeNthFromEnd_TwoPointers(self, head: ListNode, n: int) -> ListNode:
        l = head
        r = head

        for i in range(n):
            r = r.next

        if r is None:
            return head.next

        while r.next is not None:
            r = r.next
            l = l.next

        l.next = l.next.next
        return head


list_values = [ ([1,2,3,4,5], 2), ([1], 1), ([1,2], 1) ]
list_checks = [ [1,2,3,5], [], [1] ]

s = Solution()

for (loop_values, loop_n), loop_check in zip(list_values, list_checks):
    loop_node = ListNode.from_list(loop_values)
    result = s.removeNthFromEnd(loop_node, loop_n)
    print("result=(%s)" % str(result))
    result_list = []
    if result is not None: 
        result_list = result.to_list()
    assert( result_list == loop_check)

