import time
from collections import defaultdict
from typing import List, Optional, Dict

class Solution:

    #   runtime: beats 67%
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def validate_row(row: int) -> bool:
            elements = defaultdict(int)
            for col in range(9):
                current = board[row][col]
                if current == ".":
                    continue
                elements[current] += 1
                if elements[current] > 1:
                    return False
            return True

        def validate_col(col: int) -> bool:
            elements = defaultdict(int)
            for row in range(9):
                current = board[row][col]
                if current == ".":
                    continue
                elements[current] += 1
                if elements[current] > 1:
                    return False
            return True

        def validate_sector(i: int, j: int) -> bool:
            elements = defaultdict(int)
            for delta_row in range(3):
                for delta_col in range(3):
                    row = delta_row + i * 3
                    col = delta_col + j * 3
                    current = board[row][col]
                    if current == ".":
                        continue
                    elements[current] += 1
                    if elements[current] > 1:
                        return False
            return True

        for i in range(9):
            if not validate_row(i):
                return False
            if not validate_col(i):
                return False
        for i in range(3):
            for j in range(3):
                if not validate_sector(i, j):
                    return False
        return True


    #   runtime: beats 91%
    def isValidSudoku_ans_Set(self, board: List[List[str]]) -> bool:
        N = 9
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]
        for r in range(N):
            for c in range(N):
                val = board[r][c]
                if val == ".":
                    continue
                if val in rows[r]:
                    return False
                rows[r].add(val)
                if val in cols[c]:
                    return False
                cols[c].add(val)
                idx = (r // 3) * 3 + c // 3
                if val in boxes[idx]:
                    return False
                boxes[idx].add(val)
        return True


s = Solution()
test_functions = [ s.isValidSudoku, s.isValidSudoku_ans_Set, ]

inputs = [
        [["5","3",".",".","7",".",".",".","."]
         ,["6",".",".","1","9","5",".",".","."]
         ,[".","9","8",".",".",".",".","6","."]
         ,["8",".",".",".","6",".",".",".","3"]
         ,["4",".",".","8",".","3",".",".","1"]
         ,["7",".",".",".","2",".",".",".","6"]
         ,[".","6",".",".",".",".","2","8","."]
         ,[".",".",".","4","1","9",".",".","5"]
         ,[".",".",".",".","8",".",".","7","9"]],
        [["8","3",".",".","7",".",".",".","."]
         ,["6",".",".","1","9","5",".",".","."]
         ,[".","9","8",".",".",".",".","6","."]
         ,["8",".",".",".","6",".",".",".","3"]
         ,["4",".",".","8",".","3",".",".","1"]
         ,["7",".",".",".","2",".",".",".","6"]
         ,[".","6",".",".",".",".","2","8","."]
         ,[".",".",".","4","1","9",".",".","5"]
         ,[".",".",".",".","8",".",".","7","9"]]
        ]
checks = [ True, False, ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for board, check in zip(inputs, checks):
        print(f"board=({board})")
        result = f(board)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

