import time
from resources.listnode import ListNode
from typing import Optional

class Solution:

    #   runtime: beats 52%
    def partition_naive(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        l = []
        r = []
        current = head
        while current is not None:
            if current.val < x:
                l.append(current)
            else:
                r.append(current)
            current = current.next
        lr = [ *l, *r, ]
        head = lr[0]
        for i in range(len(lr)-1):
            lr[i].next = lr[i+1]
        lr[-1].next = None
        return head


    #   runtime: beats 69%
    def partition_twoPointers(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        before_sentinel = ListNode()
        after_sentinel = ListNode()
        current = head
        before = before_sentinel
        after = after_sentinel
        while current is not None:
            if current.val < x:
                before.next = current
                before = before.next
            else:
                after.next = current
                after = after.next
            current = current.next
        before.next = after_sentinel.next
        after.next = None
        return before_sentinel.next


s = Solution()
test_functions = [ s.partition_naive, s.partition_twoPointers, ]

inputs = [ ([1,4,3,2,5,2],3),  ([2,1],2), ([],0), ([1,4,3,0,5,2],2), ]
checks = [ [1,2,2,4,3,5], [1,2], [], [1,0,4,3,5,2], ]
assert len(inputs) == len(checks)

for f in test_functions:
    print(f.__name__)
    startTime = time.time()
    for (head_list, x), check in zip(inputs, checks):
        head = ListNode.from_list(head_list)
        print(f"head=({head}), x=({x})")
        result = f(head, x)
        print(f"result=({result})")
        print(f"check=({check})")
        assert result == ListNode.from_list(check), "Check comparison failed"
    print("elapsed_ms=(%0.2f)" % ((time.time() - startTime) * 1000000))
    print()


