
class NumArray:

    def __init__(self, nums):
        self.sums_list = []
        _sum = 0;
        for i, val_i in enumerate(nums):
            _sum += val_i
            self.sums_list.append(_sum)




    def sumRange(self, left: int, right: int) -> int:
        left -= 1
        if (left == -1):
            return self.sums_list[right]
        return self.sums_list[right] - self.sums_list[left]

nums = [-2,0,3,-5,2,-1]
print(nums)
test_vals = [[0,2],[2,5],[0,5]]
expected = [1, -1, -3]
obj = NumArray(nums)

results = []
for left, right in test_vals:
    results.append(obj.sumRange(left, right))

print(results)

