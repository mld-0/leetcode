from typing import List

class Solution:

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        return self.floodFill_A(image, sr, sc, newColor)
        #return self.floodFill_Queue(image, sr, sc, newColor)

    #   runtime: beats 99%
    def floodFill_A(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]

        if oldColor == newColor:
            return image

        def fill(sr, sc):
            if sr < 0 or sr >= len(image):
                return
            if sc < 0 or sc >= len(image[0]):
                return
            if image[sr][sc] == oldColor:
                image[sr][sc] = newColor
                fill(sr+1, sc)
                fill(sr-1, sc)
                fill(sr, sc+1)
                fill(sr, sc-1)

        fill(sr, sc)
        return image

    
    #   TODO: 2021-09-21T17:20:50AEST _leetcode, 733-flood-fill, queue (iterative) floodFill implementation
    def floodFill_Queue(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        pass


s = Solution()

input_values = [ ([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2), ([[0,0,0],[0,0,0]], 0, 0, 2), ([[0,0,0],[0,1,1]], 1, 1, 1), ([[0,0,1],[0,1,1]], 1, 1, 2) ]
input_checks = [ [[2,2,2],[2,2,0],[2,0,1]], [[2,2,2],[2,2,2]], [[0,0,0],[0,1,1]], [[0,0,2],[0,2,2]] ]

for (images, sr, sc, newColor), check in zip(input_values, input_checks):
    result = s.floodFill(images, sr, sc, newColor)
    print("result=(%s)" % str(result))
    assert( result == check )
    print()

