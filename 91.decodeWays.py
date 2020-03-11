
class Solution:
    def numDecodings(self, s: str) -> int:
        if s == "" or s[0] == "0":
            return 0
        dp = [0] * (len(s) + 1)
        dp[0] = dp[1] = 1

        for i in range(2, (len(s) + 1)):
            if s[i-1] == "0" and not ("10" <= s[i-2:i] <= "26"):
                dp[i] = 0
            elif s[i-1] != "0" and "10" <= s[i-2:i] <= "26":
                dp[i] = dp[i-1] + dp[i-2]
            elif s[i-1] != "0" and not ("10" <= s[i-2:i] <= "26"):
                dp[i] = dp[i-1]
            else:
                dp[i] = dp[i-2]

        return dp[-1]
