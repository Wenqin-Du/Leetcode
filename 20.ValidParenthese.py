
class Solution:
    def isValid(self, s: str) -> bool:

        dic = {'}': '{',
               ')': '(',
               ']': '['}
        front = dic.values()
        track = []

        for p in s:
            if p in front:
                track.append(p)
            elif len(track) > 0 and track[-1] == dic[p]:
                track.pop()
            else:
                return False

        return len(track) == 0
