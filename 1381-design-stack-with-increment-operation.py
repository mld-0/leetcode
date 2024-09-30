#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
from collections import deque
from typing import List, Optional

"""Design a stack which allows us to increment the bottom `k` values by `val`"""

#   runtime: beats 49%
#    memory: beats 58%
class CustomStackNaive:

    def __init__(self, maxSize: int):
        self.count = 0
        self.maxSize = maxSize
        self.values = []

    def push(self, x: int) -> None:
        if self.count >= self.maxSize:
            return
        self.values.append(x)
        self.count += 1

    def pop(self) -> int:
        if self.count == 0:
            return -1
        self.count -= 1
        return self.values.pop()

    def increment(self, k: int, val: int) -> None:
        for i in range(k):
            if i >= self.count:
                break
            self.values[i] += val


#   runtime: beats 99%
#    memory: beats 58%
class CustomStack_i:

    def __init__(self, maxSize: int):
        self.count = 0
        self.maxSize = maxSize
        self.values = []
        self.increments = []

    def push(self, x: int) -> None:
        if self.count >= self.maxSize:
            return
        self.values.append(x)
        self.count += 1

    def pop(self) -> int:
        if self.count == 0:
            self.increments = []
            return -1
        count = self.count
        self.count -= 1
        output = self.values.pop()
        i = 0
        while i < len(self.increments):
            if count <= self.increments[i][0]:
                output += self.increments[i][1]
                self.increments[i][0] -= 1
            i += 1
        return output

    def increment(self, k: int, val: int) -> None:
        if self.count == 0:
            return
        if k > self.count:
            k = self.count
        for i in range(len(self.increments)):
            if self.increments[i][0] == k:
                self.increments[i][1] += val
                return
        self.increments.append( [k, val] )



#   runtime: beats 99%
#    memory: beats 58%
class CustomStack_Ans:

    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.values = []
        self.increments = []

    def push(self, x):
        if len(self.values) < self.maxSize:
            self.values.append(x)
            self.increments.append(0)

    def pop(self):
        if len(self.values) == 0:
            return -1
        if len(self.values) > 1:
            self.increments[-2] += self.increments[-1]
        return self.values.pop() + self.increments.pop()
    
    def increment(self, k, val):
        if len(self.increments) > 0:
            k = min(k, len(self.increments))
            self.increments[k-1] += val


def run_solution(c, ops, vals):
    assert len(ops) == len(vals)
    assert issubclass(c, object)
    s = None
    result = []
    for action, loop_vals in zip(ops, vals):
        loop_result = None
        if action == "CustomStack":
            assert len(loop_vals) == 1
            s = c(loop_vals[0])
        elif action == "push":
            assert len(loop_vals) == 1
            s.push(loop_vals[0])
        elif action == "pop":
            assert len(loop_vals) == 0
            loop_result = s.pop()
        elif action == "increment":
            assert len(loop_vals) == 2
            s.increment(loop_vals[0], loop_vals[1])
        result.append(loop_result)
    return result

test_classes = [ CustomStackNaive, CustomStack_i, CustomStack_Ans, ]

inputs = [ (["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"], [[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]), (["CustomStack","push","pop","increment","pop","increment","push","pop","push","increment","increment","increment"], [[2],[34],[],[8,100],[],[9,91],[63],[],[84],[10,93],[6,45],[10,4]]), ]
checks = [ [None,None,None,2,None,None,None,None,None,103,202,201,-1], [None,None,34,None,-1,None,None,63,None,None,None,None], ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for c in test_classes:
    print(c.__name__)
    start_time = time.time()
    for (actions, loop_inputs), check in zip(inputs, checks):
        print(f"actions=({actions}), loop_inputs=({loop_inputs})")
        result = run_solution(c, actions, loop_inputs)
        print(f"result=({result})")
        assert len(result) == len(check), "Check comparison failed i"
        assert result == check, "Check comparison failed ii"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

