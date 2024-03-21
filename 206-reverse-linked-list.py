#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
from resources.listnode import ListNode
from typing import List, Optional

class Solution:
    """Reverse a linked-list, returning the new head"""

    #   runtime: beats 90%
    def reverseList_List(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        elements = []
        current = head
        while current is not None:
            elements.append(current)
            current = current.next
        for i in range(len(elements)-1, 0, -1):
            elements[i].next = elements[i-1]
        elements[0].next = None
        return elements[-1]


    #   runtime: beats 93%
    def reverseList_TwoPointers(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head
        while current is not None:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        return previous


    #   runtime: beats 99%
    def reverseList_Recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def solve(current, previous):
            if current is None:
                return previous
            temp = current.next
            current.next = previous
            return solve(temp, current)

        return solve(head, None)


s = Solution()
test_functions = [ s.reverseList_List, s.reverseList_TwoPointers, s.reverseList_Recursive, ]

inputs = [ [1,2,3,4,5], [1,2], [], list(range(100)), ]
checks = [ [5,4,3,2,1], [2,1], [], list(reversed(range(100))), ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for vals, check in zip(inputs, checks):
        head = ListNode.from_list(vals)
        print(f"head=({head})")
        result = f(head)
        print(f"result=({result})")
        result = result.to_list() if result is not None else []
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

