
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = dict()
        for name in list(s):
            counts[name] = counts.get(name, 0) + 1
        for k in counts:
            if counts[k] == 1:
                return list(s).index(k)
        return -1

        # Slow way

        # for i,j in enumerate(s):
        #     if(s.count(j) == 1):
        #         return i
        # return -1
