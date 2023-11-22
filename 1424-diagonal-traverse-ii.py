import time
from collections import defaultdict, deque
from typing import List, Optional

class Solution:

    def findDiagonalOrder_naive(self, nums: List[List[int]]) -> List[int]:
        M = len(nums)
        N = max( [ len(nums[i]) for i in range(len(nums)) ] )
        if N == 1:
            return [ n[0] for n in nums ]
        if M == 1:
            return [ n for n in nums[0] ]
        result = []
        for start_row in range(M):
            start_col = 0
            for i in range(N):
                row = start_row - i
                col = start_col + i
                if col < 0 or col >= len(nums[row]):
                    continue
                if col < 0 or col >= N:
                    break
                if row < 0 or row >= len(nums): 
                    break
                result.append(nums[row][col])
        for start_col in range(1, N):
            start_row = len(nums) - 1
            for i in range(M):
                row = start_row - i
                col = start_col + i
                if col < 0 or col >= len(nums[row]):
                    continue
                if col < 0 or col >= N:
                    break
                if row < 0 or row >= len(nums):
                    break
                result.append(nums[row][col])
        return result


    #   runtime: beats 83%
    def findDiagonalOrder_ii(self, nums: List[List[int]]) -> List[int]:
        temp = []
        for row in range(len(nums)):
            for col in range(len(nums[row])):
                temp.append( (row+col,-row,nums[row][col]) )
        temp.sort()
        return [ x[2] for x in temp ]


    #   runtime: beats 96%
    def findDiagonalOrder_ans_Dict(self, nums: List[List[int]]) -> List[int]:
        temp = defaultdict(list)
        for row in range(len(nums)-1, -1, -1):
            for col in range(len(nums[row])):
                temp[row+col].append(nums[row][col])
        result = []
        for curr in sorted(temp.keys()):
            result.extend(temp[curr])
        return result


    #   runtime: beats 99%
    def findDiagonalOrder_ans_BFS(self, nums: List[List[int]]) -> List[int]:
        queue = deque( [(0,0)] )
        result = []
        while queue:
            (row, col) = queue.popleft()
            result.append(nums[row][col])
            if col == 0 and row+1 < len(nums):
                queue.append( (row+1, col) )
            if col+1 < len(nums[row]):
                queue.append( (row, col+1) )
        return result


s = Solution()
test_functions = [ s.findDiagonalOrder_naive, s.findDiagonalOrder_ii, s.findDiagonalOrder_ans_Dict, s.findDiagonalOrder_ans_BFS, ]

inputs = [ [[1,2,3],[4,5,6],[7,8,9]], [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]], [[1,2,3,4,5,6]], [[1],[2],[3]], ]
checks = [ [1,4,2,7,5,3,8,6,9], [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16], [1,2,3,4,5,6], [1,2,3], ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for vals, check in zip(inputs, checks):
        print(f"vals=({vals})")
        result = f(vals)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

