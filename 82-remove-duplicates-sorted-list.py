from typing import List, Optional
from resources.listnode import ListNode
from collections import Counter

#class ListNode:
#   def __init__(self, val=0, _next=None):
#       self.val = val
#       self.next = _next

class Solution:
    
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Remove duplicate values from sorted linked list"""
        #return self.deleteDuplicates_useList(head)
        return self.deleteDuplicates_twoPointers(head)

    #   runtime: beats 98%
    def deleteDuplicates_useList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        p = head
        while p is not None:
            values.append(p.val)
            p = p.next
        values_count = Counter(values)
        result_list = []
        for v in values:
            if values_count[v] == 1:
                result_list.append(v)
        if len(result_list) == 0:
            return None
        result = ListNode(result_list[0], None)
        p = result
        for v in result_list[1:]:
            p.next = ListNode(v, None)
            p = p.next
        return result

    def deleteDuplicates_twoPointers(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #   Pseudo-Node 'sentinal' inserted before beginning of list, allowing first element to be easily removed if needed
        sentinal = ListNode(0, head)

        #   'l' points to previous node 
        l = sentinal

        #   'r' is advanced to skip duplicates
        r = head

        while r is not None:
            #   Is 'r' a duplicate 
            if r.next is not None and r.val == r.next.val:
                #   If 'r' is a duplicate, advance past duplicates and remove them from list
                while r.next is not None and r.val == r.next.val:
                    r = r.next
                l.next = r.next
            else:
                #   Otherwise advance 'l'
                l = l.next
            r = r.next

        head = sentinal.next
        return head



s = Solution()

input_values = [ [1,2,3,3,4,4,5], [1,1,1,2,3], ]
input_checks = [ [1,2,5], [2,3], ]

for head_list, check in zip(input_values, input_checks):
    print("head_list=(%s)" % str(head_list))
    head = ListNode.from_list(head_list)
    result = s.deleteDuplicates(head)
    print("result=(%s)" % str(result))
    result_list = []
    if result is not None:
        result_list = result.to_list()
    print("result_list=(%s)" % result_list)
    assert result_list == check, "Check failed"
    print()
