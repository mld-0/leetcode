#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
from sortedcontainers import SortedSet
import heapq
from typing import List, Optional

#   runtime: TLE
class SeatManager_List:

    def __init__(self, n: int):
        self.seat_taken = [ False ] * (n+1)

    def reserve(self) -> int:
        first_available = None
        for i in range(1, len(self.seat_taken)):
            if not self.seat_taken[i]:
                first_available = i
                break
        assert (not first_available is None)
        self.seat_taken[first_available] = True
        return first_available

    def unreserve(self, seatNumber: int) -> None:
        assert self.seat_taken[seatNumber] == True
        self.seat_taken[seatNumber] = False


#   runtime: beats 6%
class SeatManager_SortedSet:

    def __init__(self, n: int):
        self.seats_available = SortedSet(range(1, n+1))

    def reserve(self) -> int:
        return self.seats_available.pop(0)

    def unreserve(self, seatNumber: int) -> None:
        self.seats_available.add(seatNumber)


#   runtime: TLE
class SeatManager_BitSet:

    class BitSet:
        def __init__(self, size):
            self.bitset = [0] * ((size >> 3) + 1)
        def insert(self, num):
            self.bitset[num >> 3] |= 1 << (num & 7)
        def remove(self, num):
            self.bitset[num >> 3] &= ~(1 << (num & 7))
        def contains(self, num):
            return (self.bitset[num >> 3] & (1 << (num & 7))) != 0
        def first_missing_positive(self):
            for i in range(len(self.bitset)):
                for j in range(8):
                    if (self.bitset[i] & (1 << j)) == 0:
                        return (i << 3) + j

    def __init__(self, n: int):
        self.seats_taken = self.BitSet(n-1)

    def reserve(self) -> int:
        first_available = self.seats_taken.first_missing_positive()
        self.seats_taken.insert(first_available)
        return first_available + 1

    def unreserve(self, seatNumber: int) -> None:
        self.seats_taken.remove(seatNumber-1)


#   runtime: beats 85%
class SeatManager_ans_MinHeap:

    def __init__(self, n):
        self.available_seats = [i for i in range(1, n + 1)]

    def reserve(self):
        seat_number = heapq.heappop(self.available_seats)
        return seat_number

    def unreserve(self, seat_number):
        heapq.heappush(self.available_seats, seat_number)


#   runtime: beats 99%
class SeatManager_ans_MinHeap_Optimised:

    def __init__(self, n):
        self.marker = 1
        self.available_seats = []

    def reserve(self):
        if self.available_seats:
            seat_number = heapq.heappop(self.available_seats)
            return seat_number
        seat_number = self.marker
        self.marker += 1
        return seat_number

    def unreserve(self, seat_number):
        heapq.heappush(self.available_seats, seat_number)


#   runtime: beats 11%
class SeatManager_ans_SortedSet:

    def __init__(self, n):
        self.marker = 1
        self.available_seats = SortedSet()

    def reserve(self):
        if self.available_seats:
            seat_number = self.available_seats.pop(0)
            return seat_number
        seat_number = self.marker
        self.marker += 1
        return seat_number

    def unreserve(self, seat_number):
        self.available_seats.add(seat_number)


def run_solution(c, ops, vals):
    assert len(vals[0]) == 1
    initial_value = vals[0][0]
    vals = vals[1:]
    assert len(ops) == len(vals)
    assert issubclass(c, object)
    s = c(initial_value)
    result = [ None, ]
    for action, loop_vals in zip(ops, vals):
        loop_result = None
        if action == "reserve":
            assert len(loop_vals) == 0
            loop_result = s.reserve()
        elif action == "unreserve":
            assert len(loop_vals) == 1
            s.unreserve(loop_vals[0])
        result.append(loop_result)
    return result

test_classes = [ SeatManager_List, SeatManager_SortedSet, SeatManager_BitSet, SeatManager_ans_MinHeap, SeatManager_ans_MinHeap_Optimised, SeatManager_ans_SortedSet, ]

inputs = [ (["reserve","reserve","unreserve","reserve","reserve","reserve","reserve","unreserve"],[[5],[],[],[2],[],[],[],[],[5]]), ]
checks = [ [None,1,2,None,2,3,4,5,None], ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for c in test_classes:
    print(c.__name__)
    start_time = time.time()
    for (ops, vals), check in zip(inputs, checks):
        print(f"ops=({ops}), vals=({vals})")
        result = run_solution(c, ops, vals)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

