
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

