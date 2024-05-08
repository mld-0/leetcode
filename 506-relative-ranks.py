#   {{{3
#   vim: set tabstop=4 modeline modelines=10:
#   vim: set foldlevel=2 foldcolumn=2 foldmethod=marker:
#   {{{2
import time
import heapq
from collections import defaultdict
from typing import List, Optional

class Solution:
    """Given an array, `score` of unique values, return a list of where each score ranks, with 1st/2nd/3rd being denoted as medalists"""

    #   runtime: beats 91%
    #    memory: beats 22%
    def findRelativeRanks_Sorting(self, score: List[int]) -> List[str]:
        n = len(score)
        medals = { 1: "Gold Medal", 2: "Silver Medal", 3: "Bronze Medal", }
        _, places = zip(*sorted(zip(score, range(n)), key=lambda x: -x[0]))
        result = [ None for _ in range(n) ]
        for i, place in enumerate(places):
            result[place] = medals[i+1] if i+1 in medals else str(i+1)
        return result


    #   runtime: beats 95%
    #    memory: beats 23%
    def findRelativeRanks_Heap(self, score: List[int]) -> List[str]:
        n = len(score)
        medals = { 1: "Gold Medal", 2: "Silver Medal", 3: "Bronze Medal", }
        score = [ (-x, i) for i, x in enumerate(score) ]
        heapq.heapify(score)
        result = [ None for _ in range(n) ]
        i = 0
        while len(score) > 0:
            s, place = heapq.heappop(score)
            result[place] = medals[i+1] if i+1 in medals else str(i+1)
            i += 1
        return result


    #   runtime: beats 98%
    #    memory: beats 71%
    def findRelativeRanks_ans_Sorting_IndexDict(self, score: List[int]) -> List[str]:
        n = len(score)
        medals = { 1: "Gold Medal", 2: "Silver Medal", 3: "Bronze Medal", }
        score_to_index = dict()
        for i, s in enumerate(score):
            score_to_index[s] = i
        score = sorted(score, reverse=True)
        result = [ None for _ in range(n) ]
        for i in range(n):
            s = score[i]
            index = score_to_index[s]
            result[index] = medals[i+1] if i+1 in medals else str(i+1)
        return result


    #   runtime: beats 74%
    #    memory: beats 71%
    def findRelativeRanks_ans_ArrayAsMap(self, score: List[int]) -> List[str]:
        N = len(score)
        M = max(score)
        medals = { 1: "Gold Medal", 2: "Silver Medal", 3: "Bronze Medal", }
        score_to_index = [ 0 for _ in range(M+1) ]
        for i in range(N):
            score_to_index[score[i]] = i+1
        result = [ None for _ in range(N) ]
        place = 1
        for i in range(M, -1, -1):
            if score_to_index[i] == 0:
                continue
            origional_index = score_to_index[i] - 1
            result[origional_index] = medals[place] if place in medals else str(place)
            place += 1
        return result


    #   runtime: beats 86%
    #    memory: beats 72%
    def findRelativeRanks_ans_Mapping(self, score: List[int]) -> List[str]:
        score_sorted = sorted(score, reverse = True)
        awards = [ "Gold Medal", "Silver Medal", "Bronze Medal" ] \
                    + [ str(i) for i in range(4, len(score) + 1) ]
        num_to_award = {num : award for num, award in zip(score_sorted, awards)}
        results = [num_to_award[num] for num in score]
        return results


s = Solution()
test_functions = [ s.findRelativeRanks_Sorting, s.findRelativeRanks_Heap, s.findRelativeRanks_ans_Sorting_IndexDict, s.findRelativeRanks_ans_ArrayAsMap, s.findRelativeRanks_ans_Mapping, ]

inputs = [ [5,4,3,2,1], [10,3,8,9,4], ]
checks = [ ["Gold Medal","Silver Medal","Bronze Medal","4","5"], ["Gold Medal","5","Bronze Medal","Silver Medal","4"], ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for score, check in zip(inputs, checks):
        print(f"score=({score})")
        result = f(score[:])
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

