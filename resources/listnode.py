
class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next
    def from_list(values):
        if len(values) == 0:
            return None
        result = ListNode()
        first = result
        second = first
        for v in values:
            first.val = v
            first.next = ListNode()
            second = first
            first = first.next
        second.next = None
        return result
    def to_list(self):
        result = []
        first = self
        while first is not None:
            result.append(first.val)
            first = first.next
        return result
    def __repr__(self):
        return str(self.to_list())


if __name__ == '__main__':
    input_values = [ [1,2,3,4,5], [7,9,4,3], [], [1], ]
    input_checks = input_values[:]

    for value, check in zip(input_values, input_checks):
        loop_node = ListNode.from_list(value)
        print("loop_node=(%s)" % str(loop_node))
        if loop_node is not None:
            loop_list = loop_node.to_list()
            assert( str(loop_node) == str(loop_list) )
        else:
            loop_list = []
        print("loop_list=(%s)" % str(loop_list))
        assert( loop_list == check )
        print()

