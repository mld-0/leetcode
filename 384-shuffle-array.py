#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=2:
#   }}}1
from typing import List
import random
#   {{{2
def is_sortable(obj):
    cls = obj.__class__
    return cls.__lt__ != object.__lt__ or cls.__gt__ != object.__gt__

class Solution:

    def __init__(self, nums: List[int]):
        """Initalize with values 'nums'"""
        self.nums_initial = nums

    def reset(self) -> List[int]:
        """Resets array to origional configuration and return it"""
        self.nums_shuffled = self.nums_initial
        return self.nums_initial


    #   runtime: beats 95%
    def shuffle_Pythonic(self) -> List[int]:
        """Returns a random shuffling of array"""
        self.nums_shuffled = self.nums_initial[:]
        random.shuffle(self.nums_shuffled)
        return self.nums_shuffled

    
    #   runtime: beats 46%
    def shuffle_Selection(self) -> List[int]:
        values = self.nums_initial[:]
        self.nums_shuffled = []

        while len(values) > 0:
            rand_index = random.randint(0, len(values)-1)
            rand_choice = values.pop(rand_index)
            self.nums_shuffled.append(rand_choice)

        return self.nums_shuffled


    #   runtime: beats 56%
    def shuffle_FisherYates(self) -> List[int]:
        self.nums_shuffled = self.nums_initial[:]
        for i in range(len(self.nums_shuffled)):
            swap_i = random.randint(i, len(self.nums_shuffled)-1)
            self.nums_shuffled[i], self.nums_shuffled[swap_i] = self.nums_shuffled[swap_i], self.nums_shuffled[i]
        return self.nums_shuffled


input_values = [ [1,2,3], ]

for nums in input_values:
    print("nums=(%s)" % nums)
    s = Solution(nums)

    result = s.reset()
    assert result == nums, "Check comparison failed"
    result = s.shuffle_Pythonic()
    print("result=(%s)" % result)
    assert is_sortable(result), "Check is_sortable failed"
    assert sorted(result) == sorted(nums), "Check comparison failed"

    result = s.reset()
    assert result == nums, "Check comparison failed"
    result = s.shuffle_Selection()
    print("result=(%s)" % result)
    assert is_sortable(result), "Check is_sortable failed"
    assert sorted(result) == sorted(nums), "Check comparison failed"

    result = s.reset()
    assert result == nums, "Check comparison failed"
    result = s.shuffle_FisherYates()
    print("result=(%s)" % result)
    assert is_sortable(result), "Check is_sortable failed"
    assert sorted(result) == sorted(nums), "Check comparison failed"

    print()

