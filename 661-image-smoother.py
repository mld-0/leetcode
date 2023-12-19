import time
import math
import copy
from typing import List, Optional

class Solution:
    """Smooth image given by `img`, that is, set each cell to the average of itself and its surrounding cells"""

    #   runtime: beats 50%
    def imageSmoother_i(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])

        def avg_9by9(x: int, y: int) -> int:
            total = 0
            count = 0
            for delta_i in range(-1,2):
                for delta_j in range(-1,2):
                    i = x + delta_i
                    j = y + delta_j
                    if i < 0 or i >= m:
                        continue
                    if j < 0 or j >= n:
                        continue
                    total += img[i][j]
                    count += 1
            return total // count

        return [ [ avg_9by9(i,j) for j in range(n) ] for i in range(m) ]


    #   runtime: beats 86%
    def imageSmoother_ans_SpaceOptimised(self, img: List[List[int]]) -> List[List[int]]:
        # Save the dimensions of the image.
        m = len(img)
        n = len(img[0])

        # Create a temp array of size n.
        temp = [0] * n

        # Iterate over the cells of the image.
        for i in range(m):
            for j in range(n):
                # Initialize the Sum and count 
                Sum = 0
                count = 0
                # Bottom neighbors
                if i + 1 < m:
                    if j - 1 >= 0:
                        Sum += img[i + 1][j - 1]
                        count += 1
                    Sum += img[i + 1][j]
                    count += 1
                    if j + 1 < n:
                        Sum += img[i + 1][j + 1]
                        count += 1
                # Next neighbor
                if j + 1 < n:
                    Sum += img[i][j + 1]
                    count += 1
                # This cell
                Sum += img[i][j]
                count += 1
                # Previous neighbor
                if j - 1 >= 0:
                    Sum += temp[j - 1]
                    count += 1
                # Top neighbors
                if i - 1 >= 0:
                    # Left-top corner-sharing neighbor.
                    if j - 1 >=  0:
                        Sum += prev_val
                        count += 1
                    # Top edge-sharing neighbor.
                    Sum += temp[j]
                    count += 1
                    # Right-top corner-sharing neighbor.
                    if j + 1 < n:
                        Sum += temp[j + 1]
                        count += 1
                # Store the original value of temp[j], which represents
                # original value of img[i - 1][j].
                if i - 1 >= 0:
                    prev_val = temp[j]
                # Save current value of img[i][j] in temp[j].
                temp[j] = img[i][j]
                # Overwrite with smoothed value.
                img[i][j] = Sum // count

        # Return the smooth image.
        return img


    #   runtime: beats 50%
    def imageSmoother_ans_ConstSpace(self, img: List[List[int]]) -> List[List[int]]:
        # Save the dimensions of the image.
        m = len(img)
        n = len(img[0])

        # Iterate over the cells of the image.
        for i in range(m):
            for j in range(n):
                # Initialize the Sum and count 
                Sum = 0
                count = 0
                # Iterate over all plausible nine indices.
                for x in (i - 1, i, i + 1):
                    for y in (j - 1, j, j + 1):
                        # If the indices form valid neighbor
                        if 0 <= x < m and 0 <= y < n:
                            # Extract the original value of img[x][y].
                            Sum += img[x][y] % 256
                            count += 1
                # Encode the smoothed value in img[i][j].
                img[i][j] += (Sum // count) * 256

        # Extract the smoothed value from encoded img[i][j].
        for i in range(m):
            for j in range(n):
                img[i][j] //= 256

        # Return the smooth image.
        return img


s = Solution()
test_functions = [ s.imageSmoother_i, s.imageSmoother_ans_SpaceOptimised, s.imageSmoother_ans_ConstSpace, ]

inputs = [ [[1,1,1],[1,0,1],[1,1,1]], [[100,200,100],[200,50,200],[100,200,100]], ]
checks = [ [[0,0,0],[0,0,0],[0,0,0]], [[137,141,137],[141,138,141],[137,141,137]], ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for f in test_functions:
    print(f.__name__)
    start_time = time.time()
    for img, check in zip(inputs, checks):
        img = copy.deepcopy(img)
        print(f"img=({img})")
        result = f(img)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

