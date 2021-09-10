import math

class Solution:


    #   Result:
    #       runtime: beats 13%
    #   Modified threeSum_Ans
    def threeSumClosest(self, nums, target):
        result = []
        nums.sort()
        #   need at least 3 numbers to continue
        for l in range(len(nums)-2):
            #   prevent checking duplicate (again)
            if l > 0 and nums[l] == nums[l-1]:
                continue
            mid = l+1
            r = len(nums)-1
            while mid < r:
                trial = nums[l] + nums[mid] + nums[r]
                if len(result) == 0 or abs(trial-target) < abs(sum(result)-target):
                    result = [nums[l], nums[mid], nums[r]]
                if trial < target:
                    mid += 1
                elif trial > target:
                    r -= 1
                else:
                    #result.append([nums[l], nums[mid], nums[r]])
                    while mid < r and nums[mid] == nums[mid+1]:  # avoid duplicates
                        mid += 1
                    while mid < r and nums[r] == nums[r-1]:  # avoid duplicates
                        r -= 1
                    mid += 1
                    r -= 1
        return sum(result)
        

s = Solution()

values_list = [ [-1,2,1,-4], [0,0,0], [1,1,1,1] ]
target_list = [ 1, 1, 0 ]
check_list = [ 2, 0, 3 ]

for values, target, check in zip(values_list, target_list, check_list):
    result = s.threeSumClosest(values, target)
    print("result=(%s)" % result)
    assert( result == check )


