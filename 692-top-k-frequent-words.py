from collections import defaultdict
from collections import Counter
from heapq import nsmallest
from typing import List

class Solution:

    #   runtime: beats 98%
    def topKFrequent_i(self, words: List[str], k: int) -> List[str]:
        counts = defaultdict(int)
        for word in words:
            counts[word] -= 1
        counts = sorted([ (v,k) for k,v in counts.items() ] )
        return [ k for (v,k) in counts ][:k]

    #   runtime: beats 95%
    def topKFrequent_Counter(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        counts = sorted([ (-v,k) for k,v in counts.items() ] )
        return [ k for (v,k) in counts ][:k]

    #   runtime: beats 96%
    def topKFrequent_Ans_MaxHeap(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        counts = nsmallest(k, counts.items(), key=lambda x: (-x[1],x[0]))
        return [ k for (k,v) in counts ]


    def topKFrequent_Ans_MinHeap(self, words: List[str], k: int) -> List[str]:
        raise NotImplementedError()

    def topKFrequent_Ans_Trie(self, words: List[str], k: int) -> List[str]:
        raise NotImplementedError()


s = Solution()
#test_functions = [ s.topKFrequent_i, s.topKFrequent_Counter, s.topKFrequent_Ans_MaxHeap, s.topKFrequent_Ans_MinHeap, s.topKFrequent_Ans_Trie, ]
test_functions = [ s.topKFrequent_i, s.topKFrequent_Counter, s.topKFrequent_Ans_MaxHeap, ]

inputs = [ (["i","love","leetcode","i","love","coding"], 2), (["the","day","is","sunny","the","the","the","sunny","is","is"], 4), ]
checks = [ ["i","love"], ["the","is","sunny","day"], ]
assert len(inputs) == len(checks)

for f in test_functions:
    print(f.__name__)
    for (words,k), check in zip(inputs, checks):
        print(f"words=({words}, k=({k})")
        result = f(words, k)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print()

