from collections import Counter

class Solution:

    #   runtime: beats 12%
    def checkInclusion_Sorting(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_sorted = sorted(s1)
        for l in range(0, len(s2)-len(s1)+1):
            r = min(l+len(s1), len(s2))
            trial = sorted(s2[l:r])
            if trial == s1_sorted:
                return True
        return False


    #   runtime: beats 23%
    def checkInclusion_Counter(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_counts = Counter(s1)
        for l in range(0, len(s2)-len(s1)+1):
            r = min(l+len(s1), len(s2))
            trial = s2[l:r]
            trial_counts = Counter(trial)
            if trial_counts == s1_counts:
                return True
        return False


    #   runtime: beats 80%
    def checkInclusion_RollingCounter(self, s1: str, s2: str) -> bool:
        s1_counts = Counter(s1)
        s2_window_counts = Counter(s2[:len(s1)])

        if s1_counts == s2_window_counts:
            return True

        for i in range(1, len(s2)-len(s1)+1):
            l = s2[i-1]  #  character leaving window
            r = s2[i+len(s1)-1]  # character entering window

            #   Update counter to new window
            s2_window_counts[r] += 1
            s2_window_counts[l] -= 1
            if s2_window_counts[l] == 0:
                del s2_window_counts[l]

            if s1_counts == s2_window_counts:
                return True

        return False


    #   runtime: beats 88%
    def checkInclusion_RollingListCount(self, s1: str, s2: str) -> bool:
        s1_counts = [ 0 for x in range(26) ]
        s2_window_counts = [ 0 for x in range(26) ]

        for c in s1:
            s1_counts[ord(c)-ord('a')] += 1
        for c in s2[0:len(s1)]:
            s2_window_counts[ord(c)-ord('a')] += 1
        if s1_counts == s2_window_counts:
            return True

        for i in range(1, len(s2)-len(s1)+1):
            l = s2[i-1]
            r = s2[i+len(s1)-1]

            s2_window_counts[ord(r)-ord('a')] += 1
            s2_window_counts[ord(l)-ord('a')] -= 1

            if s1_counts == s2_window_counts:
                return True

        return False


s = Solution()
functions = [ s.checkInclusion_Sorting, s.checkInclusion_Counter, s.checkInclusion_RollingCounter, s.checkInclusion_RollingListCount, ]

inputs = [ ("ab", "eidbaooo"), ("ab", "eidboaoo"), ("a", "ab"), ("horse", "ros"), ("adc", "dcda"), ]
checks = [ True, False, True, False, True, ]
assert len(inputs) == len(checks)

for f in functions:
    print(f.__name__)
    for (s1, s2), check in zip(inputs, checks):
        print(f"s1=({s1}), s2=({s2})")
        result = f(s1, s2)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print()

