from typing import List

class Solution:

    #   runtime: beats 66%
    def isIsomorphic_i(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mapping = dict()
        for c_s, c_t in zip(s, t):
            if c_s in mapping.keys():
                if c_t != mapping[c_s]:
                    return False
            else:
                mapping[c_s] = c_t

        if len(mapping.values()) != len(set(mapping.values())):
            return False
        else:
            return True


    #   runtime: beats 25%
    def isIsomorphic_ans_TwoDicts(self, s: str, t: str) -> bool:
        mapping_s2t = dict()
        mapping_t2s = dict()

        for c_s, c_t in zip(s, t):
            if (not c_s in mapping_s2t) and (not c_t in mapping_t2s):
                mapping_s2t[c_s] = c_t
                mapping_t2s[c_t] = c_s
            elif mapping_s2t.get(c_s) != c_t or mapping_t2s.get(c_t) != c_s:
                return False

        return True


    #   runtime: beats 55%
    def isIsomorphic_ans_TwoLists(self, s: str, t: str) -> bool:
        mapping_s2t = [ None for i in range(256) ]
        mapping_t2s = [ None for i in range(256) ]

        for c_s, c_t in zip(s, t):
            i_s = ord(c_s)
            i_t = ord(c_t)
            if (mapping_s2t[i_s] == None) and (mapping_t2s[i_t] == None):
                mapping_s2t[i_s] = c_t
                mapping_t2s[i_t] = c_s
            elif mapping_s2t[i_s] != c_t or mapping_t2s[i_t] != c_s:
                return False

        return True


    #   runtime: beats 17%
    def isIsomorphic_ans_FirstOccurenceTransform(self, s: str, t: str) -> bool:
        def transform(s: str) -> List[int]:
            index_map = dict()
            result = []
            for i, c in enumerate(s):
                if not c in index_map.keys():
                    index_map[c] = i
                result.append(index_map[c])
            return result

        return transform(s) == transform(t)


    #   runtime: beats 45%
    def isIsomorphic_ans_OneLiner(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))


s = Solution()
test_functions = [ s.isIsomorphic_i, s.isIsomorphic_ans_TwoDicts, s.isIsomorphic_ans_TwoLists, s.isIsomorphic_ans_FirstOccurenceTransform, s.isIsomorphic_ans_OneLiner, ]

inputs = [ ("egg", "add"), ("foo", "bar"), ("paper", "title"), ]
checks = [ True, False, True, ]
assert len(inputs) == len(checks)

for f in test_functions:
    print(f.__name__)
    for (s, t), check in zip(inputs, checks):
        print(f"s=({s}), t=({t})")
        result = f(s, t)
        print(f"result=({result})")
        assert result == check
    print()

