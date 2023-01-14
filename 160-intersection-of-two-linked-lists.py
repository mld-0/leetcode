from typing import Optional
from resources.listnode import ListNode

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    #   runtime: beats 98%
    def getIntersectionNode_Set(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        set_A = set()
        A = headA
        while not A is None:
            set_A.add(A)
            A = A.next
        B = headB
        while not B is None:
            if B in set_A:
                return B
            B = B.next
        return None


    #   runtime: beats 97%
    def getIntersectionNode_TwoPointers(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def linked_list_len(head):
            result = 0
            p = head
            while not p is None:
                p = p.next
                result += 1
            return result
        #   Get the length of both lists
        lenA = linked_list_len(headA)
        lenB = linked_list_len(headB)
        #   Set headA to be the longer list
        if lenB > lenA:
            headA, headB = headB, headA
            lenA, lenB = lenB, lenA
        #   Advance 'A' so that the same number of elements remain as in 'B'
        A = headA
        B = headB
        for _ in range(lenA-lenB):
            A = A.next
        #   Find intersection
        while not A is None:
            if A is B:
                return B
            A = A.next
            B = B.next
        return None


    #   runtime: beats 98%
    def getIntersectionNode_Ans(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA = headA
        pB = headB
        while pA != pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next
        return pA


def make_intersect(intersectVal, listA, listB, skipA, skipB):
    headA = ListNode.from_list(listA)
    headB = ListNode.from_list(listB)
    if intersectVal == 0:
        return (headA, headB)
    if skipA == 0:
        return (headA, headA)
    if skipB == 0:
        return (headB, headB)
    A = headA
    for i in range(skipA-1):
        A = A.next
    B = headB
    for _ in range(skipB-1):
        B = B.next
    assert A.next.val == intersectVal
    assert B.next.val == intersectVal
    assert A.next.to_list() == B.next.to_list()
    B.next = A.next
    return (headA, headB)


s = Solution()
functions = [ s.getIntersectionNode_Set, s.getIntersectionNode_TwoPointers, s.getIntersectionNode_Ans, ]

inputs = [ (8, [4,1,8,4,5], [5,6,1,8,4,5], 2, 3), (2, [1,9,1,2,4], [3,2,4], 3, 1), (0, [2,6,4], [1,5], 3, 2), (1, [1], [1], 0, 0), ]
checks = [ [8,4,5], [2,4], None, [1], ]
assert len(inputs) == len(checks)

for f in functions:
    print(f.__name__)
    for (intersectVal, listA, listB, skipA, skipB), check in zip(inputs, checks):
        print(f"intersectVal=({intersectVal}), listA=({listA}), listB=({listB}), skipA=({skipA}), skipB=({skipB})")
        headA, headB = make_intersect(intersectVal, listA, listB, skipA, skipB)
        print(f"headA=({headA}), headB=({headB})")
        result = f(headA, headB)
        print(f"result=({result})")
        result_list = None if result is None else result.to_list()
        assert result_list == check, "Check comparison failed"
    print()

