
class Solution:
    def numTrees(self, n: int) -> int:
        ### Bottom up
        l = [0] * (n+1)
        l[0], l[1] = 1, 1
        for i in range(2, n+1):
            for j in range(i):
                l[i] += l[j] * l[i -j - 1]

        return l[-1]
