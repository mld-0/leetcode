import time
import copy

class Solution:

    #   runtime: beats 70%
    def reverseWords_pythonic_i(self, s: str) -> str:
        return ' '.join(s.split()[::-1])


    #   runtime: beats 73%
    def reverseWords_pythonic_ii(self, s: str) -> str:
        return ' '.join(reversed(s.split()))


s = Solution()
test_functions = [ s.reverseWords_pythonic_i, s.reverseWords_pythonic_ii, ]

inputs = [ "the sky is blue", "  hello world  ", "a good   example", "The black-and-yellow broadbill Eurylaimus ochromalus is a species of bird in the typical broadbill family Eurylaimidae. A small, distinctive species, it has a black head, breastband, and upperparts, a white neckband, yellow streaking on the back and wings, and vinous-pink underparts that turn yellow towards the belly. The beak is bright blue, with a green tip to the upper mandible and black edges. It shows some sexual dimorphism, with the black breastband being incomplete in females", ]
checks = [ "blue is sky the", "world hello", "example good a", "females in incomplete being breastband black the with dimorphism, sexual some shows It edges. black and mandible upper the to tip green a with blue, bright is beak The belly. the towards yellow turn that underparts vinous-pink and wings, and back the on streaking yellow neckband, white a upperparts, and breastband, head, black a has it species, distinctive small, A Eurylaimidae. family broadbill typical the in bird of species a is ochromalus Eurylaimus broadbill black-and-yellow The", ]
assert len(inputs) == len(checks)

for f in test_functions:
    inputs_copy = copy.deepcopy(inputs)
    print(f.__name__)
    startTime = time.time()
    for s, check in zip(inputs_copy, checks):
        print(f"s=({s})")
        result = f(s)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_ms=(%0.2f)" % ((time.time() - startTime) * 1000000))
    print()

