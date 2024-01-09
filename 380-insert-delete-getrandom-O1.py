#   {{{3 #   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
import random
from typing import List, Optional

#   runtime: beats 38%
class RandomizedSet_set:
    def __init__(self):
        self.values = set()

    def insert(self, val: int) -> bool:
        result = val not in self.values
        self.values.add(val)
        return result

    def remove(self, val: int) -> bool:
        result = val in self.values
        if result:
            self.values.remove(val)
        return result

    def getRandom(self) -> int:
        val = random.choice(list(self.values))
        return val


class RandomizedSet_setAndList:
    def __init__(self):
        self.values_list = list()
        self.values_set = set()

    def insert(self, val: int) -> bool:
        raise NotImplementedError()

    def remove(self, val: int) -> bool:
        raise NotImplementedError()

    def getRandom(self) -> int:
        raise NotImplementedError()


#   runtime: beats 99%
class RandomizedSet_ans():
    #   {{{
    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.dict:
            last_element, idx = self.list[-1], self.dict[val]
            self.list[idx], self.dict[last_element] = last_element, idx
            self.list.pop()
            del self.dict[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.list)
    #   }}}


def run_solution(c, ops, vals):
    assert len(ops) == len(vals)
    assert issubclass(c, object)
    s = c()
    result = []
    for action, loop_vals in zip(ops, vals):
        loop_result = None
        if action == "insert":
            loop_result = s.insert(loop_vals[0])
        elif action == "remove":
            loop_result = s.remove(loop_vals[0])
        elif action == "getRandom":
            loop_result = s.getRandom()
        result.append(loop_result)
    return result

def check_results(ops, results, checks) -> bool:
    assert len(ops) == len(results)
    assert len(ops) == len(checks)
    for op, result, check in zip(ops, results, checks):
        if not result in set(check):
            return False
    return True

test_classes = [ RandomizedSet_set, RandomizedSet_setAndList, RandomizedSet_ans, ]

inputs = [ (["insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"], [[1], [2], [2], [], [1], [2], []]) ]
checks = [ [[True], [False], [True], [1,2], [True,False], [True,False], [2]], ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"
assert all( [ len(x[0]) == len(x[1]) for x in inputs ] )

for c in test_classes:
    print(c.__name__)
    start_time = time.time()
    for (ops, vals), check in zip(inputs, checks):
        print(f"ops=({ops}), vals=({vals})")
        result = run_solution(c, ops, vals)
        print(f"result=({result})")
        assert check_results(ops, result, check), "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

