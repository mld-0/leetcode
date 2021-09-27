from resources.listnode import ListNode


class Solution:

    def reverseList(self, head):
        #return self.reverseList_A(head)
        #return self.reverseList_Inplace(head)
        #return self.reverseList_Recursive(head)
        return self.reverseList_RecursiveInplace(head)

    #       runtime: beats 39%
    def reverseList_Iterative(self, head):
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

    
    #       runtime: beats 97%
    def reverseList_Inplace(self, head):
        curr = head
        prev = None
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    
    #   runtime: beats 90%
    def reverseList_Recursive(self, head, r=None):
        if head is None:
            return r
        if r is None:
            r = ListNode(head.val)
            return self.reverseList_Recursive(head.next, r)
        r = ListNode(head.val, r)
        return self.reverseList_Recursive(head.next, r)


    #   runtime: beats 97%
    def reverseList_RecursiveInplace(self, head):
        if head is None or head.next is None:
            return head
        p = self.reverseList_RecursiveInplace(head.next)
        head.next.next = head
        head.next = None
        return p

        


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
    result_list = []
    if result is not None:
        result_list = result.to_list()
    assert result_list == loop_check 
    print()



