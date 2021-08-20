
class Solution:

    def calcArea(self, height: list[int], start: int, end: int) -> int:
        return min(height[end], height[start]) * abs(end - start)

    #   Result:
    #       runtime: 632ms (beats 96%)
    def maxArea_Second(self, height: list[int]) -> int:
        V = 0
        start = i = 0
        end = j = len(height)-1
        
        while (i < j):
            #   Evaluate h/V 
            h = min(height[i], height[j])
            trial_V = h * (j - i)
            if (trial_V > V):
                V = trial_V
                start = i
                end = j
            
            #   Increment i until height[i] > h (or out of bounds)
            while (h >= height[i] and i < j):
                i += 1
            
            #   Decrement j until height[j] > h (or out of bounds)
            while (h >= height[j] and i < j):
                j -= 1
            
        return V

    #   Result:
    #       runtime: Time Limit Exceded
    def maxArea_BruteForce(self, height: list[int]) -> int:
        V = 0
        start = 0
        end = len(height)-1

        for i in range(0, len(height)-1):
            for j in range(1, len(height)):
                h = min(height[i], height[j])
                trial_V = h * (j - i)
                if trial_V > V:
                    V = trial_V
                    start = i
                    end = j

        return V


    #   Wrong
    def maxArea_First(self, height: list[int]) -> int:
        start = 0 
        end = len(height)-1
        #   while there is a line in height[start+1, end] > min(height[start], height[end])
        while ( any([ height[x] > min(height[start], height[end]) for x in range(start+1, end) ]) ):
            #   What is the tallest line between [start+1, end)
            index_max = start+1
            #if height[end] < height[start]:
            #    index_max = end
            for i in range(start+1, end):
                if height[i] > height[index_max]:
                    index_max = i
            #   If swapping whichever of start/end has the smaller height with index_max produces a larger area, do so and continue, otherwise break (and return area as per current start/end)
            if height[end] > height[start]:
                if (self.calcArea(height, index_max, end) > self.calcArea(height, start, end)):
                    start = index_max
                else:
                    break
            else:
                if (self.calcArea(height, start, index_max) > self.calcArea(height, start, end)):
                    end = index_max
                else:
                    break

        return self.calcArea(height, start, end)


    def maxArea(self, height: list[int]) -> int:
        return self.maxArea_BruteForce(height)

s = Solution()

values = [ 1,8,6,2,5,4,8,3,7 ]
check = 49
result = s.maxArea(values)
print("result=(%s)" % result)
assert(result == check)


input_items = [ [1,8,6,2,5,4,8,3,7], [1,1], [4,3,2,1,4], [1,2,1], [1,2,4,3] ]
check_items = [ 49, 1, 16, 2, 4 ]

for loop_input, loop_check in zip(input_items, check_items):
    print("loop_input=(%s)" % str(loop_input))
    loop_result = s.maxArea(loop_input)
    print("loop_result=(%s)" % loop_result)
    assert(loop_result == loop_check)

