import time
import copy
from collections import Counter, defaultdict
from typing import List, Optional

class Solution:
    """Determine the h-index for each list, that is, the maximum number `h` for which there are `h` many instances greater than or equal to `h`"""

    #   runtime: beats 91%
    def hIndex(self, citations: List[int]) -> int:
        citation_counts = Counter(citations)
        citation_instances = sorted(citation_counts.keys(), reverse=True)

        if len(citation_instances) == 1:
            return min(len(citations), citations[0])

        counts_greater = defaultdict(int)
        counts_greater[citation_instances[0]] = citation_counts[citation_instances[0]]

        for i in range(1, len(citation_instances)):
            instance = citation_instances[i]
            previous_instance = citation_instances[i-1]
            count = citation_counts[instance]
            previous_count = counts_greater[previous_instance]
            counts_greater[instance] = count + previous_count

        result = 1
        for instance in citation_instances:
            if counts_greater[instance] <= instance:
                result = counts_greater[instance]
            elif result < instance:
                result = instance

        return result


    #   runtime: beats 76%
    def hIndex_ans_Sorting(self, citations: List[int]) -> int:
        citations.sort()
        i = 0
        while i < len(citations) and citations[len(citations)-1-i] > i:
            i += 1
        return i


    #   runtime: beats 88%
    def hIndex_ans_Counting(self, citations: List[int]) -> int:
        n = len(citations)
        papers = [ 0 for _ in range(n+1) ]
        for c in citations:
            papers[min(n,c)] += 1
        k = n
        s = papers[n]
        while k > s:
            k -= 1
            s += papers[k]
        return k


s = Solution()
test_functions = [ s.hIndex, s.hIndex_ans_Sorting, s.hIndex_ans_Counting, ]

inputs = [ [3,0,6,1,5], [1,3,1], [1], [100], [11,15], [4,4,0,0], [1,1], [0,1,1], [2,2,2], [2,3,2], ]
checks = [ 3, 1, 1, 1, 2, 2, 1, 1, 2, 2, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for citations, check in zip(inputs, checks):
        citations = copy.deepcopy(citations)
        print(f"citations=({citations})")
        result = f(citations)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

