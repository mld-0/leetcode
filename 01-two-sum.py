
def twoSum_A(nums, target):
    target_difference = dict()
    
    for i, val_i in enumerate(nums):
        target_difference[i] = target - val_i
        
    for i, val_i in target_difference.items():
        temp = [index for index, val in enumerate(nums) if val == val_i]
        for j in temp:
            if i != j:
                return [i, j]


def twoSum_B(nums, target):
    index_by_val = dict()  # keys = vals, values = indexes
    #for i, val_i in enumerate(nums):
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in nums[:i]:  
            return [index_by_val[diff], i]
        index_by_val[nums[i]] = i


result = twoSum_A([3,3], 6)
print(result)
result = twoSum_A([2,7,11,15], 9)
print(result)

result = twoSum_B([3,3], 6)
print(result)
result = twoSum_B([2,7,11,15], 9)
print(result)



