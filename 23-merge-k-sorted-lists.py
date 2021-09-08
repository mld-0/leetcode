
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def from_list(l):
        result = ListNode()
        node = result
        previous = node
        for i in l:
            node.val = i
            node.next = ListNode()
            previous = node
            node = node.next
        previous.next = None
        return result

    def to_list(self):
        result = []
        node = self
        while node is not None:
            result.append(node.val)
            node = node.next
        return result

    def __repr__(self):
        return str(self.to_list())


class Solution:

    #  Results:
    #       runtime: beats 94%
    def mergeKLists_bruteforce(self, lists):
        if lists is None:
            return None
        combined = []
        for loop_list in lists:
            node = loop_list
            while node is not None:
                combined.append(node.val)
                node = node.next
        combined = sorted(combined)
        if len(combined) == 0:
            return None
        result = ListNode()
        node = result
        previous = node
        for i in combined:
            node.val = i
            node.next = ListNode()
            previous = node
            node = node.next
        previous.next = None
        return result

    #   TODO: 2021-09-08T17:09:36AEST mergeKLists, comparison, comparison_priorityqueue, divideconquer
    def mergeKLists_comparison(self, lists):
        pass
    def mergeKLists_comparison_priorityqueue(self, lists):
        pass
    def mergeKLists_divideconquer(self, lists):
        pass


    def mergeKLists(self, lists):
        return self.mergeKLists_bruteforce(lists)


s = Solution()

input_lists = [ ([1,4,5],[1,3,4],[2,6]), ([]), ([[]]) ]
check_lists = [ [1,1,2,3,4,4,5,6], [], [] ]

for loop_input, loop_check in zip(input_lists, check_lists):
    print("loop_input=(%s)" % str(loop_input))
    loop_input_linked = []
    for loop_list in loop_input:
        print("loop_list=(%s)" % str(loop_list))
        loop_list_linked = ListNode.from_list(loop_list)
        print("loop_list_linked=(%s)" % str(loop_list_linked))
        loop_input_linked.append(loop_list_linked)
    print("loop_check=(%s)" % str(loop_check))
    result  = s.mergeKLists(loop_input_linked)
    print("result=(%s)" % str(result))


