from typing import List

class Solution:

    def rob(self, nums: List[int]) -> int:
        #self.decisions = {}
        #self.maxRobbedAmount = {}
        #result = self.rob_RecursiveMemorize(nums)
        #print(self.decisions)
        #return result
        #return self.rob_DP(nums)
        return self.rob_DP_SpaceOptimised(nums)



    #   runtime: beats 97%
    def rob_RecursiveMemorize(self, nums: List[int], i: int=0) -> int:
        """Recursively decide whether to skip house i in 'nums', or to rob i and i+1"""
        maxRobbedAmount = dict()
        decisions = dict()

        def rob_solve(nums, i):
            #   no more houses
            if i >= len(nums):
                return 0

            #   used memorized solution
            if i in maxRobbedAmount:
                return maxRobbedAmount[i]

            #   skip current house
            trial_A = rob_solve(nums, i+1)

            #   rob current house
            trial_B = rob_solve(nums, i+2) + nums[i]

            ans = trial_A
            if trial_A < trial_B:
                ans = trial_B

                #   store decision: we are robbing houses i, i+2, and skipping i+1
                decisions[i] = 'rob'
                if i+1 in decisions:
                    del decisions[i+1]
                if i+2 < len(nums):
                    decisions[i+2] = 'rob'

            maxRobbedAmount[i] = ans
            return ans

        result = rob_solve(nums, i)
        print(decisions)
        return result


    #   runtime: beats 37%
    def rob_DP(self, nums: List[int]) -> int:
        decisions = {}
        maxRobbedAmount = [ None for i in range(len(nums)+1) ]

        maxRobbedAmount[len(nums)] = 0
        maxRobbedAmount[len(nums)-1] = nums[len(nums)-1]

        for i in range(len(nums)-2, -1, -1):
            trial_A = maxRobbedAmount[i+1]
            trial_B = maxRobbedAmount[i+2] + nums[i]

            if trial_A < trial_B:
                maxRobbedAmount[i] = trial_B

                #   store decision: we are robbing houses i, i+2, and skipping i+1
                decisions[i] = 'rob'
                if i+1 in decisions:
                    del decisions[i+1]
                if i+2 < len(nums):
                    decisions[i+2] = 'rob'

            else:
                maxRobbedAmount[i] = trial_A

        print(decisions)
        return maxRobbedAmount[0]


    #   runtime: beats 72%
    def rob_DP_SpaceOptimised(self, nums: List[int]) -> int:
        if not nums:
            return 0

        decisions = {}
        N = len(nums)

        rob_next_plus_one = 0
        rob_next = nums[N-1]

        for i in range(N-2, -1, -1):
            trial_A = rob_next
            trial_B = rob_next_plus_one + nums[i]

            rob_next_plus_one = rob_next
            if trial_A < trial_B:
                rob_next = trial_B

                #   we are robbing houses i, i+2, and skipping i+1
                decisions[i] = 'rob'
                if i+1 in decisions:
                    del decisions[i+1]
                if i+2 < len(nums):
                    decisions[i+2] = 'rob'

            else:
                rob_next = trial_A

        print(decisions)
        return rob_next


s = Solution()
test_functions = [ s.rob_RecursiveMemorize, s.rob_DP, s.rob_DP_SpaceOptimised, ] 

input_values = [ [1,2,3,1], [2,7,9,3,1], ]
input_checks = [ 4, 12 ]

for test_func in test_functions:
    print(test_func.__name__)
    for nums, check in zip(input_values, input_checks):
        print("nums=(%s)" % nums)
        result = test_func(nums)
        print("result=(%s)" % str(result))
        assert check == result, "Check failed"
    print()

