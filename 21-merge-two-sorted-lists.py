
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def from_list(l):
        if len(l) == 0:
            return None
        L = ListNode(l[0])
        result = L
        for i in range(1, len(l)):
            L.next = ListNode(l[i])
            L = L.next
        return result

    def to_list(self):
        result = []
        node = self
        while node is not None:
            result.append(node.val)
            node = node.next
        return result
    
    def __repr__(self):
        result = str(self.to_list())
        return result

class Solution:

    #   Result:
    #       runtime: 92%
    def mergeTwoLists(self, l1, l2):
        if l1 is None and l2 is None:
            return None
        node = ListNode()
        result = node
        previous = node
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                node.val = l1.val
                l1 = l1.next
            else:
                node.val = l2.val
                l2 = l2.next
            node.next = ListNode()
            previous = node
            node = node.next
        while l1 is not None:
            node.val = l1.val
            l1 = l1.next
            node.next = ListNode()
            previous = node
            node = node.next
        while l2 is not None:
            node.val = l2.val
            l2 = l2.next
            node.next = ListNode()
            previous = node
            node = node.next

        previous.next = None

        return result


s = Solution()

input_lists = [ ([1,2,4], [1,3,4]), ([], []), ([], [0]) ]
check_lists = [ [1,1,2,3,4,4], [], [0] ]

for (l1, l2), check in zip(input_lists, check_lists):
    L1 = ListNode.from_list(l1)
    L2 = ListNode.from_list(l2)

    print("L1=(%s)" % L1)
    print("L2=(%s)" % L2)

    result = s.mergeTwoLists(L1, L2)

    print("result=(%s)" % str(result))
    if result is not None:
        assert( result.to_list() == check )

