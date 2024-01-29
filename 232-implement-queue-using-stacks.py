#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
from collections import deque
from typing import List, Optional

def list2str(vals, max_str_length=60):
    #   {{{
    """Return a list as a string, in the format of [1,2,3,4,...,n] if the whole list cannot be kept under `max_str_length` characters"""
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

#   Implement a queue with the operations `push()`, `pop()`, `peek()`, and `empty()` using two stacks

#   runtime: beats 98%
#   memory: beats 80%
class MyQueue_deque:

    def __init__(self):
        self.vals = deque()

    def push(self, x: int) -> None:
        self.vals.append(x)

    def pop(self) -> int:
        return self.vals.popleft()

    def peek(self) -> int:
        return self.vals[0]

    def empty(self) -> bool:
        return len(self.vals) == 0


#   runtime: beats 98%
#   memory: beats 68%
class MyQueue_list:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        
    def push(self, x: int) -> None:
        self.s2.append(x)
        
    def pop(self) -> int:
        if len(self.s1) == 0:
            while len(self.s2) > 0:
                self.s1.append(self.s2.pop())
        return self.s1.pop() 

    def peek(self) -> int:
        if len(self.s1) == 0:
            while len(self.s2) > 0:
                self.s1.append(self.s2.pop())
        return self.s1[-1]
        
    def empty(self) -> bool:
        return len(self.s1) == 0 and len(self.s2) == 0
        

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
        elif action == "peek":
            assert len(loop_vals) == 0
            loop_result = s.peek()
        elif action == "pop":
            assert len(loop_vals) == 0
            loop_result = s.pop()
        elif action == "empty":
            assert len(loop_vals) == 0
            loop_result = s.empty()
        result.append(loop_result)
    return result

test_classes = [ MyQueue_deque, MyQueue_list, ]

inputs = [ (["MyQueue","push","push","peek","pop","empty"], [[],[1],[2],[],[],[]]), (["MyQueue", *["push" for _ in range(100)], *["pop" for _ in range(100)], ], [ [], *[[x] for x in range(100)], *[[] for x in range(100)], ]), ]
checks = [ [None,None,None,1,1,False], [None, *[None for _ in range(100)], *[x for x in range(100)], ], ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for c in test_classes:
    print(c.__name__)
    start_time = time.time()
    for (ops, vals), check in zip(inputs, checks):
        print(f"ops=({list2str(ops)}), vals=({list2str(vals)})")
        result = run_solution(c, ops, vals)
        print(f"result=({list2str(result)})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

