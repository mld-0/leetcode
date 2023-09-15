import time
from collections import defaultdict, Counter
from typing import List, Optional

class Solution:
    """Given a 2d matrix, `grid`, return the number of pairs of rows and columns which are the same"""

    #   runtime: beats 93%
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = defaultdict(int)
        cols = defaultdict(int)
        for i in range(len(grid)):
            row = tuple(grid[i])
            col = tuple([grid[j][i] for j in range(len(grid))])
            rows[row] += 1
            cols[col] += 1
        result = 0
        for element in set(rows.keys()) & set(cols.keys()):
            result += rows[element] * cols[element]
        return result


    #   runtime: beats 46%
    def equalPairs_ans_Trie(self, grid: List[List[int]]) -> int:

        class TrieNode:
            def __init__(self):
                self.count = 0
                self.children = {}
        class Trie:
            def __init__(self):
                self.trie = TrieNode()
            def insert(self, array):
                my_trie = self.trie
                for a in array:
                    if a not in my_trie.children:
                        my_trie.children[a] = TrieNode()
                    my_trie = my_trie.children[a] 
                my_trie.count += 1
            def search(self, array):
                my_trie = self.trie
                for a in array:
                    if a in my_trie.children:
                        my_trie = my_trie.children[a]
                    else:
                        return 0
                return my_trie.count

        my_trie = Trie()
        count = 0
        n = len(grid)        
        for row in grid:
            my_trie.insert(row)
        for c in range(n):
            col_array = [grid[i][c] for i in range(n)]
            count += my_trie.search(col_array)
        return count    


s = Solution()
test_functions = [ s.equalPairs, s.equalPairs_ans_Trie, ]

inputs = [ [[3,2,1],[1,7,6],[2,7,7]], [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]], [[13,13],[13,13]], ]
checks = [ 1, 3, 4, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for grid, check in zip(inputs, checks):
        print(f"grid=({grid})")
        result = f(grid)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

