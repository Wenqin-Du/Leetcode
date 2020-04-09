
class Solution:
    def isHappy(self, n: int) -> bool:

        track = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in track:
                return False
            track.add(n)
        return True

