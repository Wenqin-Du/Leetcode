
class Solution:
    def numSquares(self, n: int) -> int:

        dp = [0] + [float('inf')] * (n)
        for i in range(1, n+1):
            for a in range(1, int(i**0.5)+1):
                dp[i] = min(dp[i], dp[i - a**2] + 1)
        return dp[-1]

        # Better way:

        # dp = [0] + [float('inf')]*n
        # for i in range(1, n+1):
        #     dp[i] = min(dp[i-j*j] for j in range(1, int(i**0.5)+1)) + 1
        # return dp[n]
