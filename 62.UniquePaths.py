
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        A = [[1 for i in range(m)] for j in range(n)]

        for i in range(1, n):
            for j in range(1, m):
                A[i][j] = A[i-1][j] + A[i][j-1]

        return A[n-1][m-1]




