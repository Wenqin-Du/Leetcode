
class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res *= 26
            res += ord(s[i]) - ord('A') + 1
        return res
