
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.to_list())

    def to_list(self):
        result = []
        node = self
        while node is not None:
            result.append(node.val)
            node = node.next
        return result

    def from_list(l):
        if l is None or len(l) == 0:
            return None
        result = ListNode()
        node = result
        previous = node
        for i in l:
            node.val = i
            previous = node
            node.next = ListNode()
            node = node.next
        previous.next = None
        return result


class Solution:

    #   Results:
    #       runtime: beats 39%
    def reverseList_A(self, head):
        if head is None:
            return None
        elements = []
        node = head
        while node is not None:
            elements.append(node.val)
            node = node.next
        elements = elements[::-1]
        result = ListNode()
        node = result
        previous = node
        for i in elements:
            node.val = i
            node.next = ListNode()
            previous = node
            node = node.next
        previous.next = None
        return result

    
    #   Results:
    #       runtime: beats 69%
    def reverseList_Ans(self, head):
        curr = head
        prev = None
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def reverseList(self, head):
        #return self.reverseList_A(head)
        return self.reverseList_Ans(head)


s = Solution()

input_list = [ [1,2,3,4,5], [1,2], [] ]
check_list = [ [5,4,3,2,1], [2,1], [] ]

for loop_input, loop_check in zip(input_list, check_list):
    print("loop_input=(%s)" % loop_input)
    loop_input_linked = ListNode.from_list(loop_input)
    print("loop_input_linked=(%s)" % loop_input_linked)
    result = s.reverseList(loop_input_linked)
    print("result=(%s)" % result)
    print("loop_check=(%s)" % loop_check)
    if result is not None:
        assert( result.to_list() == loop_check )



