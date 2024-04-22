#   {{{3
       #   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
from collections import deque
from typing import List, Optional

class Solution:
    """We start with the combination '0000' on a rotary dial. At each step, we may rotate one wheel, provided we do not set the dial to one of the combinations in `deadends`. What is the minimum number of steps to reach `target`."""

    #   runtime: beats 79%
    #    memory: beats 80%
    def openLock_i(self, deadends: List[str], target: str) -> int:

        def increment(digit):
            digit = int(digit)
            if digit < 9:
                return str(digit+1)
            return "0"

        def decrement(digit):
            digit = int(digit)
            if digit > 0:
                return str(digit-1)
            return "9"

        seen = set()
        deadends = set(deadends)
        initial = ''.join( ["0" * len(target) ] )
        if target in deadends or initial in deadends:
            return -1
        queue = deque()
        queue.append( (initial, 0) )
        seen.add(initial)
        while queue:
            current, turns = queue.popleft()
            if current == target:
                return turns
            for i, c in enumerate(current):
                next_1 = current[:i] + increment(c) + current[i+1:]
                next_2 = current[:i] + decrement(c) + current[i+1:]
                if next_1 == target:
                    return turns+1
                if next_1 not in deadends and next_1 not in seen:
                    queue.append( (next_1, turns+1) )
                    seen.add(next_1)
                if next_2 == target:
                    return turns+1
                if next_2 not in deadends and next_2 not in seen:
                    queue.append( (next_2, turns+1) )
                    seen.add(next_2)
        return -1

    #   {{{
    ##   runtime: beats 80%
    ##    memory: beats 94%
    #def openLock_ii(self, deadends: List[str], target: str) -> int:
    #    def rotate(digit, position, direction):
    #        assert (direction == 1 or direction == -1)
    #        assert (position >= 0 and position <= 3)
    #        position = 3 - position
    #        if digit < 10**position:
    #            if direction == 1:
    #                return 10**position + digit
    #            elif direction == -1:
    #                return 9 * 10**position + digit
    #        leading = digit // 10**(position+1)
    #        current = (digit // 10**(position)) % 10
    #        trailing = digit % 10**(position)
    #        if direction == 1:
    #            current = current + 1 if current < 9 else 0
    #        elif direction == -1:
    #            current = current - 1 if current > 0 else 9
    #        result = leading * 10**(position+1) + current * 10**position + trailing
    #        return result
    #    seen = set()
    #    deadends = set([int(x) for x in deadends])
    #    target = int(target)
    #    initial = 0
    #    if target in deadends or initial in deadends:
    #        return -1
    #    queue = deque()
    #    queue.append( (initial, 0) )
    #    seen.add(initial)
    #    while queue:
    #        current, turns = queue.popleft()
    #        if current == target:
    #            return turns
    #        for i in range(4):
    #            next_1 = rotate(current, i, 1)
    #            next_2 = rotate(current, i, -1)
    #            if next_1 == target:
    #                return turns+1
    #            if next_1 not in deadends and next_1 not in seen:
    #                queue.append( (next_1, turns+1) )
    #                seen.add(next_1)
    #            if next_2 == target:
    #                return turns+1
    #            if next_2 not in deadends and next_2 not in seen:
    #                queue.append( (next_2, turns+1) )
    #                seen.add(next_2)
    #    return -1
    #   }}}

    #   runtime: beats 83%
    #    memory: beats 92%
    def openLock_ii(self, deadends: List[str], target: str) -> int:

        def rotate(digit, position, direction):
            position = 3 - position
            if digit < 10**position:
                if direction == 1:
                    return 10**position + digit
                elif direction == -1:
                    return 9 * 10**position + digit
            leading = digit // 10**(position+1)
            current = (digit // 10**(position)) % 10
            trailing = digit % 10**(position)
            if direction == 1:
                current = current + 1 if current < 9 else 0
            elif direction == -1:
                current = current - 1 if current > 0 else 9
            result = leading * 10**(position+1) + current * 10**position + trailing
            return result

        seen = set([int(x) for x in deadends])
        target = int(target)
        initial = 0
        if initial in seen:
            return -1
        queue = deque()
        queue.append( (initial, 0) )
        seen.add(initial)
        while queue:
            current, turns = queue.popleft()
            if current == target:
                return turns
            for i in range(4):
                next_1 = rotate(current, i, 1)
                next_2 = rotate(current, i, -1)
                if next_1 == target:
                    return turns+1
                if next_1 not in seen:
                    queue.append( (next_1, turns+1) )
                    seen.add(next_1)
                if next_2 == target:
                    return turns+1
                if next_2 not in seen:
                    queue.append( (next_2, turns+1) )
                    seen.add(next_2)
        return -1


    #   runtime: beats 95%
    #    memory: beats 80%
    def openLock_ans(self, deadends: List[str], target: str) -> int:
        next_slot = { "0": "1", "1": "2", "2": "3", "3": "4", "4": "5", "5": "6", "6": "7", "7": "8", "8": "9", "9": "0", }
        prev_slot = { "0": "9", "1": "0", "2": "1", "3": "2", "4": "3", "5": "4", "6": "5", "7": "6", "8": "7", "9": "8", }
        visited_combinations = set(deadends)
        pending_combinations = deque()
        turns = 0
        if "0000" in visited_combinations:
            return -1
        pending_combinations.append("0000")
        visited_combinations.add("0000")
        while pending_combinations:
            curr_level_nodes_count = len(pending_combinations)
            for _ in range(curr_level_nodes_count):
                current_combination = pending_combinations.popleft()
                if current_combination == target:
                    return turns
                for wheel in range(4):
                    new_combination = list(current_combination)
                    new_combination[wheel] = next_slot[new_combination[wheel]]
                    new_combination_str = "".join(new_combination)
                    if new_combination_str not in visited_combinations:
                        pending_combinations.append(new_combination_str)
                        visited_combinations.add(new_combination_str)
                    new_combination = list(current_combination)
                    new_combination[wheel] = prev_slot[new_combination[wheel]]
                    new_combination_str = "".join(new_combination)
                    if new_combination_str not in visited_combinations:
                        pending_combinations.append(new_combination_str)
                        visited_combinations.add(new_combination_str)
            turns += 1
        return -1



def test_rotate():
    #   {{{
    print("test_rotate_increment:")
    inputs = [ ("0000",0), ("0000",1), ("1234",1), ("1934",1), ("1294",2), ("1239",3), ("1234",0), ("1234",2), ("1234",3), ]
    checks = [ "1000", "0100", "1334", "1034", "1204", "1230", "2234", "1244", "1235", ]
    assert len(inputs) == len(checks)
    for (x,i), check in zip(inputs, checks):
        print(f"x=({int(x)}), i=({i})")
        result = rotate(int(x), i, 1)
        print(f"result=({result})")
        assert result == int(check)
    print()
    print("test_rotate_decement:")
    inputs = [ ("0000",0), ("0000",1), ("1234",1), ("1034",1), ("1204",2), ("1230",3), ("1234",0), ("1234",2), ("1234",3), ]
    checks = [ "9000", "0900", "1134", "1934", "1294", "1239", "0234", "1224", "1233", ]
    assert len(inputs) == len(checks)
    for (x,i), check in zip(inputs, checks):
        print(f"x=({int(x)}), i=({i})")
        result = rotate(int(x), i, -1)
        print(f"result=({result})")
        assert result == int(check)
    print()
    #   }}}

s = Solution()
test_functions = [ s.openLock_i, s.openLock_ii, s.openLock_ans, ]

inputs = [ (["0201","0101","0102","1212","2002"],"0202"), (["8888"],"0009"), (["8887","8889","8878","8898","8788","8988","7888","9888"],"8888"), (["0000"],"8888"), ]
checks = [ 6, 1, -1, -1, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for (deadends, target), check in zip(inputs, checks):
        print(f"deadends=({deadends}), target=({target})")
        result = f(deadends, target)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

