#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
from collections import deque
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
    num_elements = len(vals)
    while num_elements > 0:
        formatted_list = build_string(vals, num_elements)
        if len(formatted_list) <= max_str_length:
            break
        num_elements -= 1
    return formatted_list
    #   }}}

#   Implement a stack using two queues

#   runtime: beats 99%
#   memory: beats 70%
class MyStack_list:

    def __init__(self):
        self.vals = []

    def push(self, x: int) -> None:
        self.vals.append(x)

    def pop(self) -> int:
        return self.vals.pop()

    def top(self) -> int:
        return self.vals[-1]

    def empty(self) -> bool:
        return len(self.vals) == 0


#   runtime: beats 99%
#   memory: beats 60%
class MyStack_deque:

    def __init__(self):
        self.q1 = deque()
        self.last = None

    def push(self, x: int) -> None:
        if self.last is not None:
            self.q1.appendleft(self.last)
        self.last = x

    def shuffle_items(self):
        if len(self.q1) >= 1:
            temp = self.q1
            self.q1 = deque()
            while len(temp) > 1:
                self.q1.appendleft(temp.pop())
            self.last = temp.pop()
        else:
            self.last = None

    def pop(self) -> int:
        result = self.last
        self.shuffle_items()
        return result

    def top(self) -> int:
        return self.last

    def empty(self) -> bool:
        return self.last is None and len(self.q1) == 0


#   runtime: beats 93%
#   memory: 70%
class MyStack_ans_deque_nested:

    def __init__(self):
        self.q = None

    def push(self, x):
        q = deque()
        q.append(x)
        q.append(self.q)
        self.q = q

    def pop(self):
        result = self.q.popleft()
        self.q = self.q.popleft()
        return result

    def top(self):
        return self.q[0]

    def empty(self):
        return self.q is None


def run_solution(c, ops, vals):
    assert len(ops) == len(vals)
    assert issubclass(c, object)
    s = c()
    result = []
    for action, loop_vals in zip(ops, vals):
        loop_result = None
        if action == "push":
            assert len(loop_vals) == 1
            loop_result = s.push(loop_vals[0])
        elif action == "pop":
            assert len(loop_vals) == 0
            loop_result = s.pop()
        elif action == "top":
            assert len(loop_vals) == 0
            loop_result = s.top()
        elif action == "empty":
            assert len(loop_vals) == 0
            loop_result = s.empty()
        result.append(loop_result)
    return result

test_classes = [ MyStack_list, MyStack_deque, MyStack_ans_deque_nested, ]
arg_names = ["ops","vals"]

inputs = [ (["MyStack","push","push","top","pop","empty"],[[],[1],[2],[],[],[]]), (["MyStack","push","push","top","push","top"],[[],[1],[2],[],[3],[]]), (["MyStack","push","push","pop","top"],[[],[1],[2],[],[]]), (["MyStack","push","push","push","top"],[[],[1],[2],[3],[]]), (["MyStack","push","pop","empty"],[[],[1],[],[]]), ]
checks = [ [None,None,None,2,2,False], [None,None,None,2,None,3], [None,None,None,2,1], [None,None,None,None,3], [None,None,1,True], ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for c in test_classes:
    print(c.__name__)
    start_time = time.time()
    for args, check in zip(inputs, checks):
        arg_printer(args, arg_names)
        result = run_solution(c, *args)
        print(f"result=({list2str(result)})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

