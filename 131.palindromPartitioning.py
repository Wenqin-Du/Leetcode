
class Solution:
    def partition(self, s: str) -> List[List[str]]:

        if not s:
            return[]

        self.res = []
        self.dfs([], s)
        return self.res

    def isPal(self, s):
        return s == s[:: -1]

    def dfs(self, temp, s):
        if not s:
            self.res.append(temp[:])

        for i in range(1, len(s) + 1):
            if self.isPal(s[: i]):
                temp.append(s[: i])
                self.dfs(temp, s[i:])
                temp.pop()
