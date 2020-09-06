
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic1, dic2 = {}, {}
        for i,v in enumerate(s):
            dic1[v] = dic1.get(v, []) + [i]
        for i,v in enumerate(t):
            dic2[v] = dic2.get(v, []) + [i]

        return sorted(dic1.values()) == sorted(dic2.values())
