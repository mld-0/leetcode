#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
from resources.listnode import ListNode
from typing import List, Optional
#   arg_printer(args: List, arg_names: List), list2str(vals: List, max_str_length: int=60) {{{
def arg_printer(args: List, arg_names: List):  
    assert len(args) == len(arg_names), "input args / arg_names length mismatch"
    output = ""
    for arg, arg_name in zip(args, arg_names):
        output += f"{arg_name}=({list2str(arg)}), "
    print(output[:-2])
def list2str(vals: List, max_str_length: int=60):  
    def build_string(vals, num_elements):
        if num_elements < len(vals):
            return f"[{','.join(map(str, vals[:num_elements]))},...,{vals[-1]}]"
        else:
            return str(vals)
    if type(vals) != type([]):
        return str(vals)
    if len(vals) == 0:
        return str(vals)
    num_elements = len(vals)
    if num_elements > 100:
        return f"len([...])=({num_elements})"
    while num_elements > 0:
        formatted_list = build_string(vals, num_elements)
        if len(formatted_list) <= max_str_length:
            break
        num_elements -= 1
    return formatted_list
#   }}}

class Solution:
    """Remove the n-th node from the end of a linked list and return its head"""

    #   runtime: beats 98%
    def removeNthFromEnd_TwoPass(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_length = 0
        current = head
        while current is not None:
            current = current.next
            list_length += 1

        #   position of node to be removed (0-indexed)
        index_remove = list_length - n

        if index_remove == 0:
            return head.next
        previous = None
        current = head
        for i in range(index_remove):
            previous = current
            current = current.next
        previous.next = current.next
        return head


    #   runtime: beats 99%
    def removeNthFromEnd_TwoPointers(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None

        l = head
        r = head
        for i in range(n+1):
            if r is None:
                return head.next
            r = r.next

        while r is not None:
            l = l.next
            r = r.next
        l.next = l.next.next
        return head


s = Solution()
test_functions = [ s.removeNthFromEnd_TwoPass, s.removeNthFromEnd_TwoPointers, ]
arg_names = ["head", "n"]

inputs = [ ([1,2,3,4,5], 2), ([1], 1), ([1,2], 1), ([1,2],2), ]
checks = [ [1,2,3,5], [], [1], [2], ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for args, check in zip(inputs, checks):
        args = (ListNode.from_list(args[0]), args[1])
        if type(args) != type(tuple()) and len(arg_names) == 1: args = tuple([args])
        arg_printer(args, arg_names)
        result = f(*args)
        result = result.to_list() if result is not None else []
        print(f"result=({list2str(result)})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

