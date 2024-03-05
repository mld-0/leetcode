#   {{{3
       #   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
from resources.listnode import ListNode
from typing import List, Optional

class Solution:
    """In a given linked list, nodes occur in pairs, (0,1), (2,3), ect, if the even index node of each pair is greater, even gets a point, and vice versa, return which team wins"""

    #   runtime: beats 97%
    def gameResult_TwoPointer(self, head: Optional[ListNode]) -> str:
        l = head
        r = head.next
        score_even = 0
        score_odd = 0
        while l is not None:
            if l.val > r.val:
                score_even += 1
            elif l.val < r.val:
                score_odd += 1
            l = l.next.next if l.next is not None else None
            r = l.next if l is not None else None
        if score_even > score_odd:
            return "Even"
        elif score_even < score_odd:
            return "Odd"
        else:
            return "Tie"


    #   runtime: beats 99%
    def gameResult_SinglePointer(self, head: Optional[ListNode]) -> str:
        current = head
        net_score = 0
        while current is not None:
            if current.val > current.next.val:
                net_score += 1
            elif current.val < current.next.val:
                net_score -= 1
            current = current.next.next if current.next is not None else None
        if net_score > 0:
            return "Even"
        elif net_score < 0:
            return "Odd"
        else:
            return "Tie"


s = Solution()
test_functions = [ s.gameResult_i, s.gameResult_ii, ]

inputs = [ [2,1], [2,5,4,7,20,5], [4,5,2,1], ]
checks = [ "Even", "Odd", "Tie", ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

inputs = [ ListNode.from_list(x) for x in inputs ]
for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for head, check in zip(inputs, checks):
        print(f"head=({head})")
        result = f(head)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

