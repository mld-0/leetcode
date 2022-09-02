from typing import Optional
from resources.listnode import ListNode

class Solution:

    #   runtime: beats 90%
    def deleteDuplicates_i(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        previous = None
        current = head
        while current is not None:
            if current.val in seen:
                previous.next = current.next
            else:
                seen.add(current.val)
                previous = current
            current = current.next
        return head


s = Solution()
test_functions = [ s.deleteDuplicates_i, ]

input_values = [ [1,1,2], [1,1,2,3,3], [1,1,1], ]
result_expected = [ [1,2], [1,2,3], [1], ]
assert len(input_values) == len(result_expected)

for f in test_functions:
    print(f.__name__)
    for values, expected in zip(input_values, result_expected):
        print("values=(%s)" % values)
        values_llist = ListNode.from_list(values)
        result_llist = f(values_llist)
        result = result_llist.to_list()
        print("result=(%s)" % result)
        assert result == expected, "Expected comparison failed"
    print()


