from typing import List, Any, Optional

class ListNode:

    def __init__(self, val: Any=0, _next: Optional['ListNode']=None):
        self.val = val
        self.next = _next

    @staticmethod
    def from_list(values: List[Any]) -> Optional['ListNode']:
        if not values:
            return None
        sentinel = ListNode()
        current = sentinel
        for v in values:
            current.next = ListNode(v)
            current = current.next
        return sentinel.next

    def to_list(self) -> List[Any]:
        result = []
        current: Optional['ListNode'] = self
        while current is not None:
            result.append(current.val)
            current = current.next
        return result

    def __eq__(self, rhs):
        if not isinstance(rhs, ListNode):
            return False
        if self.val != rhs.val:
            return False
        return self.next == rhs.next

    def __repr__(self):
        return '->'.join( [ str(x) for x in self.to_list() ] )


def test():
    input_values = [ [1,2,3,4,5], [7,9,4,3], [], [1], ]
    input_checks = input_values[:]
    for value, check in zip(input_values, input_checks):
        loop_node = ListNode.from_list(value)
        print(loop_node)
        if loop_node is not None:
            loop_list = loop_node.to_list()
        else:
            loop_list = []
        assert loop_list == check 
        assert loop_node == ListNode.from_list(check)
        assert loop_node != ListNode.from_list([53,9])

if __name__ == '__main__':
    test()

