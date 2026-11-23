import time
from collections import deque
from typing import List, Optional

#   runtime: TLE
class ProductOfNumbers_naive:

    def __init__(self):
        self.vals = deque()

    def add(self, num: int) -> None:
        self.vals.appendleft(num)

    def getProduct(self, k: int) -> int:
        result = 1
        for n in range(k):
            result *= self.vals[n]
        return result


#   runtime: TLE
class ProductOfNumbers_ii:

    def __init__(self):
        self.vals = deque()
        self.answers = dict()

    def add(self, num: int) -> None:
        self.vals.appendleft(num)
        new_answers = dict()
        for k in self.answers.keys():
            new_answers[k+1] = self.answers[k] * num
        self.answers = new_answers

    def getProduct(self, k: int) -> int:
        if k in self.answers:
            return self.answers[k]
        result = 1
        for n in range(k):
            result *= self.vals[n]
        self.answers[k] = result
        return result


#   runtime: TLE
class ProductOfNumbers_iii:

    def __init__(self):
        self.vals = deque()

    def add(self, num: int) -> None:
        if num == 1:
            self.vals.appendleft(num)
            return
        for i in range(len(self.vals)):
            self.vals[i] *= num
        self.vals.appendleft(num)

    def getProduct(self, k: int) -> int:
        return self.vals[k-1]


#   runtime: TLE
class ProductOfNumbers_iv:

    def __init__(self):
        raise NotImplementedError("Non TLE Solution not found yet")

    def add(self, num: int) -> None:
        ...

    def getProduct(self, k: int) -> int:
        ...



def list2str(vals, max_str_length=60):
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

def run_solution(c, ops, vals):
    assert len(ops) == len(vals)
    assert issubclass(c, object)
    s = c()
    result = []
    for action, loop_val in zip(ops, vals):
        loop_result = None
        if action == "add":
            assert len(loop_val) == 1
            loop_result = s.add(*loop_val)
        elif action == "getProduct":
            assert len(loop_val) == 1
            loop_result = s.getProduct(*loop_val)
        result.append(loop_result)
    print(s.vals)
    return result

test_classes = [ ProductOfNumbers_naive, ProductOfNumbers_ii, ProductOfNumbers_iii, ProductOfNumbers_iv, ]

inputs = [
    ( ["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"],
     [[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]] ),
    ( ["ProductOfNumbers","add","add","add","add","add","add","add","add","getProduct","getProduct","getProduct","getProduct","add"],
    [[],[2],[4],[1],[7],[4],[1],[4],[2],[3],[5],[6],[8],[4]] ),
]
checks = [
    [None,None,None,None,None,None,20,40,0,None,32],
    [None,None,None,None,None,None,None,None,None,8,224,224,1792,None],
]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for c in test_classes:
    print(c.__name__)
    start_time = time.time()
    for (ops, args), check in zip(inputs, checks):
        assert len(ops) == len(args)
        print(f"ops=({list2str(ops)})")
        print(f"args=({list2str(args)})")
        result = run_solution(c, ops, args)
        print(f"result=({list2str(result)})")
        #print(f"result=({result})")
        assert len(result) == len(check), "Check comparison failed (length)"
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

