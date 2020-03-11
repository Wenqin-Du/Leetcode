
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if len(strs) == 0:
            return strs

        solution = {}
        for word in strs:

            orig = word
            origsort = "".join(sorted(word))

            if origsort in solution:
                solution[origsort].append(orig)
            else:
                solution[origsort] = orig

        return list(solution.values())



def groupAnagrams(self, strs):

    d = {}
    for w in sorted(strs):  # 这一步很慢
        key = tuple(sorted(w))
        d[key] = d.get(key, []) + [w]
    return list(d.values())
